from pathlib import Path
import json,math,subprocess
import cv2,numpy as np,imageio_ffmpeg
from PIL import Image
P=Path(__file__).resolve().parent
W,H,FPS,D=1920,1080,30,30
cv2.setNumThreads(4)
base=np.array(Image.open(P/'visuals/clean-meadow.png').convert('RGB').resize((W,H),Image.Resampling.LANCZOS),dtype=np.float32)
y,x=np.mgrid[:H,:W].astype(np.float32);xn=x/W;yn=y/H
soft=cv2.GaussianBlur(base,(0,0),12)
sky=np.clip((.68-yn)/.14,0,1)
colour=np.clip((soft[:,:,1]-soft[:,:,0]-8)/34,0,1)*np.clip((.63-yn)/.13,0,1)
aurora=soft*colour[:,:,None]
grass=np.clip((yn-.75)/.25,0,1)**2
# Isolate the actual brighter stars; twinkle their detail, not the surrounding sky.
detail=np.maximum(base-cv2.GaussianBlur(base,(0,0),2),0)
hot=((detail.max(axis=2)>70)&(base.max(axis=2)>170)&(yn<.59)).astype(np.uint8)
count,labels,stats,centres=cv2.connectedComponentsWithStats(hot)
candidates=[]
for i in range(1,count):
    if 1<=stats[i,4]<=80:
        cx,cy=centres[i]; candidates.append((float(base[labels==i].max()),float(cx),float(cy)))
candidates.sort(reverse=True)
stars=[]
for brightness,cx,cy in candidates:
    if all((cx-s['x'])**2+(cy-s['y'])**2>28**2 for s in stars):
        stars.append(dict(x=cx,y=cy,phase=len(stars)*1.618))
    if len(stars)==24:break
star_patches=[]
for s in stars:
    cx,cy=s['x'],s['y'];xa=max(0,int(cx)-10);xb=min(W,int(cx)+11);ya=max(0,int(cy)-10);yb=min(H,int(cy)+11)
    falloff=np.exp(-((x[ya:yb,xa:xb]-cx)**2+(y[ya:yb,xa:xb]-cy)**2)/32)
    star_patches.append((xa,xb,ya,yb,detail[ya:yb,xa:xb]*falloff[:,:,None],s['phase']))
rng=np.random.default_rng(73)
# Every large foreground light is now its own moving object, not part of the grass.
anchors=[(.08,.72),(.04,.85),(.13,.89),(.18,.78),(.25,.79),(.40,.78),(.59,.92),(.75,.82),(.80,.94),(.91,.78),(.93,.88),(.96,.79)]
paths=[]
for i,(xx,yy) in enumerate(anchors):
    paths.append(dict(x=xx*W,y=yy*H,radius=3.8 if i in [2,10] else 2.4,ax=float(rng.uniform(42,75)),ay=float(rng.uniform(22,45)),phase=float(rng.uniform(0,6.28)),phase2=float(rng.uniform(0,6.28)),kind='large'))
for i in range(18):
    paths.append(dict(x=float(rng.uniform(100,1820)),y=float(rng.uniform(825,1020)),radius=1.2,ax=float(rng.uniform(35,65)),ay=float(rng.uniform(16,35)),phase=float(rng.uniform(0,6.28)),phase2=float(rng.uniform(0,6.28)),kind='small'))
def pos(p,t):
    u=2*np.pi*t/D
    return p['x']+p['ax']*np.sin(u+p['phase'])+9*np.sin(2*u+p['phase2']),p['y']+p['ay']*np.sin(u+p['phase2'])+6*np.sin(3*u+p['phase'])
def scene(t):
    a=2*np.pi*(t%10)/10
    dx=(9*np.sin(a+yn*6)+5*np.cos(a+xn*5))*sky
    dy=4*np.sin(a+xn*5)*sky
    shifted=cv2.remap(aurora,x+dx,y+dy,cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT_101)
    im=base+(shifted-aurora)*.82+aurora*(.035*np.sin(a+xn*4))[:,:,None]
    for xa,xb,ya,yb,patch,phase in star_patches:
        im[ya:yb,xa:xb]+=patch*(.40*np.sin(a+phase))
    # The meadow moves in a low breeze. Foreground tips move more than roots.
    depth=np.clip((yn-.745)/.255,0,1)
    sway=6*np.sin(np.pi*depth)**1.2+.6*depth
    stalk=7*np.exp(-((xn-.035)/.075)**4)*np.clip((yn-.55)/.08,0,1)*np.clip((.98-yn)/.35,0,1)
    wind=(sway+stalk)*(np.sin(a+xn*5)+.15*np.sin(2*a+xn*9))
    vertical=.35*sway*np.sin(a+xn*5+.7)
    return np.uint8(np.clip(cv2.remap(im,x+wind,y+vertical,cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT_101),0,255))
def draw(a,t):
    a=a.copy()
    for p in paths:
        px,py=pos(p,t);r=p['radius'];reach=int(r*5+3)
        xa=max(0,int(px)-reach);xb=min(W,int(px)+reach+1);ya=max(0,int(py)-reach);yb=min(H,int(py)+reach+1)
        if xa>=xb or ya>=yb:continue
        d=(x[ya:yb,xa:xb]-px)**2+(y[ya:yb,xa:xb]-py)**2
        glow=np.exp(-d/(2*r*r))+.10*np.exp(-d/(2*(r*2.5)**2))
        pulse=.84+.16*np.sin(4*np.pi*t/D+p['phase'])
        a[ya:yb,xa:xb]=np.clip(a[ya:yb,xa:xb].astype(float)+glow[:,:,None]*np.array([255,198,89])*pulse,0,255)
    return a
scenes=[scene(i/FPS) for i in range(300)]
FF=imageio_ffmpeg.get_ffmpeg_exe();out=P/'visuals/aurora-meadow-loop.mp4'
cmd=[FF,'-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-an','-c:v','h264_nvenc','-preset','p5','-tune','lossless','-rc','constqp','-qp','0','-pix_fmt','yuv420p',str(out)]
proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for n in range(900):
    a=draw(scenes[n%300],n/FPS);proc.stdin.write(a.tobytes())
    if n in [0,150,300,450,600,750]:Image.fromarray(a).save(P/f'visuals/flight-{n//FPS:02}.jpg',quality=95)
proc.stdin.close();assert proc.wait()==0
endpoint=int(np.abs(draw(scene(0),0).astype(int)-draw(scene(30),30).astype(int)).max());assert endpoint==0
displacements=[float(np.linalg.norm(np.array(pos(p,5))-pos(p,0))) for p in paths]
report=dict(duration=D,fps=FPS,frames=900,resolution='1920x1080',cycle_endpoint_max_difference=endpoint,firefly_count=len(paths),large_fireflies=12,flight_displacement_5s_px=displacements,paths=paths,method='Clean meadow plate reconstructed with built-in image generation; no baked-in large fireflies. All 12 large and 18 small lights animate independently after grass and aurora motion.',bytes=out.stat().st_size)
report.update(bright_star_count=len(stars),bright_stars=stars,twinkle_cycle_seconds=10,star_detail_amplitude=.40,grass_breeze_cycle_seconds=10,grass_peak_horizontal_px_approx=8,grass_roots_anchored=True)
(P/'visuals/loop-verification.json').write_text(json.dumps(report,indent=2))
print('Background complete: all 30 fireflies move independently.',flush=True)
