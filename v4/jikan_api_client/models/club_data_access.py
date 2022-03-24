from enum import Enum


class ClubDataAccess(str, Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    SECRET = "secret"

    def __str__(self) -> str:
        return str(self.value)
