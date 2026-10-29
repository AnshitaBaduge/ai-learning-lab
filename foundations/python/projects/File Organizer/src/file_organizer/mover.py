
import os
import shutil
from pathlib import Path


def move_file(source: str | Path, destination_dir: str | Path) -> Path:
    """Move a file without overwriting an existing destination."""
    source_path = Path(source)
    destination_path = Path(destination_dir)

    if not source_path.exists():
        raise FileNotFoundError(f"source file does not exist: {source_path}")

    if not source_path.is_file():
        raise ValueError(f"source is not a file: {source_path}")

    if not destination_path.exists():
        raise FileNotFoundError(
            f"destination directory does not exist: {destination_path}"
        )

    if not destination_path.is_dir():
        raise NotADirectoryError(
            f"destination is not a directory: {destination_path}"
        )

    target_path = destination_path / source_path.name

    with source_path.open("rb") as source_file:
        file_descriptor = os.open(
            target_path,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o666,
        )

        try:
            with os.fdopen(file_descriptor, "wb") as target_file:
                shutil.copyfileobj(source_file, target_file)
                target_file.flush()
                os.fsync(target_file.fileno())
        except Exception:
            target_path.unlink(missing_ok=True)
            raise

    try:
        source_path.unlink()
    except OSError:
        target_path.unlink(missing_ok=True)
        raise

    return target_path
