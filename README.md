# Medhavy YouTube Production Library

This repository is a structured archive of the non-audio, non-video production materials used to build Medhavy educational videos. It collects reusable source files, scripts, beat sheets, rendered stills, quality-control artifacts, and supporting documentation for projects in physics and biology.

The repository is intended for studying, maintaining, and rebuilding the visual and editorial structure of the videos. Final `.mp3` and `.mp4` files are deliberately excluded.

## Collections

### `physics/`

Physics and physical-science video projects, including quantum mechanics, electromagnetism, astronomy, cosmology, and related topics. The collection contains approximately 36,000 files and more than 1,100 beat-sheet variants.

### `biology/`

Biology, cancer biology, cancer medicine, nanomedicine, genetics, immunology, and related life-science projects. The collection contains approximately 19,600 files and more than 850 beat-sheet variants.

Both collections preserve their source-relative directory structure. For example, a project originally created under a quantum-mechanics textbook remains nested under that textbook's path. This prevents collisions between projects with similar names and preserves provenance.

## Typical project contents

A project directory may contain some or all of the following:

- `beat_sheet.json` and named beat-sheet variants describing narrative beats, timing, and visual intent
- `FACTCHECK.md`, `PEDAGOGY.md`, `PROMPTS.md`, `SHOTLIST.md`, or similar editorial notes
- Python scene or rendering scripts such as `vox_scenes.py`
- `clips/manifest.json`, concatenation lists, and timing metadata
- `media/` assets, generated SVG text, diagrams, and still images
- `_qc/`, `qc-sheet.png`, and layout-audit files used for visual review
- supporting source notes, citations, status files, and build instructions

Not every directory is a self-contained application. Many are production snapshots whose scripts depend on tooling or assets from the larger Bear Textbooks workspace.

## Finding material

Useful searches from the repository root:

```bash
# Find projects by subject or slug
find physics biology -type d -iname '*tunneling*'

# List primary beat sheets
find physics biology -name 'beat_sheet.json'

# Find fact-check and pedagogy notes
find physics biology -type f \( -name 'FACTCHECK.md' -o -name 'PEDAGOGY.md' \)

# Search the production text
rg -i 'photosynthesis|wavefunction|immunotherapy' physics biology
```

## Media policy

The root `.gitignore` excludes:

```gitignore
*.mp3
*.mp4
```

Small metadata files inside directories named `mp3/` may still be present when they are JSON or text. These files describe timing or production state; they are not audio files. Other supporting formats such as PNG, JPEG, SVG, M4A, and source-code files may be included when they are part of the production archive.

## Working with a project

1. Locate the project by subject, title, or slug.
2. Read its beat sheet and any fact-check, pedagogy, source, or status notes.
3. Inspect the clip manifest and media folders to understand the asset sequence.
4. Review QC sheets and layout audits before changing visuals.
5. Treat generated outputs and hand-authored source files differently; check neighboring documentation before regenerating anything.

## Repository scope

This repository mirrors the contents of `books/medhavy/youtube` from the Bear Textbooks workspace. It is an asset and production-material repository, not the public Medhavy website and not a distribution location for finished videos.

