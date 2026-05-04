# Contributing

Thanks for your interest in `tts-pipeline`.

The project is pre-alpha, so the most useful contributions are small, focused changes that clarify the public CLI contract, improve tests, or implement one pipeline step at a time.

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run checks before opening a pull request:

```bash
ruff check .
pytest
```

## Development Guidelines

- Keep CLI behavior deterministic and testable.
- Add or update tests with behavior changes.
- Document whether a feature is implemented, experimental, or planned.
- Do not commit generated private media, transcripts, secrets, API keys, or provider credentials.
- Prefer data-driven pronunciation rules when a correction does not require code.

## Pull Requests

Please include:

- A short summary of the user-facing change.
- Tests or a note explaining why tests are not applicable.
- Any setup, provider, or privacy implications.
