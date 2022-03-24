from enum import Enum


class MangaSearchQueryStatus(str, Enum):
    PUBLISHING = "publishing"
    COMPLETE = "complete"
    HIATUS = "hiatus"
    DISCONTINUED = "discontinued"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
