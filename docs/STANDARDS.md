# Organization and production standards

## Folder layout

```text
songs/YYYY-MM-DD-song-slug/
  README.md                 brief, status, chosen take, outstanding work
  CHANGELOG.md              dated production history
  lyrics/lyrics-v001.txt     clean lyrics with optional section cues
  prompts/style-v001.txt     exact submitted musical direction
  prompts/generation-v001.md actual settings and generation notes
  metadata/links.md          platform and reference URLs
  metadata/generations.json  structured take records
  assets/audio/             original audio and versioned mixes
  assets/stems/             separated instrument and vocal files
  assets/artwork/           covers, source artwork, export variants
  assets/artwork/thumbnails/ static YouTube thumbnail exports
  assets/video/             lyric videos and visualizers
  assets/project/           editable production projects
  assets/evidence/          screenshots and verification evidence
```

Create asset subfolders only when needed. Keep all alternative takes of one song together. Keep the folder's creation date stable if the title later changes; record aliases in the README.

## Naming and revisions

- Use lowercase ASCII kebab-case folder/file names and ISO dates (`YYYY-MM-DD`). Use Asia/Singapore for production log dates unless a source explicitly uses another timezone.
- Number lyrical and prompt revisions `v001`, `v002`, etc. Retain revisions used for a generation.
- Name audio by song, take, and revision: `your-will-in-my-heart-take-01-original.mp3`, `your-will-in-my-heart-take-01-mix-v002.wav`.
- Keep provider IDs in metadata rather than relying on filenames to identify a generation.
- Never label an unreviewed generation `final`, `approved`, or `master`. Approval must be recorded with date and scope.

## Creative brief

Record the purpose, language, lyrical focus, musical feel, vocal direction, instrumentation, target duration, references, and exclusions. Kingdom perspective in AGENTS.md applies to biblical music and visuals. A reference describes a creative target; document whether it was actually heard and what qualities were identified.

## Lyric videos and YouTube thumbnails

Latest video direction (2026-10-10): use the main RUACH white lockup for lyric-video overlays and colors suited to the individual scene. Record the exact source and preserve prior versions. Refer to the lyric-video standard for the current branding override; the RUACH Anthem channel identity kit remains available for channel-specific work.
Follow the approved [RUACH lyric-video standard](LYRIC-VIDEO-STANDARD.md). Deliver 1080p only with the consistent RUACH layout, plain lyrics, and subtle next-line preview. Create a unique motion background that expresses the particular song's vibe and message and is distinguishable from other songs at preview size.

Record the exact video revision and user approval date. Once approved, create a matching static YouTube thumbnail and save its export and editable assets in the song folder. Track thumbnail review separately. Follow the [YouTube release standard](YOUTUBE-RELEASE-STANDARD.md) to upload approved songs to RUACH Anthem under the user's standing authorization, with full lyrics in the description and the title `[SONG TITLE] by RUACH`. Use the visual-production fields in the song template to retain the concept, provenance, approvals, and deliverable links.

Mobile lyric readability is mandatory: follow the font-size minimums and save 390px/640px preview checks specified in the lyric-video standard. Keep complete phrases readable without shrinking long lines.

## Prompts and platform records

Store exact submitted text. Separate requested tempo/duration/instruments from actual controls and output observations. For each take record provider, model, generation date, URL, displayed duration, lyrics/prompt revisions, local file paths, review state, and release state. Use `null` for unknown values and explain meaningful gaps. Never fabricate credit costs or settings.

Platform controls, entitlements, prices, and licensing change. Verify them during the relevant workflow; this document intentionally avoids fixed plan claims. Record plan/license evidence when preparing a release. Do not assume generation, downloading, commercial permission, or copyright eligibility are interchangeable.

## Review stages

`draft` → `generated` → `listening-reviewed` → `approved` → `released`

Downloading is a separate asset state. Review complete audio for missing/extra lyrics, pronunciation, phrasing, clipped endings, unwanted sounds, and the intended mood. Check authority, loving obedience, and other brief requirements in both words and delivery. Inspect visuals independently. Keep notes on each take; a displayed duration alone is not a listening review.

Before release, record the approved take/mix, artwork, credits, relevant permissions, intended destination, user authorization, export format, and release link after publication. Do not publish just to obtain a link.

## Asset handling and Git

- Apply the [MP3 metadata branding standard](MP3-BRANDING-STANDARD.md) to every future song and release copy, using the approved RUACH Anthem artwork and verified unchanged audio.
- Preserve original downloads and provenance. Keep edited exports separate from source assets.
- Store associated assets in the song folder. For assets intentionally stored externally, include a durable URL/path and the reason in metadata; do not claim they are in the repository.
- Use UTF-8 text and relative paths within packages. Do not store credentials or private account data.
- Keep caches and temporary renders out of Git. Review large binaries before a future push and configure Git LFS with the remote's limits in mind; do not silently omit assets.
- Repository creation does not authorize a remote, commit, or push.

## Completion check

Confirm catalog and local links resolve; metadata is valid JSON; recorded local files exist; exact input revisions are saved; generated takes have URLs; missing assets and review gaps are explicit. Review Git status and diff before reporting completion.

## Post-publication cleanup and push

Standing user instruction, 2026-10-12 (Asia/Singapore): after the approved upload is verified on YouTube, delete non-reusable assets, including the uploaded delivery MP4, and remove unapproved outputs and files. Preserve reusable motion backgrounds and branding, including their source files, dependencies and licenses. Keep approved audio masters, the approved thumbnail, lyrics, and compact approval/release/provenance records as the release archive. Remove redundant copies, temporary renders and superseded experiments; do not delete a source still required by retained reusable work.

Before deletion, inventory exact song-scoped paths and sizes, confirm the uploaded video ID and approval, and record a cleanup manifest. Replace local export links with the published YouTube link and record intentional removals. Do not treat reusable background MP4 loops as disposable delivery MP4s. This instruction supersedes earlier requirements to retain every video export or unapproved revision after publication. Never remove hosted YouTube videos or GitHub Release downloads as part of local cleanup.

After cleanup, update the catalog, song README, changelog and metadata. Commit and push the approved song package and related approved standards to the configured repository remote; this is standing authorization for that scoped step. Review the staged diff and assets, exclude unrelated or unapproved work, and verify the remote commit. Do not rewrite Git history or force-push. If cleanup or push is blocked, record the actual result and report the remaining work rather than claiming completion.
