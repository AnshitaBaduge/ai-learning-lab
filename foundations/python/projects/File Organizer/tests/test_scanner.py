
from pathlib import Path

import pytest

from file_organizer.scanner import scan_directory


def test_scan_directory_returns_file_metadata(tmp_path: Path) -> None:
    file_path = tmp_path / "report.txt"
    file_path.write_text("hello", encoding="utf-8")

    result = scan_directory(tmp_path)

    assert len(result) == 1
    assert result[0]["name"] == "report.txt"
    assert result[0]["extension"] == ".txt"
    assert result[0]["size"] == 5
    assert result[0]["path"] == str(file_path.resolve())


def test_scan_directory_sorts_files_alphabetically(tmp_path: Path) -> None:
    (tmp_path / "zebra.txt").touch()
    (tmp_path / "Apple.pdf").touch()
    (tmp_path / "mango.csv").touch()

    result = scan_directory(tmp_path)

    assert [file["name"] for file in result] == [
        "Apple.pdf",
        "mango.csv",
        "zebra.txt",
    ]


def test_scan_directory_ignores_subdirectories(tmp_path: Path) -> None:
    (tmp_path / "document.txt").touch()
    (tmp_path / "subfolder").mkdir()
    (tmp_path / "subfolder" / "nested.txt").touch()

    result = scan_directory(tmp_path)

    assert [file["name"] for file in result] == ["document.txt"]


def test_scan_directory_raises_for_missing_directory(
    tmp_path: Path,
) -> None:
    missing_path = tmp_path / "missing"

    with pytest.raises(FileNotFoundError):
        scan_directory(missing_path)


def test_scan_directory_raises_for_file_path(tmp_path: Path) -> None:
    file_path = tmp_path / "document.txt"
    file_path.touch()

    with pytest.raises(NotADirectoryError):
        scan_directory(file_path)


def test_scan_directory_does_not_modify_files(tmp_path: Path) -> None:
    file_path = tmp_path / "important.txt"
    original_content = "keep this content safe"
    file_path.write_text(original_content, encoding="utf-8")

    scan_directory(tmp_path)

    assert file_path.read_text(encoding="utf-8") == original_content