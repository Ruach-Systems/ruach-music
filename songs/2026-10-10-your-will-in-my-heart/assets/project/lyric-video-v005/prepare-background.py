from pathlib import Path
import subprocess,imageio_ffmpeg
P=Path(__file__).resolve().parent
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-y','-v','error','-i',str(P/'visuals/aurora-meadow-loop.mp4'),'-vf','scale=3840:2160:flags=lanczos,unsharp=5:5:0.25:3:3:0,drawbox=x=0:y=0:w=iw:h=ih:color=black@0.30:t=fill,vignette=PI/6','-c:v','h264_nvenc','-preset','p5','-rc','vbr','-cq','14','-b:v','0','-pix_fmt','yuv420p',str(P/'visuals/aurora-meadow-4k-prepared.mp4')],check=True)
