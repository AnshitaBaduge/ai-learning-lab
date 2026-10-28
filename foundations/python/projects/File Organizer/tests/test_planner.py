
from file_organizer.planner import plan_organization


def test_plan_organization_assigns_categories_and_destinations() -> None:
    files = [
        {"name": "report.pdf", "extension": ".pdf", "size": 1200, "path": "/downloads/report.pdf"},
        {"name": "photo.jpg", "extension": ".jpg", "size": 2500, "path": "/downloads/photo.jpg"},
        {"name": "script.py", "extension": ".py", "size": 800, "path": "/downloads/script.py"},
    ]

    plan = plan_organization(files)

    assert plan == [
        {"name": "report.pdf", "category": "Documents", "destination": "Documents/report.pdf"},
        {"name": "photo.jpg", "category": "Images", "destination": "Images/photo.jpg"},
        {"name": "script.py", "category": "Code", "destination": "Code/script.py"},
    ]


def test_plan_organization_handles_unknown_extensions() -> None:
    files = [
        {"name": "file.xyz", "extension": ".xyz", "size": 100, "path": "/downloads/file.xyz"},
    ]

    plan = plan_organization(files)

    assert plan[0]["category"] == "Other"
    assert plan[0]["destination"] == "Other/file.xyz"


def test_plan_organization_handles_empty_list() -> None:
    assert plan_organization([]) == []
