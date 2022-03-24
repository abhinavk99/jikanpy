from enum import Enum


class GetTopMangaFilter(str, Enum):
    PUBLISHING = "publishing"
    UPCOMING = "upcoming"
    BYPOPULARITY = "bypopularity"
    FAVORITE = "favorite"

    def __str__(self) -> str:
        return str(self.value)
