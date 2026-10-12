# RUACH lyric-video standard

Approved by the user on 2026-10-10 (Asia/Singapore). This is the standard for future lyric videos. It supersedes the earlier style proposal and its 4K recommendation.

## Delivery and visual reference

Deliver at **1920 x 1080 (1080p), 16:9, 30 fps**, with crisp typography and high-quality H.264/AAC encoding. Do not produce 4K deliveries under this standard. Preserve existing exports as historical revisions.

Use [Your Will in My Heart revision 005](../songs/2026-10-10-your-will-in-my-heart/assets/project/lyric-video-v005/README.md) as the approved layout reference, adapted to 1080p. Its existing 4K export is a historical asset, not the resolution template.

## Consistent layout and RUACH identity

Updated user direction, 2026-10-10: use the **main RUACH branding** for lyric-video overlays, returning to the established white parent RUACH lockup. The source is channel/ruach-anthem/ruach-lockup-white-2048.png. Preserve approved historical exports and keep the channel identity kit available for channel-specific uses.

Keep title, lyric and preview positions consistent with the reference. Retain Manrope, the tagline **Governed by the Spirit.**, and the main logo's exact proportions. Choose accent colors to fit each song's background; Crimson is optional. Use a restrained, harmonious rule such as warm champagne for golden scenes. Maintain strong lyric contrast. Subtle organic shapes and environmental objects may add depth while leaving the lyric area quiet; select them to fit the music and setting.

Reference geometry on a 1920 x 1080 canvas:

| Element | Placement |
| --- | --- |
| Opening song title | Centered at x=960, y=465 |
| Opening LYRIC VIDEO label | Centered at x=960, y=566 |
| Song title during lyrics | Centered at x=960, y=120 |
| Song-colored title rule | x=914, y=190; 92 x 3 pixels |
| Current lyric | Centered at x=960, y=490 |
| Subtle next-line preview | Centered at x=960, y=615 |
| Governed by the Spirit. tagline | Centered at x=330, y=983 |
| Main RUACH logo | Fit proportionally within the existing 230-pixel-wide branding area; 100 pixels from right, 70 from bottom; verify legibility and clear space |

Retain the reference's hierarchy, safe margins, and gentle transitions. Fit long titles or lines within the safe area without moving the established layout. Synchronize the small title and its rule so no orphan rule appears during the opening. Keep take/version/speed labels out of the visible title.

Current lyrics use a single steady ivory color. Keep the next lyric line smaller and subdued below them, and omit previews across instrumental breaks. **No word highlighting, colored word boxes, karaoke effects, or completed/upcoming word color changes.**

## Mobile readability

Standing requirement added by the user on 2026-10-10: all future lyric videos must be comfortably readable on mobile.

- At 1920x1080, start with **100 px Manrope 600 for the current lyric**; use **96 px as the minimum**. Keep a steady ivory color with strong contrast against a quiet background.
- Use **56 px for the next-line preview**, with **52 px as the minimum**. Subdue its color without making it disappear.
- Keep the established centers at (960,490) and (960,615), and at least 120 px of left/right safe space. Break long text into complete musical phrases with accurate timing, or at most two balanced lines, instead of reducing the font below the minimum. Two-line layouts must leave clear separation from the preview.
- Use at least 44 px for the persistent song title and 80 px for the opening title. Preserve the approved logo proportions and established branding placement.
- Export representative frames at **390x219** and **640x360** for review at actual image size, including the longest lyric and the Father/Son/King declaration when present. Check legibility, clipping, contrast, and separation from the preview. Save these checks with the project.
- These are production defaults and visual checks, not a claim of testing on a physical phone. Record any actual device review separately.

## Custom motion background for every song

Create a motion background specifically for each song's vibe and message. Read its lyrics and creative brief, identify the central message, emotional tone, musical energy, and appropriate visual motifs, then record how the background expresses them. For biblical material, follow the Kingdom perspective in AGENTS.md.

Each song must have a noticeably distinct visual identity that subscribers can recognize at preview size. Vary meaningful features such as setting, composition, dominant background colors, lighting, motifs, and movement. A minor tint change or reuse of the same generic loop is insufficient. Match the song first; do not use unrelated scenery simply to look different.

The RUACH overlay stays consistent while the background changes. Keep the lyric area readable and motion appropriate to the song. Repeating backgrounds should loop seamlessly without obvious resets. Compare a representative frame with other songs in the catalog at small preview size before approval.

Record the concept, song-message rationale, differences from other songs, prompts, source files, provenance, and motion settings in the song folder.

Decorative motion must belong to the song's visual setting. For natural country scenes, prefer organic wind/haze ribbons, seed or leaf silhouettes, field glints and other restrained environmental details. Avoid detached geometric outlines or arbitrary sky overlays unless the song's concept specifically calls for them. This refinement was requested on 2026-10-10.

## Timing and review

Derive phrase timing from the actual selected recording and retain sustained vocal endings. Keep complete lyric lines visible without word-by-word activation. Save editable timing cues and subtitles. Check opening, lyric transitions, instrumental breaks, and ending; verify resolution, legibility, decoding, and audio alignment. Distinguish automated checks, visual review, and listening review.

Record the user's lyric-video approval with the exact revision and date. Video approval does not imply audio-master or thumbnail approval. The user has separately authorized approved-song uploads to RUACH Anthem; follow the [YouTube release standard](YOUTUBE-RELEASE-STANDARD.md) and respect the recorded approval scope.

## Static YouTube thumbnail after video approval

Once the user approves a lyric video, create a matching **static YouTube thumbnail image** as the next production deliverable. This does not mean a short teaser video. Use the approved song-specific visual identity, recognizable RUACH branding, and a legible song title. Adapt the composition for thumbnail readability rather than blindly shrinking the full lyric-video layout. Verify the result at small preview size.

Save the thumbnail export, editable source, prompts, source artwork, and provenance in that song's folder; use `assets/artwork/thumbnails/` for exports and `assets/project/` for editable source. Record the video approval that triggered thumbnail creation, the thumbnail's revision, actual file link, and review status. Do not claim a thumbnail exists until it is created. Continue approved songs through the authorized YouTube upload workflow.

## Song package

Keep versioned video exports, custom background sources, rendering project, fonts/licenses, lyric cues, subtitles, visual briefs/prompts, thumbnails, metadata, and validation evidence inside the song's permanent folder. Preserve earlier revisions. Update the catalog, song README, and changelog when deliverables or approvals change.

## Post-publication cleanup and push

Standing user instruction, 2026-10-12 (Asia/Singapore): after the approved upload is verified on YouTube, delete non-reusable assets, including the uploaded delivery MP4, and remove unapproved outputs and files. Preserve reusable motion backgrounds and branding, including their source files, dependencies and licenses. Keep approved audio masters, the approved thumbnail, lyrics, and compact approval/release/provenance records as the release archive. Remove redundant copies, temporary renders and superseded experiments; do not delete a source still required by retained reusable work.

Before deletion, inventory exact song-scoped paths and sizes, confirm the uploaded video ID and approval, and record a cleanup manifest. Replace local export links with the published YouTube link and record intentional removals. Do not treat reusable background MP4 loops as disposable delivery MP4s. This instruction supersedes earlier requirements to retain every video export or unapproved revision after publication. Never remove hosted YouTube videos or GitHub Release downloads as part of local cleanup.

After cleanup, update the catalog, song README, changelog and metadata. Commit and push the approved song package and related approved standards to the configured repository remote; this is standing authorization for that scoped step. Review the staged diff and assets, exclude unrelated or unapproved work, and verify the remote commit. Do not rewrite Git history or force-push. If cleanup or push is blocked, record the actual result and report the remaining work rather than claiming completion.
