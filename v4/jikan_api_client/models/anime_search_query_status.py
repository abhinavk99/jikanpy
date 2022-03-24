from enum import Enum


class AnimeSearchQueryStatus(str, Enum):
    AIRING = "airing"
    COMPLETE = "complete"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
