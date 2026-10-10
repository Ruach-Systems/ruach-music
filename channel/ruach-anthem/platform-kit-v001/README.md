# RUACH Anthem platform assets v001

Prepared 2026-10-10 from the approved **Breath into Song** identity. Local asset pack only; no account artwork changed.

## Choose your file

| Platform/use | File | Export size |
| --- | --- | --- |
| YouTube profile | youtube/profile-800.png | 800 x 800 |
| YouTube banner | youtube/banner-2560x1440.png | 2560 x 1440 |
| YouTube watermark | youtube/watermark-150.png | 150 x 150 |
| Instagram profile | instagram/profile-1080.png | 1080 x 1080 |
| Facebook profile | facebook/profile-1080.png | 1080 x 1080 |
| Facebook cover | facebook/cover-1640x624.png | 1640 x 624 |
| TikTok profile | tiktok/profile-1080.png | 1080 x 1080 |
| Spotify artist avatar | spotify/profile-1024.png | 1024 x 1024 |
| Light backgrounds | general/logo-light-background-transparent.png | Original transparent PNG |
| Dark backgrounds | general/logo-dark-background.png | White logo on opaque dark background |

Profile exports deliberately share the same approved symbol. Sizes are delivery choices, not claims of mandatory platform dimensions. Use the platform crop preview before saving. The Spotify avatar has no text. This kit does not include album-cover artwork, which should be song-specific.

## Design and sources

The symbol and primary light-background logo come from `../identity-approved-v001/`. The banner source was made using the built-in image-generation tool from the approved concept board; its prompt is retained in `prompts.txt`. The platform exports are mechanically resized/cropped from these sources, without independently regenerating each profile logo. `export-assets.py` reproduces exports and `asset-inventory.json` records actual sizes and file weights.

These are raster PNG/JPEG assets, not vector masters. Resizing the source banner to its delivery size does not create native detail. The transparent primary logo retains the previously finalized raster's contours. The reverse transparent generation was rejected for visible artifacts and is not included; the dark version is intentionally opaque.

## Crop and technical checks

- All exports decoded successfully and their dimensions are recorded in the inventory.
- `previews/youtube-mobile-safe-area.png` shows the central 1546 x 423 portion of the 2560 x 1440 banner.
- `previews/circular-avatar.png` shows circular clipping of the square avatar.
- `previews/platform-overview.jpg` provides a quick comparison. Preview files are not intended for upload.
- Logo spelling, symbol continuity, margins, and central crop were reviewed locally. Account-specific rendering has not been tested live.

## Platform references

Checked 2026-10-10:

- [YouTube banner and profile guidance](https://support.google.com/youtube/answer/12950272?hl=en): recommends 2560 x 1440 banners and square or round profile art.
- [Spotify artist image guidance](https://support.spotify.com/dj-en/artists/article/artist-image-guidelines/): avatar minimum 750 x 750, maximum 20 MB; avoid text and busy backgrounds.

Keep the parent RUACH two-ribbon logo separate from this channel identity. Preserve earlier exports and version any future revisions.
