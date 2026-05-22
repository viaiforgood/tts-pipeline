from __future__ import annotations

from unittest.mock import patch

import pytest

from tts_pipeline import __version__
from tts_pipeline.cli import main


def test_help_prints_usage(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])

    assert exc_info.value.code == 0

    output = capsys.readouterr().out
    assert "usage: tts-pipeline" in output
    assert "pre-alpha" in output


def test_no_args_prints_help(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0

    output = capsys.readouterr().out
    assert "text-to-audio" in output
    assert "text-to-video" in output


def test_version_matches_package(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])

    assert exc_info.value.code == 0
    assert __version__ in capsys.readouterr().out


@pytest.mark.parametrize(
    "command",
    ["text-to-audio", "mix-background-music", "mix-bgm", "text-to-video"],
)
def test_planned_commands_return_not_implemented(
    command: str, capsys: pytest.CaptureFixture[str]
) -> None:
    assert main([command]) == 1

    err = capsys.readouterr().err
    assert "planned but not implemented yet" in err


def test_audio_to_video_missing_audio(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["audio-to-video"])
    assert exc_info.value.code != 0
    err = capsys.readouterr().err
    assert "required: -a/--audio" in err or "required: -a" in err


@patch("tts_pipeline.video.render_audio_to_video")
def test_audio_to_video_single_file(mock_render) -> None:
    with patch("os.path.isdir", return_value=False):
        code = main([
            "audio-to-video",
            "-a", "dummy.mp3",
            "-i", "bg.jpg",
            "-o", "out.mp4",
            "-r", "1280x720",
            "--bitrate", "256k",
            "--no-meta",
        ])
        assert code == 0
        mock_render.assert_called_once_with(
            audio_path="dummy.mp3",
            image_path="bg.jpg",
            output_path="out.mp4",
            resolution="1280x720",
            audio_bitrate="256k",
            no_meta=True,
        )


@patch("tts_pipeline.video.batch_render_audio_to_video")
def test_audio_to_video_directory(mock_batch) -> None:
    mock_batch.return_value = (5, 0)
    with patch("os.path.isdir", return_value=True):
        code = main([
            "audio-to-video",
            "-a", "dummy_dir",
            "-i", "bg.jpg",
            "-o", "out_dir",
        ])
        assert code == 0
        mock_batch.assert_called_once_with(
            folder_path="dummy_dir",
            image_path="bg.jpg",
            output_dir="out_dir",
            resolution="1920x1080",
            audio_bitrate="192k",
            no_meta=False,
        )

