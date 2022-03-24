from enum import Enum


class AnimeType(str, Enum):
    TV = "TV"
    OVA = "OVA"
    MOVIE = "Movie"
    SPECIAL = "Special"
    ONA = "ONA"
    MUSIC = "Music"

    def __str__(self) -> str:
        return str(self.value)
