from pathlib import Path
import json,subprocess,hashlib
import imageio_ffmpeg
import av
P=Path(__file__).resolve().parent
S=P.parents[2]
V=S/'assets/video/ruach-your-will-in-my-heart-lyric-video-v005-4k.mp4'
FF=imageio_ffmpeg.get_ffmpeg_exe()
with av.open(str(V)) as container:
    streams=[{'type':s.type,'codec':s.codec_context.name,'duration':float(s.duration*s.time_base) if s.duration else None,'width':getattr(s.codec_context,'width',None),'height':getattr(s.codec_context,'height',None)} for s in container.streams]
    duration=container.duration/av.time_base
    assert container.streams.video[0].width==3840 and container.streams.video[0].height==2160
r=subprocess.run([FF,'-v','error','-i',str(V),'-f','null','-'],capture_output=True,text=True)
assert r.returncode==0,r.stderr
cues=json.loads((P/'cues.json').read_text(encoding='utf-8'))
assert len(cues)==60
assert all(c['start'] <= c['vocal_start'] < c['vocal_end'] <= c['end'] for c in cues)
assert all(w['start'] >= c['start'] and w['end'] <= c['end'] for c in cues for w in c['words'])
assert all(0<=c['start']<c['end']<=duration for c in cues)
assert all(a['end']<=b['start'] for a,b in zip(cues,cues[1:]))
shots=[]
for t in [4,42,55,131,175,231,250]:
    out=P/f'check-{t:03}.jpg'
    subprocess.run([FF,'-v','error','-ss',str(t),'-i',str(V),'-frames:v','1','-update','1',str(out)],check=True)
    shots.append(out.name)
from PIL import Image,ImageOps,ImageDraw
sheet=Image.new('RGB',(960,3*295),(12,15,22))
for i,name in enumerate(shots[:6]):
    im=Image.open(P/name).resize((480,270));sheet.paste(im,((i%2)*480,(i//2)*295));ImageDraw.Draw(sheet).text(((i%2)*480+12,(i//2)*295+275),name,fill='white')
sheet.save(P/'contact-sheet.jpg',quality=92)
import numpy as np
def decoded(path):
    raw=subprocess.run([FF,'-v','error','-i',str(path),'-map','0:a:0','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw,dtype=np.float32)
x=decoded(S/'assets/audio/branded/ruach-your-will-in-my-heart-v2-slow-branded-v001.mp3');y=decoded(V);n=min(len(x),len(y));corr=float(np.corrcoef(x[:n],y[:n])[0,1])
assert corr>.98, f'Audio alignment correlation {corr}'
ass=(P/'lyrics.ass').read_text(encoding='utf-8-sig')
assert 'Dialogue: 2,' not in ass and 'Dialogue: 3,' not in ass
assert ass.count('\\pos(960,490)')==60
result={'word_highlighting':False,'next_line_preview':True,'background_source':'1920x1080 upscaled with Lanczos and light sharpening; typography rendered at 4K','source_audio_correlation':corr,'output':str(V.relative_to(S)),'duration_seconds':duration,'bytes':V.stat().st_size,'sha256':hashlib.sha256(V.read_bytes()).hexdigest(),'streams':streams,'full_decode_passed':True,'lyric_cues':len(cues),'all_cue_ranges_valid':True,'subtitle_overlaps':False,'audio_changes':'AAC encode at 224 kbps for MP4; no speed change, processing, added sound, or trim intended','visual_qa_frames_seconds':[4,42,55,131,175,231,250],'human_full_listening_review':'pending','timing_method':'Vocal-stem CTC word alignment and vocal energy release tracking; full listening approval pending'}
(P/'verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
