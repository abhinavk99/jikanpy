from enum import Enum


class GetAnimeForumFilter(str, Enum):
    ALL = "all"
    EPISODE = "episode"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
