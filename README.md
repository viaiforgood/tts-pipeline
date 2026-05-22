# tts-pipeline

Text-to-speech pipeline for generating narrated audio, mixing background music, and rendering audio/video assets for publishing.

## Project Status

`tts-pipeline` is a pre-alpha public scaffold. Today, only packaging and placeholder CLI help are available. Media generation commands are intentionally visible as the planned public interface, but they are not implemented yet.

This repo is being built toward one minimum successful workflow:

```text
one .txt file -> narrated audio -> optional background music -> one MP4 video
```

Longer-term, `tts-pipeline` will support repeatable text-to-media workflows:

```text
text -> TTS audio -> optional background music -> MP4 video -> captions and metadata
```

The project is designed for nonprofit, educational, public-interest, and publishing workflows, such as turning an article into a narrated video, producing accessibility audio, or preparing public service messages for video platforms.

## Roadmap

MVP:
- Text-to-audio generation with native TTS provider support.
- Background music mixing with configurable track, volume, intro, tail, and fade behavior.
- Audio-to-video rendering with FFmpeg and a default static background image.
- Direct text-to-video flow that chains the steps above.

Next:
- Voice presets and voice rotation for multi-section narration.
- Pronunciation correction with glossary-backed rules.
- Batch processing for text, audio, sidecar transcripts, and generated media.

Later:
- RAG-style pronunciation lookup for larger correction sets.
- YouTube-ready metadata, captions, and publishing assets.

## CLI Usage

`tts-pipeline` exposes a Python CLI command. The following subcommands are available:

- `text-to-audio` (planned)
- `mix-background-music` / `mix-bgm` (planned)
- `audio-to-video` (implemented): Render an audio file or directory of audio files as an MP4 video.
- `text-to-video` (planned)

### audio-to-video Command

The `audio-to-video` command renders audio (e.g. `.m4a` or `.mp3`) to a `.mp4` video with a static background image:

```bash
# Render a single file
tts-pipeline audio-to-video -a path/to/audio.m4a -i path/to/background.jpg -o path/to/output.mp4

# Batch convert a folder of audio files
tts-pipeline audio-to-video -a path/to/audio_dir -o path/to/output_dir
```

#### Arguments
- `-a`, `--audio`: Input audio file OR directory for batch mode (required).
- `-i`, `--image`: Custom background image (defaults to `assets/background/background.jpg` or `assets/background/background.png`).
- `-o`, `--output`: Output MP4 path or output directory for batch mode (defaults to replacing audio file extension with `.mp4`).
- `-r`, `--resolution`: Output video resolution (default: `1920x1080`).
- `--bitrate`: Audio bitrate (default: `192k`).
- `--no-meta`: Skip embedding default metadata.


## Repository Layout

```text
assets/
  background/          Default video background image location
  bgm/                 Optional background music tracks
data/
  pronunciation/       Pronunciation glossary and correction rules
src/
  tts_pipeline/        Python package
tests/                 Automated tests
```

## Default Background

The default video background convention is:

```text
assets/background/background.jpg
```

The scaffold only tracks the directory placeholder. Add your own `background.jpg` before using video rendering once it is implemented. Recommended source images are 1920x1080 JPG or PNG files.

## Pronunciation Glossary

The example glossary lives at:

```text
data/pronunciation/glossary.example.json
```

The initial implementation will treat rules as ordered literal replacements unless a future schema explicitly marks a rule as regex, provider-specific, or locale-specific. This keeps pronunciation fixes deterministic and testable.

## Development

Requirements:

- Python 3.11+
- FFmpeg

Verify prerequisites:

```bash
python --version
ffmpeg -version
```

Install in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run the placeholder CLI:

```bash
tts-pipeline --help
```

Run checks:

```bash
ruff check .
pytest
```

## Troubleshooting

- `tts-pipeline <command>` says the command is not implemented: expected for planned commands in this pre-alpha scaffold.
- `ffmpeg: command not found`: install FFmpeg before using video rendering commands.
- `assets/background/background.jpg` or `background.png` is missing: add your own background image in `assets/background/` or specify one using `--image`.
- TTS provider credentials are missing: provider setup will be documented when the first provider lands.

When opening an issue, include your OS, Python version, command, full error output, and whether you installed with `pip install -e ".[dev]"`.

## Data And Privacy

Future TTS and publishing providers may send input text, audio, metadata, or generated media to third-party APIs. Provider-specific commands should document what data leaves your machine before they are marked production-ready. Do not commit secrets, API keys, private transcripts, or generated private media.

## Contributing

Contributions are welcome while the project is pre-alpha. See [CONTRIBUTING.md](CONTRIBUTING.md) for local setup, testing, and review expectations.

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).
