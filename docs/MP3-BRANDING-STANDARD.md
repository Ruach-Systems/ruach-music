# MP3 metadata branding standard

Approved 2026-10-10. Apply to every future branded song and downloadable MP3.

- Use ID3v2.3 tags. Artist and album artist remain **RUACH**; channel identity is **RUACH Anthem**.
- Set the clean song title, actual album or collection, release year, appropriate genre, and track number when known. Do not invent production facts. Public titles omit take/version/speed labels unless requested; retain take identity in filenames and metadata records.
- Add a RUACH Anthem brand comment and full written lyrics, matching the selected recording. Unsynchronized lyrics are not timing cues.
- Embed the approved RUACH Anthem artwork as the front cover (APIC type 3, image/png). Default source: `channel/ruach-anthem/identity-approved-v001/ruach-anthem-avatar.png`. Song-specific artwork must retain this approved identity. Do not substitute the parent two-ribbon logo.
- Preserve encoder provenance and original recordings. Create versioned branded derivatives; avoid re-encoding MP3 audio for tag changes.
- Verify the compressed audio-stream SHA-256 before and after tagging, reread the tags and embedded artwork, and record source/output/artwork hashes and exact asset paths in the song metadata.
- Metadata branding is not an audible watermark, cryptographic signature, or proof of ownership. No audible watermark is added unless explicitly requested.
- Video rendering converts the MP3 audio to the export codec; cover art and lyrics in MP3 tags do not automatically become video overlays. Apply video branding separately.
- Record local updates separately from hosted download updates. Preserve old release records and never claim the public download changed without verifying the hosted asset.
