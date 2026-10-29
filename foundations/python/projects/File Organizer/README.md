
# smart file organizer

a python project to organize files efficiently and safely.

## status

in development - read-only file scanning, extension-based file categorization, organization planning, and safe file movement implemented with automated tests.

## planned features

- scan and categorize files by extension
- preview changes before moving files
- handle filename conflicts safely
- detect duplicate files
- maintain operation history and support undo
- generate storage reports

## tech stack

- python
- pathlib and shutil
- hashlib
- sqlite
- pytest

## project structure

- `src/file_organizer/` - application code
- `tests/` - automated tests
- `docs/` - project documentation
- `examples/` - sample files and rules

## development

the project is being developed incrementally, with tests and documentation updated alongside each feature.

## safety

the scanner reads file metadata only. it does not move, rename, delete, or modify files. file modifications will be introduced only after preview and conflict handling are implemented.

## license

to be decided
