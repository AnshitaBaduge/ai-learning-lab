"""
    Core password-generation logic. No user interaction here at all —
    this file only knows how to build passwords, nothing about menus or input().
"""

import string
import secrets


class PasswordGenerator:
    """Generates secure passwords based on configurable rules."""

    def __init__(self, length=12, use_upper=True, use_digits=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def _build_character_pool(self):
        """Builds the set of allowed characters based on current settings."""
        pool = string.ascii_lowercase

        if self.use_upper:
            pool += string.ascii_uppercase
        if self.use_digits:
            pool += string.digits
        if self.use_symbols:
            pool += string.punctuation

        return pool

    def generate(self):
        """Generates a single password. Raises ValueError on invalid settings."""
        if self.length < 4:
            raise ValueError("Password length must be at least 4 characters.")

        pool = self._build_character_pool()
        if not pool:
            raise ValueError("Character pool is empty — enable at least one character type.")

        # secrets.choice is cryptographically secure, unlike the plain `random` module
        return "".join(secrets.choice(pool) for _ in range(self.length))

    def generate_multiple(self, count=1):
        """Generates a list of passwords."""
        if count < 1:
            raise ValueError("Count must be at least 1.")
        return [self.generate() for _ in range(count)]