
from pathlib import Path


def scan_directory(directory: str | Path) -> list[dict[str, str | int]]:
    """Return metadata for files directly inside a directory."""
    path = Path(directory)

    if not path.exists():
        raise FileNotFoundError(f"directory does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"path is not a directory: {path}")

    files = []

    for entry in path.iterdir():
        if not entry.is_file():
            continue

        try:
            files.append(
                {
                    "name": entry.name,
                    "extension": entry.suffix.lower(),
                    "size": entry.stat().st_size,
                    "path": str(entry.resolve()),
                }
            )
        except OSError:
            continue

    return sorted(files, key=lambda file: file["name"].lower())