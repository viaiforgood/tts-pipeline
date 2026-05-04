"""Command line interface for tts-pipeline."""

from __future__ import annotations

import argparse
import sys

from tts_pipeline import __version__


DESCRIPTION = (
    "Text-to-speech pipeline for generating narrated audio, mixing background music, "
    "and rendering audio/video assets for publishing."
)

PLANNED_COMMANDS = {
    "text-to-audio": "Generate narrated audio from text.",
    "mix-background-music": "Mix background music into an audio file.",
    "audio-to-video": "Render an audio file as an MP4 video.",
    "text-to-video": "Generate audio from text and render video.",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tts-pipeline",
        description=DESCRIPTION,
        epilog=(
            "Project status: pre-alpha. The listed pipeline commands are planned "
            "and intentionally return a not-implemented message in this scaffold."
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command")
    for command, help_text in PLANNED_COMMANDS.items():
        aliases = ["mix-bgm"] if command == "mix-background-music" else []
        command_parser = subparsers.add_parser(
            command,
            aliases=aliases,
            help=f"{help_text} (planned)",
            description=f"{help_text} This command is planned but not implemented yet.",
        )
        command_parser.set_defaults(canonical_command=command)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    command = getattr(args, "canonical_command", args.command)
    print(
        f"tts-pipeline command '{command}' is planned but not implemented yet. "
        "See README.md for the project roadmap.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
