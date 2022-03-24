from enum import Enum


class GetUserHistoryType(str, Enum):
    ANIME = "anime"
    MANGA = "manga"

    def __str__(self) -> str:
        return str(self.value)
