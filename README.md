# Medhavy YouTube Production Library

This repository contains non-MP3, non-MP4 production materials for Medhavy science videos. It preserves beat sheets, scripts, editorial notes, visual assets, manifests, rendered stills, and quality-control artifacts needed to inspect or rebuild projects.

## Organization

Every beat-sheet project lives directly below one of five subject buckets:

```text
<subject>/<video-project>/
```

There are no intermediate book, course, `youtube`, or source-workspace layers. Source context is added to a project name only when required to prevent a collision.

| Subject directory | Projects | Beat-sheet files |
|---|---:|---:|
| `anthropics/` | 2 | 2 |
| `biology/` | 12 | 17 |
| `cancer-biology/` | 457 | 841 |
| `physics/` | 98 | 135 |
| `quantun-physics/` | 615 | 962 |
| **Total** | **1,184** | **1,957** |

`quantun-physics` is the repository's current directory name and is retained for path compatibility.

## Scope

- `anthropics/` contains the small Medhavy collection explicitly associated with Anthropic.
- `biology/` contains general life-science projects.
- `cancer-biology/` contains cancer biology, cancer medicine, cancer research, therapeutics, and nanomedicine projects.
- `physics/` contains non-quantum physics projects.
- `quantun-physics/` contains quantum mechanics and quantum-focused projects.

General courses and educational collections that are not specifically part of Medhavy belong in the Humanitarians YouTube repository. Independent music and Claude-specific creative projects belong in Musinique.

## Typical project contents

A project may contain:

- `beat_sheet.json` and alternate beat-sheet variants
- `FACTCHECK.md`, `PEDAGOGY.md`, `PROMPTS.md`, `SHOTLIST.md`, and source notes
- Python or JavaScript scene and rendering code
- clip manifests, timing metadata, and concatenation instructions
- images, SVGs, diagrams, typography, and other assets under `media/`
- QC frames, overview sheets, layout audits, and status reports

Some projects are complete builds; others are source packages, alternates, or retained quality-control snapshots.

## Finding projects

```bash
# Show the five subject buckets
find . -mindepth 1 -maxdepth 1 -type d ! -name .git | sort

# Find projects by folder-name fragment
find . -mindepth 2 -maxdepth 2 -type d -iname '*tunneling*'

# List primary beat sheets
find . -mindepth 3 -maxdepth 3 -name 'beat_sheet.json'

# Search production text
rg -i 'photosynthesis|wavefunction|immunotherapy'

# Find editorial and verification documents
find . -type f \( -name 'FACTCHECK.md' -o -name 'PEDAGOGY.md' \)
```

## Adding a project

1. Choose the single best-fit subject bucket.
2. Put the complete project at `<subject>/<video-project>/`.
3. If the name already exists, add concise source context rather than overwriting it.
4. Do not recreate book, course, source-workspace, or `youtube` layers.
5. Keep final MP3 and MP4 renders outside this repository.

The reusable organizer is `SCRIPTS/flatten_medhavy_youtube.py` in the Bear Textbooks repository.

## Media policy

The root `.gitignore` excludes `*.mp3` and `*.mp4`. Timing JSON or text files inside a directory named `mp3/` may remain because they are metadata rather than audio. Supporting PNG, JPEG, SVG, M4A, Markdown, JSON, HTML, and source-code files may be retained when needed for reconstruction or inspection.

## Repository scope

This repository mirrors `books/medhavy/youtube`. It is a production-material archive, not the public Medhavy website or storage for finished distribution media.
