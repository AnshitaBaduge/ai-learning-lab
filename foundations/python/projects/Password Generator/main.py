"""
main.py
-------
Entry point. Handles the user-facing flow, using the engine (generator.py) and input helpers (validators.py). 
"""

from generator import PasswordGenerator
from validators import get_positive_int, get_yes_no


def main():
    print("=== Password Generator ===")

    length = get_positive_int("Password length (default 12): ", default=12)
    use_upper = get_yes_no("Include uppercase letters? (Y/n): ", default=True)
    use_digits = get_yes_no("Include digits? (Y/n): ", default=True)
    use_symbols = get_yes_no("Include symbols? (Y/n): ", default=True)
    count = get_positive_int("How many passwords to generate? (default 1): ", default=1)

    generator = PasswordGenerator(length, use_upper, use_digits, use_symbols)

    try:
        passwords = generator.generate_multiple(count)
        print("\nGenerated password(s):")
        for i, pwd in enumerate(passwords, start=1):
            print(f"{i}. {pwd}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()