from enum import Enum


class MangaSearchQueryType(str, Enum):
    MANGA = "manga"
    NOVEL = "novel"
    LIGHTNOVEL = "lightnovel"
    ONESHOT = "oneshot"
    DOUJIN = "doujin"
    MANHWA = "manhwa"
    MANHUA = "manhua"

    def __str__(self) -> str:
        return str(self.value)
