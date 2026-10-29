
# changelog

## [unreleased]

### added
- initial project structure
- python virtual environment
- initial documentation files
- read-only file scanner with file metadata collection and alphabetical sorting
- automated scanner tests for metadata, sorting, subdirectories, invalid paths, and file integrity
- extension-based file categorization for documents, images, videos, audio, archives, and code
- automated categorizer tests for supported extensions, unknown files, case-insensitive matching, and path inputs
- read-only organization planner that generates proposed category destinations without moving files
- automated planner tests for category assignments, destinations, unknown extensions, and empty input
- safe file movement with destination conflict protection and cleanup after copy failures
- automated mover tests for successful moves, invalid paths, existing destinations, and copy failures
### planned
- duplicate detection
- operation history and undo
- desktop interface