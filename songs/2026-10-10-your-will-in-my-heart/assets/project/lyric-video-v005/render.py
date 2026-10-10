from pathlib import Path
import json, subprocess, argparse
from PIL import ImageFont
import imageio_ffmpeg
from mutagen.mp3 import MP3
P=Path(__file__).resolve().parent
SONG=P.parents[2]
FF=imageio_ffmpeg.get_ffmpeg_exe()
AUDIO=SONG/'assets/audio/branded/ruach-your-will-in-my-heart-v2-slow-branded-v001.mp3'
OUTPUT=SONG/'assets/video/ruach-your-will-in-my-heart-lyric-video-v005-4k.mp4'
DURATION=MP3(AUDIO).info.length

def stamp(s):
    cs=round(s*100); return f'{cs//360000}:{cs//6000%60:02}:{cs//100%60:02}.{cs%100:02}'
def srtstamp(s):
    ms=round(s*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
def prepare():
    cues=json.loads((P/'cues.json').read_text(encoding='utf-8'))
    header='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,RUACH Lyric,80,&H00F4F4F8,&H00FFFFFF,&H70120D09,&H90120D09,0,0,0,0,100,100,0,0,1,1.4,2,5,140,140,0,1
Style: Title,RUACH Lyric,82,&H00F4F4F8,&H00FFFFFF,&H70120D09,&H90120D09,0,0,0,0,100,100,0,0,1,1,2,5,140,140,0,1
Style: Small,RUACH Lyric,22,&H00D9D4D0,&H00FFFFFF,&H70120D09,&H90120D09,0,0,0,0,100,100,4,0,1,0,1,5,100,100,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
    events=[]
    def add(start,end,style,text):events.append(f'Dialogue: 0,{stamp(start)},{stamp(end)},{style},,0,0,0,,{text}')
    first=cues[0]['start']; intro_end=max(1,first-.35)
    add(0,intro_end,'Title',r'{\fad(1200,600)\pos(960,465)}Your Will in My Heart')
    add(0,intro_end,'Small',r'{\fad(1200,600)\pos(960,566)}LYRIC VIDEO')
    add(first,DURATION,'Small',r'{\fad(500,800)\pos(960,120)}YOUR WILL IN MY HEART')
    add(first,DURATION,'Small',r'{\fad(500,800)\pos(914,190)\an7\c&H3520AE&\bord0\shad0\p1}m 0 0 l 92 0 92 3 0 3')
    add(0,DURATION,'Small',r'{\fad(800,800)\pos(330,983)}GOVERNED BY THE SPIRIT.')
    def event(start,end,style,text,layer=1):
        if end>start:events.append(f'Dialogue: {layer},{stamp(start)},{stamp(end)},{style},,0,0,0,,{text}')
    for ci,c in enumerate(cues):
        event(c['start'],c['end'],'Lyric',r'{\pos(960,490)\fad(100,100)}'+c['text'])
        if ci+1<len(cues) and cues[ci+1]['start']-c['end']<3:
            event(c['start'],c['end'],'Small',r'{\pos(960,615)\fs30\fsp0\1c&HC7C2BE&\alpha&H55&\fad(250,180)}'+cues[ci+1]['text'])
    if DURATION-cues[-1]['end']>2:
        add(cues[-1]['end']+.4,DURATION,'Title',r'{\fad(800,1200)\pos(960,465)}Your will be done.')
    (P/'lyrics.ass').write_text(header+'\n'.join(events)+'\n',encoding='utf-8-sig')
    (P/'lyrics.srt').write_text('\n\n'.join(f"{i}\n{srtstamp(c['start'])} --> {srtstamp(c['end'])}\n{c['text']}" for i,c in enumerate(cues,1))+'\n',encoding='utf-8')

def command(output,preview=None):
    f="[0:v]null[bg];[2:v]scale=460:-1:flags=lanczos[logo];[bg][logo]overlay=W-w-200:H-h-140,ass=lyrics.ass:fontsdir=caption-fonts[v]"
    cmd=[FF,'-y','-hide_banner','-loglevel','warning','-stream_loop','-1','-i','visuals/aurora-meadow-4k-prepared.mp4','-i',str(AUDIO),'-loop','1','-i','visuals/ruach-lockup-white.png','-filter_complex',f,'-map','[v]']
    if preview is not None:return cmd+['-ss',str(preview),'-frames:v','1','-update','1',str(output)]
    return cmd+['-map','1:a:0','-t',str(DURATION),'-r','30','-c:v','h264_nvenc','-preset','p5','-rc','vbr','-cq','17','-b:v','0','-pix_fmt','yuv420p','-c:a','aac','-b:a','224k','-movflags','+faststart','-metadata','title=Your Will in My Heart â€” RUACH Lyric Video','-metadata','artist=RUACH',str(output)]
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--preview',type=float);args=ap.parse_args();prepare()
    out=P/f'preview-{args.preview:g}.jpg' if args.preview is not None else OUTPUT
    subprocess.run(command(out,args.preview),cwd=P,check=True)
    print(out)
