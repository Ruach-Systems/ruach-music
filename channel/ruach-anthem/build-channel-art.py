from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import shutil,math
P=Path(__file__).resolve().parent
B=Path(r'D:/WORK/MY APPS/My Business/ruach-brand-guide')
for n in ['ruach-app-crimson-1024.png','ruach-lockup-white-2048.png']:
 shutil.copyfile(B/'assets'/n,P/n)
shutil.copyfile(B/'fonts/Manrope-600.ttf',P/'Manrope-600.ttf')
shutil.copyfile(B/'fonts/Manrope-OFL.txt',P/'Manrope-OFL.txt')
im=Image.new('RGB',(2560,1440),'#141821');d=ImageDraw.Draw(im)
# Quiet flowing lines suggest breath and musical resonance beyond the mobile crop.
for side in [-1,1]:
 for k in range(16):
  pts=[]
  for x in range(0,2561,5):
   y=720+side*(245+k*24)+65*math.sin(x/550+k*.11)
   pts.append((x,y))
  d.line(pts,fill=(53+int(k*1.5),27,40),width=2)
font=lambda size:ImageFont.truetype(str(P/'Manrope-600.ttf'),size)
logo=Image.open(P/'ruach-lockup-white-2048.png').convert('RGBA');logo.thumbnail((550,130))
anthem='Anthem';f=font(112);aw=d.textlength(anthem,font=f);total=logo.width+44+aw;x=int((2560-total)/2)
im.paste(logo,(x,646),logo);d.text((x+logo.width+44,616),anthem,font=f,fill='#F7F3ED')
d.text((1280,562),'SONGS OF THE KINGDOM',font=font(30),fill='#EF5967',anchor='mt')
d.rectangle((1216,791,1344,794),fill='#B21F32')
d.text((1280,827),'Governed by the Spirit.',font=font(35),fill='#E8E3DA',anchor='mt')
im.save(P/'ruach-anthem-youtube-banner-v001.png')
shutil.copyfile(P/'ruach-app-crimson-1024.png',P/'ruach-anthem-profile-v001.png')
icon=Image.open(P/'ruach-app-crimson-1024.png');icon.resize((150,150),Image.Resampling.LANCZOS).save(P/'ruach-anthem-watermark-v001.png')
im.crop((507,509,2053,932)).save(P/'banner-mobile-safe-preview.png')
