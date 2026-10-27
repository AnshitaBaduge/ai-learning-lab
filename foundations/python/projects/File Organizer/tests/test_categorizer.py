from pathlib import Path

import pytest

from file_organizer.categorizer import categorize_file


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("report.pdf", "Documents"),
        ("notes.docx", "Documents"),
        ("photo.jpg", "Images"),
        ("image.png", "Images"),
        ("movie.mp4", "Videos"),
        ("clip.mkv", "Videos"),
        ("song.mp3", "Audio"),
        ("recording.wav", "Audio"),
        ("backup.zip", "Archives"),
        ("archive.tar.gz", "Archives"),
        ("script.py", "Code"),
        ("app.js", "Code"),
        ("unknown.xyz", "Other"),
        ("LICENSE", "Other"),
    ],
)
def test_categorize_file(filename: str, expected: str) -> None:
    assert categorize_file(filename) == expected


def test_categorize_file_is_case_insensitive() -> None:
    assert categorize_file("PHOTO.JPG") == "Images"


def test_categorize_file_accepts_path() -> None:
    assert categorize_file(Path("documents/report.pdf")) == "Documents"