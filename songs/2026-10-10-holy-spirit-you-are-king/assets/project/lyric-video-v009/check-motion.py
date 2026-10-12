from pathlib import Path
import json, subprocess
import numpy as np, imageio_ffmpeg
from PIL import Image, ImageDraw
P=Path(__file__).resolve().parent
FF=imageio_ffmpeg.get_ffmpeg_exe()
v=P/'visuals/aurora-meadow-loop.mp4'
raw=subprocess.check_output([FF,'-v','error','-i',str(v),'-vf','scale=480:270','-f','rawvideo','-pix_fmt','rgb24','-'])
frames=np.frombuffer(raw,dtype=np.uint8).reshape((-1,270,480,3))
normal=np.abs(frames[1:].astype(np.int16)-frames[:-1].astype(np.int16)).mean(axis=(1,2,3))
seam=float(np.abs(frames[0].astype(np.int16)-frames[-1].astype(np.int16)).mean())
report=json.loads((P/'visuals/loop-verification.json').read_text())
star_ranges=[]
for star in report['bright_stars']:
    sx=round(star['x']/4);sy=round(star['y']/4)
    values=frames[::15,max(0,sy-1):sy+2,max(0,sx-1):sx+2,:].max(axis=(1,2,3)).astype(float)
    star_ranges.append(float(np.ptp(values)))
report['encoded_bright_star_intensity_ranges']=star_ranges
assert sum(v>3 for v in star_ranges)>=12, 'Twinkle should register in encoded output'
import cv2
f0=cv2.cvtColor(frames[0],cv2.COLOR_RGB2GRAY)
f1=cv2.cvtColor(frames[75],cv2.COLOR_RGB2GRAY)
flow=cv2.calcOpticalFlowFarneback(f0,f1,None,.5,3,15,3,5,1.2,0)
grass_motion=np.linalg.norm(flow[218:255,70:400],axis=2)
report['encoded_grass_motion_median_px_at_480']=float(np.median(grass_motion))
assert report['encoded_grass_motion_median_px_at_480']>.1, 'Grass movement should register in encoded output'
report.update(decode_ok=True,decoded_frames=len(frames),encoded_seam_mean_change=seam,encoded_normal_mean_change=float(normal.mean()),encoded_seam_to_normal_ratio=seam/float(normal.mean()))
assert len(frames)==900
print('Seam diagnostics:', seam, float(normal.mean()), report['encoded_seam_to_normal_ratio'])
assert report['encoded_seam_to_normal_ratio']<2, 'Encoded loop join requires smoothing'
(P/'visuals/loop-verification.json').write_text(json.dumps(report,indent=2))
sheet=Image.new('RGB',(960,580),(12,18,23))
for i,n in enumerate([0,150,300,450]):
    x=(i%2)*480;y=(i//2)*290
    sheet.paste(Image.fromarray(frames[n]),(x,y));ImageDraw.Draw(sheet).text((x+8,y+274),f'{n/30:g} seconds',fill='white')
sheet.save(P/'firefly-flight-comparison.jpg',quality=94)
subprocess.run([FF,'-y','-v','error','-i',str(v),'-t','15','-vf','scale=960:540','-an','-c:v','h264_nvenc','-cq','20',str(P/'firefly-motion-preview.mp4')],check=True)
print({k:report[k] for k in ['firefly_count','decoded_frames','encoded_seam_to_normal_ratio']})
