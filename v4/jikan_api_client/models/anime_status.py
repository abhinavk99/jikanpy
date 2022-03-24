from enum import Enum


class AnimeStatus(str, Enum):
    FINISHED_AIRING = "Finished Airing"
    CURRENTLY_AIRING = "Currently Airing"
    NOT_YET_AIRED = "Not yet aired"

    def __str__(self) -> str:
        return str(self.value)
