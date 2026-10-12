from pathlib import Path
import hashlib, json, re, shutil, subprocess
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TPE2, TDRC, TCON, COMM, USLT, APIC
import imageio_ffmpeg

root = Path(__file__).resolve().parents[2]
repo = root.parents[1]
source = Path("C:/Users/Z/Downloads/Holy Spirit, You Are King.mp3")
original = root / "assets/audio/originals/holy-spirit-you-are-king-take-01-original.mp3"
branded = root / "assets/audio/branded/ruach-holy-spirit-you-are-king-take-01-branded-v001.mp3"
art_source = repo / "channel/ruach-anthem/identity-approved-v001/ruach-anthem-avatar.png"
art = root / "assets/artwork/ruach-anthem-avatar-v001.png"
for path in (original, branded, art):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise RuntimeError(f"Preserve existing asset: {path}")
shutil.copy2(source, original)
shutil.copy2(original, branded)
shutil.copy2(art_source, art)
lyrics = "\n".join(line for line in (root / "lyrics/lyrics-v001.txt").read_text(encoding="utf-8-sig").splitlines() if not re.match(r"^\[.*\]$", line)).strip()
tags = ID3(branded)
for key in ("TIT2", "TPE1", "TPE2", "TDRC", "TCON", "APIC", "USLT", "TBPM"):
    tags.delall(key)
tags.add(TIT2(encoding=1, text="Holy Spirit, You Are King"))
tags.add(TPE1(encoding=1, text="RUACH"))
tags.add(TPE2(encoding=1, text="RUACH"))
tags.add(TDRC(encoding=1, text="2026"))
tags.add(TCON(encoding=1, text="Country Gospel"))
tags.add(COMM(encoding=1, lang="eng", desc="RUACH Anthem", text="RUACH Anthem — Governed by the Spirit. Suno AI-generated music; Take 1 selected by user."))
tags.add(USLT(encoding=1, lang="eng", desc="Written lyrics", text=lyrics))
tags.add(APIC(encoding=1, mime="image/png", type=3, desc="RUACH Anthem approved artwork", data=art.read_bytes()))
tags.save(branded, v2_version=3)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def stream_hash(path):
    return subprocess.check_output([imageio_ffmpeg.get_ffmpeg_exe(), "-v", "error", "-i", str(path), "-map", "0:a:0", "-c:a", "copy", "-f", "hash", "-hash", "sha256", "-"], text=True).strip()
before, after = stream_hash(original), stream_hash(branded)
assert sha(source) == sha(original)
assert before == after
check = ID3(branded)
assert check.version == (2, 3, 0)
assert str(check["TIT2"]) == "Holy Spirit, You Are King"
assert str(check["TPE1"]) == str(check["TPE2"]) == "RUACH"
assert check.getall("APIC")[0].data == art.read_bytes()
assert check.getall("USLT")[0].text == lyrics
info = MP3(branded).info
record = dict(date="2026-10-10", brand="RUACH", channel_identity="RUACH Anthem", branding_type="ID3v2.3 metadata and embedded artwork; no audible watermark or cryptographic signature", source_file=str(source), original_file=original.relative_to(root).as_posix(), branded_file=branded.relative_to(root).as_posix(), artwork_file=art.relative_to(root).as_posix(), artwork_source=art_source.relative_to(repo).as_posix(), source_sha256=sha(source), original_sha256=sha(original), branded_sha256=sha(branded), artwork_sha256=sha(art), audio_stream_sha256=after, audio_stream_unchanged=True, duration_seconds=info.length, sample_rate_hz=info.sample_rate, bitrate_bps=info.bitrate, provider_take_id="8b8bba66-1529-434c-ab14-9ac8517ddeb2", take_mapping="User identifies manual download as Take 1", user_selection="User said I like the Take 1; no release-video approval implied", listening_review="No independent assistant listening review", embedded_lyrics="Full written lyrics v001; sung correspondence and timing not independently reviewed", album_and_track="Retained source values if present; no invented album or track number", tool="Mutagen ID3; FFmpeg compressed audio-stream SHA-256")
(root / "metadata/audio-assets-v001.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print(json.dumps(dict(output=str(branded), duration_seconds=info.length, audio_unchanged=before == after, tags_verified=True)))
