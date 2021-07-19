"""
This module is for custom defined errors and/or exceptions
"""


class LinkException(Exception):
    def __init__(self, criteria: str) -> None:
        self.message = f"Link does not meet required criteria:\n'{criteria}'"
        super().__init__(self.message)
