"""Text-to-speech pipeline for narrated audio and video assets."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("tts-pipeline")
except PackageNotFoundError:
    __version__ = "0.0.0+local"
