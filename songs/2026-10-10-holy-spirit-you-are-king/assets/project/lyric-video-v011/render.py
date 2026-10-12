from pathlib import Path
import json,subprocess,argparse,shutil,math
from PIL import ImageFont
from mutagen.mp3 import MP3
import imageio_ffmpeg
P=Path(__file__).resolve().parent
S=P.parents[2]; R=S.parents[1]
A=S/'assets/audio/branded/ruach-holy-spirit-you-are-king-take-01-branded-v001.mp3'
V=S/'assets/video/ruach-holy-spirit-you-are-king-lyric-video-v011-1080p.mp4'
D=MP3(A).info.length
FF=imageio_ffmpeg.get_ffmpeg_exe()
def stamp(s):
    n=round(s*100);return f'{n//360000}:{n//6000%60:02}:{n//100%60:02}.{n%100:02}'
def srt(s):
    n=round(s*1000);return f'{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}'
def prepare():
    (P/'fonts').mkdir(exist_ok=True); V.parent.mkdir(exist_ok=True)
    shutil.copy2(R/'channel/ruach-anthem/Manrope-600.ttf',P/'fonts/Manrope-600.ttf')
    shutil.copy2(R/'channel/ruach-anthem/Manrope-OFL.txt',P/'Manrope-OFL.txt')
    cues=json.loads((P/'cues.json').read_text())
    font=ImageFont.truetype(str(P/'fonts/Manrope-600.ttf'),100)
    widths=[font.getlength(c['text']) for c in cues]
    sizes=[min(100,math.floor(1680/w*100)) for w in widths]
    assert min(sizes)>=96, min(sizes)
    header="""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,Manrope-600,100,&H00F3F5F4,&H00F3F5F4,&H5018100B,&H7018100B,0,0,0,0,100,100,0,0,1,1.5,2,5,120,120,0,1
Style: Title,Manrope-600,88,&H00F3F5F4,&H00F3F5F4,&H6018100B,&H7018100B,0,0,0,0,100,100,0,0,1,1,1,5,120,120,0,1
Style: Small,Manrope-600,30,&H00F3F5F4,&H00F3F5F4,&H6018100B,&H7018100B,0,0,0,0,100,100,0,0,1,0,1,5,100,100,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev=[]
    def add(a,b,style,text):
        ev.append(f'Dialogue: 0,{stamp(a)},{stamp(b)},{style},,0,0,0,,{text}')
    first=cues[0]['start']
    add(0,first-.35,'Title',r'{\pos(960,465)\fad(900,450)}Holy Spirit, You Are King')
    add(0,first-.35,'Small',r'{\pos(960,566)\fsp4\fad(900,450)}LYRIC VIDEO')
    add(first,D,'Small',r'{\pos(960,120)\fs44\fad(250,600)}HOLY SPIRIT, YOU ARE KING')
    add(first,D,'Small',r'{\pos(914,190)\an7\c&HACAF8D&\bord0\shad0\p1\fad(250,600)}m 0 0 l 92 0 92 3 0 3')
    add(0,D,'Small',r'{\pos(330,983)\fs26\fad(700,700)}Governed by the Spirit.')
    add(0,D,'Small',r'{\pos(1705,983)\fs48\fsp5\fad(700,700)}RUACH')
    for i,c in enumerate(cues):
        add(c['start'],c['end'],'Lyric',r'{\pos(960,490)\fad(60,0)\fs'+str(sizes[i])+'}'+c['text'])
        if i+1<len(cues) and cues[i+1]['start']-c['end']<2:
            add(c['start'],c['end'],'Small',r'{\pos(960,615)\fs56\1c&HD0CEBE&\alpha&H20&\fad(100,0)}'+cues[i+1]['text'])
    add(cues[-1]['end']+1,D,'Title',r'{\pos(960,465)\fad(900,1600)}Holy Spirit, You are King.')
    (P/'lyrics.ass').write_text(header+'\n'.join(ev)+'\n',encoding='utf-8-sig')
    (P/'lyrics.srt').write_text('\n\n'.join(f"{i}\n{srt(c['start'])} --> {srt(c['end'])}\n{c['text']}" for i,c in enumerate(cues,1))+'\n')
    (P/'typography-check.json').write_text(json.dumps(dict(font='Manrope 600',current_lyric_px_range=[min(sizes),max(sizes)],next_line_px=56,title_header_px=44,safe_width_px=1680,max_lyric_width_px=max(w*s/100 for w,s in zip(widths,sizes)),current_min_font_at_390px_width=min(sizes)*390/1920,next_font_at_390px_width=56*390/1920),indent=2))
def command(out,preview=None):
    filt="[0:v]eq=gamma=0.94:saturation=1.13:contrast=1.025:brightness=-0.008,ass=lyrics.ass:fontsdir=fonts[v]"
    cmd=[FF,'-y','-hide_banner','-loglevel','warning','-stream_loop','-1','-i','visuals/aurora-meadow-loop.mp4','-i',str(A),'-filter_complex',filt,'-map','[v]']
    if preview is not None:return cmd+['-ss',str(preview),'-frames:v','1','-update','1',str(out)]
    return cmd+['-map','1:a:0','-t',str(D),'-r','30','-c:v','h264_nvenc','-preset','p5','-cq','18','-b:v','0','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-movflags','+faststart','-metadata','title=Holy Spirit, You Are King by RUACH','-metadata','artist=RUACH',str(out)]
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--preview',type=float);args=ap.parse_args();prepare()
    out=P/f'preview-{args.preview:g}.jpg' if args.preview is not None else V
    subprocess.run(command(out,args.preview),cwd=P,check=True)
    print(out)
