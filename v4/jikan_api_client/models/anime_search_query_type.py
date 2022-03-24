from enum import Enum


class AnimeSearchQueryType(str, Enum):
    TV = "tv"
    MOVIE = "movie"
    OVA = "ova"
    SPECIAL = "special"
    ONA = "ona"
    MUSIC = "music"

    def __str__(self) -> str:
        return str(self.value)
