from enum import Enum


class GetTopAnimeFilter(str, Enum):
    AIRING = "airing"
    UPCOMING = "upcoming"
    BYPOPULARITY = "bypopularity"
    FAVORITE = "favorite"

    def __str__(self) -> str:
        return str(self.value)
