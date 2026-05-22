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
            "and intentionally return a not-implemented message in this scaffold "
            "except for implemented commands."
        ),
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command")
    for command, help_text in PLANNED_COMMANDS.items():
        aliases = ["mix-bgm"] if command == "mix-background-music" else []
        if command == "audio-to-video":
            command_parser = subparsers.add_parser(
                command,
                aliases=aliases,
                help=help_text,
                description="Render an audio file or directory of audio files as an MP4 video with a static background image.",
            )
            command_parser.add_argument(
                "-a", "--audio", required=True, help="Input audio file OR directory for batch mode."
            )
            command_parser.add_argument(
                "-i", "--image", help="Background image (defaults: assets/background/background.jpg or .png)."
            )
            command_parser.add_argument(
                "-o", "--output", help="Output MP4 file path OR output directory for batch mode (defaults: auto)."
            )
            command_parser.add_argument(
                "-r", "--resolution", default="1920x1080", help="Output video resolution (default: 1920x1080)."
            )
            command_parser.add_argument(
                "--bitrate", default="192k", help="Audio bitrate (default: 192k)."
            )
            command_parser.add_argument(
                "--no-meta", action="store_true", help="Skip embedding default metadata."
            )
            command_parser.set_defaults(canonical_command=command)
        else:
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
    if command == "audio-to-video":
        from tts_pipeline.video import batch_render_audio_to_video, render_audio_to_video
        import os

        try:
            if os.path.isdir(args.audio):
                success, failure = batch_render_audio_to_video(
                    folder_path=args.audio,
                    image_path=args.image,
                    output_dir=args.output,
                    resolution=args.resolution,
                    audio_bitrate=args.bitrate,
                    no_meta=args.no_meta,
                )
                return 0 if failure == 0 else 1
            else:
                render_audio_to_video(
                    audio_path=args.audio,
                    image_path=args.image,
                    output_path=args.output,
                    resolution=args.resolution,
                    audio_bitrate=args.bitrate,
                    no_meta=args.no_meta,
                )
                return 0
        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            return 1

    print(
        f"tts-pipeline command '{command}' is planned but not implemented yet. "
        "See README.md for the project roadmap.",
        file=sys.stderr,
    )
    return 1



if __name__ == "__main__":
    raise SystemExit(main())
