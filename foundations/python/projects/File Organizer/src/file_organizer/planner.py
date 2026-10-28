
from file_organizer.categorizer import categorize_file


def plan_organization(files: list[dict[str, str | int]]) -> list[dict[str, str]]:
    """Return proposed destinations without modifying files."""
    plan = []

    for file in files:
        category = categorize_file(file["name"])

        plan.append(
            {
                "name": file["name"],
                "category": category,
                "destination": f"{category}/{file['name']}",
            }
        )

    return plan
