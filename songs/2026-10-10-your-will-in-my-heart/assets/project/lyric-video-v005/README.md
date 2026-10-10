# Lyric video revision 005 - 4K

User direction: remove text highlighting, retain the subtle next-line preview, and improve resolution.

All current lyrics use one steady ivory color. There are no active-word backgrounds, word color changes, or karaoke effects. The next line remains smaller and muted below the current line. Phrase timings are preserved from revision 004.

Export: 3840 x 2160, 30 fps, H.264/AAC. Text is rendered at output resolution; the 1024-pixel-wide approved RUACH logo is rendered at 460 pixels. The existing 1920 x 1080 background is upscaled using Lanczos and restrained sharpening. This does not make the background native 4K or recover missing source detail. A prepared 4K loop avoids repeated processing of the same frames. High-quality NVIDIA encoding uses CQ 14 for the background and CQ 17 for the delivery.

The original branded MP3 remains the audio source. Superseded revisions 001–004 were removed at the user's cleanup request on 2026-10-10. The approved v005 MP4 remains local and is excluded from Git at the user's request; this project preserves its reproducible sources.

Reproduce with `prepare-background.py`, `render.py`, and `verify.py`. The saved prepared loop can be reused directly. Python dependencies: imageio-ffmpeg, Pillow, mutagen, av, numpy. Rendering uses NVIDIA NVENC; on machines without it, substitute an available H.264 encoder with equivalent quality settings.

See verification.json for actual export measurements and checks. Full listening approval remains pending.
