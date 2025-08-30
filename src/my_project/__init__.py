from importlib.metadata import version, PackageNotFoundError

try:
    # must match the name in pyproject.toml
    __version__ = version("my-project")
except PackageNotFoundError:
    __version__ = "0.0.0"
