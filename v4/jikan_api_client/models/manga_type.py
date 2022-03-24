from enum import Enum


class MangaType(str, Enum):
    MANGA = "Manga"
    NOVEL = "Novel"
    ONE_SHOT = "One-shot"
    DOUJINSHI = "Doujinshi"
    MANHUA = "Manhua"
    MANHWA = "Manhwa"
    OEL = "OEL"

    def __str__(self) -> str:
        return str(self.value)
