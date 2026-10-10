# YouTube release standard

User instruction recorded on 2026-10-10 (Asia/Singapore).

## Destination and identity

- Channel: **RUACH Anthem**
- Handle: **@RuachAnthem**
- URL: https://www.youtube.com/@RuachAnthem
- Stable channel ID: `UCrEm70zv0iTkSro5cl_pdAg`
- Channel artwork and source assets: [channel/ruach-anthem](../channel/ruach-anthem/)

Use the approved [RUACH Anthem — Breath into Song identity](../channel/ruach-anthem/identity-approved-v001/README.md) for all new videos, lyric videos, visualizers, and matching static thumbnails. Use its musical-note/breath emblem and approved wordmark, rather than the parent RUACH two-ribbon logo. Available exports are in [the platform kit](../channel/ruach-anthem/platform-kit-v001/README.md). Preserve historical releases. The artist credit in video titles remains RUACH.

## Default upload package

Confirmed by the user on 2026-10-10 following the first release:

- Visibility: **Public**; audience: **Not made for kids**.
- Title: **[SONG TITLE] by RUACH**.
- Description: free MP3 download link near the top, a short Kingdom-focused introduction where applicable, full lyrics including repeated sections, RUACH channel link, and accurate production credits.
- Artwork: matching static RUACH thumbnail created after video approval, using the song's distinct visual identity.
- Video: approved lyric video; future deliveries remain **1080p**. The explicitly approved v005 4K release is an existing exception, not a new resolution default.
- Category: **Music**. Set language to the actual song language. Disclose AI use when applicable; for Suno-generated music, select Yes. Record paid promotion and other declarations according to the actual production facts.
- Preserve the approved assets, exact submitted metadata, approval evidence, download/release links, and verification screenshots in the song folder.

These defaults are standing instructions for future approved releases; no repeated generic upload or MP3-hosting permission is needed. A later song-specific instruction takes precedence.

## Approval-to-upload workflow

The user has authorized uploads of approved songs to this channel as a standing production step. Record the approved audio and lyric-video revisions and approval date/scope. Respect any later hold, requested changes, or approval limited to visual design. Do not ask for the same generic upload authorization again.

1. Confirm the approved recording and release video match. Follow the 1080p [lyric-video standard](LYRIC-VIDEO-STANDARD.md).
2. Create the matching static thumbnail after lyric-video approval; retain its source and review status.
3. Prepare and verify the public MP3 download below. Save the exact upload title and description in `metadata/youtube-title.txt` and `metadata/youtube-description.txt`. Put the download link near the top and include full lyrics matching the actual approved recording, preserving repeated sections; omit production instructions and timing tags. Never silently truncate lyrics. If a platform limit prevents the full description, resolve the limitation before upload completion is claimed.
4. Upload to the channel above, preferably through the signed-in in-app browser. Check the channel identity before uploading and use the matching thumbnail.
5. Publish approved releases as Public and select Not made for kids (user clarification on 2026-10-10). This supersedes the initial private-upload default. Respect any later song-specific hold or schedule. Record required platform declarations accurately from the actual production facts.
6. Verify the uploaded title, description, thumbnail, processing state, and visibility. Record the video URL/ID, upload date, selected files, settings, and evidence in the song folder. Avoid duplicate uploads by checking existing release records first.
7. Update the song README, changelog, metadata links, and root catalog. Report uploaded, processing, private, scheduled, and publicly released states accurately.

This documentation update does not itself upload existing songs or change their approval state.

## Title and description

Required title format: **[SONG TITLE] by RUACH**. Replace the placeholder; do not include brackets. Example: **Your Will in My Heart by RUACH**.

Do not append take numbers, speed/version labels, promotional text, or extra suffixes unless the user requests them.

Descriptions must include the full song lyrics. A short song introduction, accurate credits, and relevant links may accompany them. Use the Kingdom perspective from AGENTS.md for biblical material. Scripture quotations, if included, are separate from original lyrics and must identify their translation.

## Free MP3 download

Offer the approved recording as a free MP3 download with every approved YouTube release. Host it as an asset on a versioned GitHub Release in `Ruach-Systems/ruach-music`, following the first release's approach. This link is public and available to everyone, including subscribers; do not describe it as subscriber-gated or dependent on YouTube Premium.

Keep the release copy in `assets/audio/releases/`, named `song-slug-by-ruach.mp3`. Use the clean song title and RUACH artist metadata, with the approved brand artwork. Preserve the original recording and earlier versions. Avoid re-encoding an existing suitable MP3 merely to change tags.

Use a unique versioned release tag such as `song-slug-v001`; check existing releases before creating one to avoid duplicates. Save release notes, the asset URL, source recording, and checksum in song metadata. Verify the asset is uploaded and its link resolves before claiming the download is available. Keep unrelated uncommitted work out of the release operation. Do not upload the lyric-video file as a downloadable release asset unless separately requested.

Put `Download the MP3:` followed by the verified direct asset link near the top of the YouTube description, above the introduction and lyrics. Save the exact final description locally and verify it after publication.

## Per-song release records

- `metadata/youtube-title.txt`: exact submitted title.
- `metadata/youtube-description.txt`: exact submitted description, including lyrics.
- `metadata/links.md`: YouTube URL/ID and visibility/status.
- `metadata/youtube-release-v001.json`: selected files, approval scope/date, upload settings, processing/check status, MP3 asset URL, and checksums; version later release records.
- `assets/audio/releases/`: downloadable MP3 release copies; retain source recording links and release notes in metadata.
- Song README/changelog: approval evidence, selected audio/video/thumbnail revisions, upload date, visibility, schedule if any, and outstanding work.
- `assets/evidence/`: verification screenshots or receipts.

Keep channel-wide artwork in `channel/ruach-anthem/`; keep song-specific release assets in the song folder.
