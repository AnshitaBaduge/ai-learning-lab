"""
Safely reads and validates input from the user.
Kept separate from generator.py because "reading input" and
"generating passwords" are two unrelated responsibilities.
"""


def get_positive_int(prompt, default):
    """Reads an integer from the user, falling back to a default on bad input."""
    user_input = input(prompt).strip()
    if user_input == "":
        return default
    try:
        value = int(user_input)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print("Invalid number entered — using default value instead.")
        return default


def get_yes_no(prompt, default=True):
    """Reads a yes/no answer from the user."""
    user_input = input(prompt).strip().lower()
    if user_input == "":
        return default
    return user_input in ("y", "yes")