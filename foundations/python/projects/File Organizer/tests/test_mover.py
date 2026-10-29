import pytest
from unittest.mock import patch

import file_organizer.mover as mover
from file_organizer.mover import move_file


def test_move_file_moves_file_to_destination(tmp_path) -> None:
    source_dir = tmp_path / "source"
    destination_dir = tmp_path / "Documents"
    source_dir.mkdir()
    destination_dir.mkdir()

    source = source_dir / "report.pdf"
    source.write_text("test content")

    destination = move_file(source, destination_dir)

    assert destination == destination_dir / "report.pdf"
    assert destination.read_text() == "test content"
    assert not source.exists()


def test_move_file_rejects_existing_destination(tmp_path) -> None:
    source = tmp_path / "report.pdf"
    destination_dir = tmp_path / "Documents"
    destination_dir.mkdir()

    source.write_text("original content")
    target = destination_dir / "report.pdf"
    target.write_text("existing content")

    with pytest.raises(FileExistsError):
        move_file(source, destination_dir)

    assert source.read_text() == "original content"
    assert target.read_text() == "existing content"


def test_move_file_rejects_missing_source(tmp_path) -> None:
    destination_dir = tmp_path / "Documents"
    destination_dir.mkdir()

    with pytest.raises(FileNotFoundError):
        move_file(tmp_path / "missing.pdf", destination_dir)


def test_move_file_rejects_source_directory(tmp_path) -> None:
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    destination_dir = tmp_path / "Documents"
    destination_dir.mkdir()

    with pytest.raises(ValueError):
        move_file(source_dir, destination_dir)


def test_move_file_rejects_missing_destination_directory(tmp_path) -> None:
    source = tmp_path / "report.pdf"
    source.write_text("test content")

    with pytest.raises(FileNotFoundError):
        move_file(source, tmp_path / "missing")

    assert source.exists()


def test_move_file_rejects_destination_that_is_a_file(tmp_path) -> None:
    source = tmp_path / "report.pdf"
    source.write_text("test content")
    destination_file = tmp_path / "not_a_directory"
    destination_file.write_text("existing content")

    with pytest.raises(NotADirectoryError):
        move_file(source, destination_file)

    assert source.exists()
    


def test_move_file_cleans_up_destination_after_copy_failure(tmp_path) -> None:
    source = tmp_path / "report.pdf"
    destination_dir = tmp_path / "Documents"
    destination_dir.mkdir()
    source.write_text("original content")

    with patch.object(mover.shutil, "copyfileobj", side_effect=OSError("copy failed")):
        with pytest.raises(OSError, match="copy failed"):
            move_file(source, destination_dir)

    assert source.read_text() == "original content"
    assert not (destination_dir / "report.pdf").exists()
