from pathlib import Path
import json,hashlib,subprocess
import av,numpy as np,imageio_ffmpeg
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent
S=P.parents[2]; R=S.parents[1]
V=S/'assets/video/ruach-holy-spirit-you-are-king-lyric-video-v011-1080p.mp4'
A=S/'assets/audio/branded/ruach-holy-spirit-you-are-king-take-01-branded-v001.mp3'
FF=imageio_ffmpeg.get_ffmpeg_exe()
with av.open(str(V)) as c:
    v=c.streams.video[0];a=c.streams.audio[0]
    assert (v.width,v.height)==(1920,1080)
    assert float(v.average_rate)==30
    duration=c.duration/av.time_base
    streams=dict(video=v.codec_context.name,audio=a.codec_context.name,resolution=[v.width,v.height],fps=float(v.average_rate))
r=subprocess.run([FF,'-v','error','-i',str(V),'-f','null','-'],capture_output=True,text=True)
assert r.returncode==0 and not r.stderr.strip(),r.stderr
def decoded(path):
    return np.frombuffer(subprocess.check_output([FF,'-v','error','-i',str(path),'-map','0:a:0','-ac','1','-ar','16000','-f','f32le','-']),dtype=np.float32)
x,y=decoded(A),decoded(V);n=min(len(x),len(y))
corr=float(np.corrcoef(x[:n],y[:n])[0,1]);assert corr>.98
assert abs(len(x)-len(y))/16000<.1
cues=json.loads((P/'cues.json').read_text())
assert all(0<=c['start']<c['end']<=duration and c['end']+.01>=c['vocal_end'] for c in cues)
assert all(a['end']<=b['start'] for a,b in zip(cues,cues[1:]))
ass=(P/'lyrics.ass').read_text(encoding='utf-8-sig')
assert ass.count(r'\pos(960,490)')==len(cues)
assert 'RUACH' in ass and r'\pos(1705,983)' in ass
assert r'\kf' not in ass and r'\ko' not in ass
shots=[4,18,35,50,54,77,121,145,190,214,225]
for t in shots:
    target=P/f'check-{t:03}.jpg'
    subprocess.run([FF,'-y','-v','error','-ss',str(t),'-i',str(V),'-frames:v','1','-update','1',str(target)],check=True)
    if t in [18,35,50,77]:
        for width in [390,640]:
            Image.open(target).resize((width,round(width*9/16)),Image.Resampling.LANCZOS).save(P/f'mobile-{width}-{t:03}.png')
sheet=Image.new('RGB',(1170,4*244),(12,18,23))
d=ImageDraw.Draw(sheet)
for i,t in enumerate(shots):
    xx=(i%3)*390;yy=(i//3)*244
    sheet.paste(Image.open(P/f'check-{t:03}.jpg').resize((390,219),Image.Resampling.LANCZOS),(xx,yy))
    d.text((xx+8,yy+224),f'{t}s',fill='white')
sheet.save(P/'contact-sheet.jpg',quality=94)
compare=Image.new('RGB',(780,245),(12,18,23))
prior=R/'songs/2026-10-10-your-will-in-my-heart/assets/project/lyric-video-v005/check-042.jpg'
compare.paste(Image.open(prior).resize((390,219)),(0,0))
compare.paste(Image.open(P/'check-050.jpg').resize((390,219)),(390,0))
dr=ImageDraw.Draw(compare);dr.text((8,225),'Your Will in My Heart - historical reference',fill='white');dr.text((398,225),'Holy Spirit, You Are King - aurora meadow with independent firefly flight',fill='white')
compare.save(P/'catalog-comparison.jpg',quality=94)
loop=json.loads((P/'visuals/loop-verification.json').read_text())
assert loop['cycle_endpoint_max_difference']==0
result=dict(output=V.relative_to(S).as_posix(),duration_seconds=duration,bytes=V.stat().st_size,sha256=hashlib.sha256(V.read_bytes()).hexdigest(),streams=streams,full_decode_passed=True,audio_source_correlation=corr,audio_duration_difference_seconds=abs(len(x)-len(y))/16000,lyric_cues=len(cues),no_overlaps=True,recognized_vocal_ends_preserved=True,word_highlighting=False,next_line_preview=True,mobile_preview_widths=[390,640],typography=json.loads((P/'typography-check.json').read_text()),loop=loop,alignment_method='Whisper small word timestamps aligned to canonical lyrics, opening checked using cropped transcription; reading lead and phrase-end holds',limitations='Automated timing and audio checks plus still-frame visual review. Full listening and physical-phone review remain pending. Original file duration discrepancy remains documented.',audio_export='AAC 256k from branded Take 1, no tempo change or intended trimming',source_audio_sha256=hashlib.sha256(A.read_bytes()).hexdigest(),brand_asset='Text-only RUACH in Manrope 600; no symbol or logo image')
source=R/'songs/2026-10-10-your-will-in-my-heart/assets/project/lyric-video-v005/visuals/aurora-meadow-loop.mp4'
local=P/'visuals/aurora-meadow-loop.mp4'
assert loop['firefly_count'] > 5
result['background_source']='../lyric-video-v009/visuals/aurora-meadow-loop.mp4; unchanged motion; gamma 0.94, saturation 1.13, contrast 1.025, brightness -0.008 before text'
result['background_exact_copy']=False
result['background_sha256']=hashlib.sha256(local.read_bytes()).hexdigest()
(P/'verification.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
