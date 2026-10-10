"""Create versioned Anthem-artwork derivatives without re-encoding audio."""
from pathlib import Path
import hashlib, json, shutil, subprocess
from mutagen.id3 import ID3, APIC
import imageio_ffmpeg

SONG = Path(__file__).resolve().parents[2]
REPO = SONG.parents[1]
ART = REPO / 'channel/ruach-anthem/identity-approved-v001/ruach-anthem-avatar.png'
FF = imageio_ffmpeg.get_ffmpeg_exe()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def audio_hash(path):
    return subprocess.check_output([FF, '-v', 'error', '-i', str(path), '-map', '0:a:0',
        '-c:a', 'copy', '-f', 'hash', '-hash', 'sha256', '-']).decode().strip()

def update(source, destination):
    if destination.exists():
        raise FileExistsError(destination)
    before = audio_hash(source)
    original_tags = ID3(source)
    other_tags = {key: value.pprint() for key, value in original_tags.items() if not key.startswith('APIC:')}
    shutil.copy2(source, destination)
    tags = ID3(destination)
    tags.delall('APIC')
    tags.add(APIC(encoding=3, mime='image/png', type=3, desc='RUACH Anthem front cover', data=ART.read_bytes()))
    tags.save(destination, v2_version=3)
    readback = ID3(destination)
    assert {key: value.pprint() for key, value in readback.items() if not key.startswith('APIC:')} == other_tags
    assert len(readback.getall('APIC')) == 1 and readback.getall('APIC')[0].data == ART.read_bytes()
    assert audio_hash(destination) == before
    return {'source': str(source.relative_to(SONG)), 'file': str(destination.relative_to(SONG)),
        'source_sha256': sha(source), 'sha256': sha(destination), 'audio_stream_hash': before,
        'audio_stream_unchanged': True, 'other_tags_unchanged': True, 'artwork_readback_verified': True}

if __name__ == '__main__':
    pairs = []
    for version in ('v1', 'v2-slow'):
        source = SONG / f'assets/audio/branded/ruach-your-will-in-my-heart-{version}-branded-v001.mp3'
        pairs.append((source, source.with_name(source.name.replace('v001.mp3', 'v002.mp3'))))
    source = SONG / 'assets/audio/releases/your-will-in-my-heart-by-ruach.mp3'
    pairs.append((source, source.with_name('your-will-in-my-heart-by-ruach-v002.mp3')))
    records = [update(source, output) for source, output in pairs]
    report = {'date': '2026-10-10', 'branding': 'RUACH Anthem approved artwork; ID3v2.3',
        'artwork_source': str(ART.relative_to(REPO)), 'artwork_sha256': sha(ART),
        'files': records, 'hosted_download_updated': False,
        'note': 'Historical MP3s and published video retained; this updates versioned local derivatives only.'}
    (SONG / 'metadata/audio-artwork-update-v002.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
