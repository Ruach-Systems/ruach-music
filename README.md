# RUACH Music

The home for all music created with the user. Every song has one permanent folder containing its lyrics, prompts, generation records, links, and assets.

## YouTube channel

Channel logo: [approved RUACH Anthem identity — Breath into Song](channel/ruach-anthem/identity-approved-v001/README.md).

[RUACH Anthem — @RuachAnthem](https://www.youtube.com/@RuachAnthem) is the official destination for approved songs. Upload approved songs with their lyric videos and matching static thumbnails. Video titles must use **[SONG TITLE] by RUACH** (for example, **Your Will in My Heart by RUACH**), and descriptions must include the full lyrics.

See the [YouTube release standard](docs/YOUTUBE-RELEASE-STANDARD.md) for the approval-to-upload workflow and [channel assets](channel/ruach-anthem/).

Default releases are **Public**, **Not made for kids**, and include a matching RUACH static thumbnail plus a **free MP3 download link** above the full lyrics in the description. Download files are hosted on this repository's GitHub Releases and are accessible to everyone, including subscribers. Future lyric videos remain 1080p.

## Catalog

| Song | Created | Status | Folder |
| --- | --- | --- | --- |
| Holy Spirit, You Are King | 2026-10-10 | Video v011 and thumbnail v001 approved; [published on YouTube](https://youtu.be/mhlUouC-sFk); free MP3 available | [Song package](songs/2026-10-10-holy-spirit-you-are-king/) |
| Your Will in My Heart | 2026-10-10 | Lyric video v005 explicitly approved; static thumbnail created; published on YouTube; MP3 download available | [Song package](songs/2026-10-10-your-will-in-my-heart/) |

## Start a song

1. Copy `templates/song/` into `songs/YYYY-MM-DD-song-slug/`.
2. Fill in the brief, lyrics, prompts, links, and generation records.
3. Keep all related files inside that song folder, including alternative takes and artwork.
4. Record what was actually generated, downloaded, reviewed, approved, and released.
5. Add the song to this catalog and update its changelog as work progresses.

Read [organization and production standards](docs/STANDARDS.md) and [agent instructions](AGENTS.md) before working here. GitHub repository: [Ruach-Systems/ruach-music](https://github.com/Ruach-Systems/ruach-music). Uploading this archive does not mark any song as an approved master or distributed release.

[Approved lyric-video standard](docs/LYRIC-VIDEO-STANDARD.md) — 1080p only, consistent RUACH layout, custom motion backgrounds matching each song, and a static YouTube thumbnail after video approval.

After verified publication, follow the [post-publication cleanup and push standard](docs/YOUTUBE-RELEASE-STANDARD.md#post-publication-cleanup-and-push): remove disposable uploaded exports and unapproved work, retain reusable backgrounds/branding and the release archive, then commit and push approved changes.
