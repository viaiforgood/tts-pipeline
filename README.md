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

## Planned CLI

The first implementation milestone is a Python CLI with:

- `text-to-audio`
- `mix-background-music` with `mix-bgm` as a short alias
- `audio-to-video`
- `text-to-video`

Current behavior: these commands return a clear “planned but not implemented yet” message.

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

- `tts-pipeline <command>` says the command is not implemented: expected in the current pre-alpha scaffold.
- `ffmpeg: command not found`: install FFmpeg before using future audio/video rendering commands.
- `assets/background/background.jpg` is missing: add your own background image before using future video rendering commands.
- TTS provider credentials are missing: provider setup will be documented when the first provider lands.

When opening an issue, include your OS, Python version, command, full error output, and whether you installed with `pip install -e ".[dev]"`.

## Data And Privacy

Future TTS and publishing providers may send input text, audio, metadata, or generated media to third-party APIs. Provider-specific commands should document what data leaves your machine before they are marked production-ready. Do not commit secrets, API keys, private transcripts, or generated private media.

## Contributing

Contributions are welcome while the project is pre-alpha. See [CONTRIBUTING.md](CONTRIBUTING.md) for local setup, testing, and review expectations.

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).
