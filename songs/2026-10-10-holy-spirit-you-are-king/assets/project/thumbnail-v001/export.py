from pathlib import Path
from PIL import Image
import json,hashlib
P=Path(__file__).resolve().parent
S=P.parents[2]
out=S/'assets/artwork/thumbnails/holy-spirit-you-are-king-youtube-thumbnail-v001.jpg'
im=Image.open(P/'generated-source.png').convert('RGB').resize((1920,1080),Image.Resampling.LANCZOS)
im.save(out,quality=94,optimize=True)
for w in [320,390,640]:
    im.resize((w,round(w*9/16)),Image.Resampling.LANCZOS).save(P/f'preview-{w}.jpg',quality=94)
assert out.stat().st_size<2*1024*1024
record=dict(output=str(out.relative_to(S)),size=[1920,1080],bytes=out.stat().st_size,sha256=hashlib.sha256(out.read_bytes()).hexdigest(),source='generated-source.png',tool='built-in image_gen',video_revision='v011',video_approved='2026-10-12',thumbnail_approval='pending',preview_widths=[320,390,640])
(P/'verification.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
