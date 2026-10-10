from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import json, shutil

ROOT = Path(__file__).resolve().parent
IDENTITY = ROOT.parent / 'identity-approved-v001'
avatar = Image.open(IDENTITY / 'ruach-anthem-avatar.png').convert('RGB')
banner = Image.open(ROOT / 'sources/banner-generated.png').convert('RGB')
primary = Image.open(IDENTITY / 'ruach-anthem-primary-transparent.png').convert('RGBA')
records = []

def save(im, name, use):
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    im.save(p, optimize=True)
    records.append(dict(file=name, width=im.width, height=im.height, mode=im.mode, bytes=p.stat().st_size, use=use))

for name, size in [('youtube',800), ('instagram',1080), ('facebook',1080), ('tiktok',1080), ('spotify',1024)]:
    save(avatar.resize((size,size), Image.Resampling.LANCZOS), f'{name}/profile-{size}.png', 'Profile avatar; centered symbol, no text')

save(banner.resize((2560,1440),Image.Resampling.LANCZOS),'youtube/banner-2560x1440.png','Channel banner')
save(avatar.resize((150,150),Image.Resampling.LANCZOS),'youtube/watermark-150.png','Video watermark')
# Center crop retains the lockup while adapting the artwork to a wide cover.
save(ImageOps.fit(banner,(1640,624),Image.Resampling.LANCZOS,centering=(.5,.5)), 'facebook/cover-1640x624.png','Cover artwork; check platform crop preview')
save(primary,'general/logo-light-background-transparent.png','Dark wordmark for light backgrounds; RGBA')
save(banner.crop((460,310,1220,620)), 'general/logo-dark-background.png','White lockup on opaque dark background')

# Small previews for crop and readability review; not upload assets.
yt=Image.open(ROOT/'youtube/banner-2560x1440.png')
save(yt.crop((507,509,2053,932)),'previews/youtube-mobile-safe-area.png','Central safe-area proof')
circle=avatar.resize((320,320),Image.Resampling.LANCZOS).convert('RGBA')
mask=Image.new('L',(320,320));ImageDraw.Draw(mask).ellipse((0,0,319,319),fill=255)
circle.putalpha(mask)
save(circle,'previews/circular-avatar.png','Circular crop proof')
board=Image.new('RGB',(1200,800),'#F7F3ED')
d=ImageDraw.Draw(board)
board.paste(Image.open(ROOT/'youtube/banner-2560x1440.png').resize((720,405)),(30,50))
board.paste(avatar.resize((300,300)),(850,50))
board.paste(Image.open(ROOT/'facebook/cover-1640x624.png').resize((720,274)),(30,490))
board.paste(circle,(825,445),circle)
d.text((30,20),'YOUTUBE BANNER',fill='#141821')
d.text((850,20),'PROFILE / SOCIAL',fill='#141821')
d.text((30,465),'FACEBOOK COVER',fill='#141821')
d.text((850,420),'CIRCLE CROP',fill='#141821')
save(board,'previews/platform-overview.jpg','Visual overview')
(ROOT/'asset-inventory.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
for r in records:
    im=Image.open(ROOT/r['file']); im.verify()
print(json.dumps(records,indent=2))
