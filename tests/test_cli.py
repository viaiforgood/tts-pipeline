from __future__ import annotations

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
    ["text-to-audio", "mix-background-music", "mix-bgm", "audio-to-video", "text-to-video"],
)
def test_planned_commands_return_not_implemented(
    command: str, capsys: pytest.CaptureFixture[str]
) -> None:
    assert main([command]) == 1

    err = capsys.readouterr().err
    assert "planned but not implemented yet" in err
