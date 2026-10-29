"""Official LlamaIndex tools for the VideoGen API."""

from importlib.metadata import PackageNotFoundError, version

from .base import VideoGenToolSpec, create_videogen_tools
from .client import resolve_client
from .operations import Controls

__all__ = [
    "Controls",
    "VideoGenToolSpec",
    "create_videogen_tools",
    "resolve_client",
]

try:
    __version__ = version("llama-index-tools-videogen")
except PackageNotFoundError:
    __version__ = "0.0.0"
