from enum import Enum


class GenreQueryFilter(str, Enum):
    GENRES = "genres"
    EXPLICIT_GENRES = "explicit_genres"
    THEMES = "themes"
    DEMOGRAPHICS = "demographics"

    def __str__(self) -> str:
        return str(self.value)
