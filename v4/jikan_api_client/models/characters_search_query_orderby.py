from enum import Enum


class CharactersSearchQueryOrderby(str, Enum):
    MAL_ID = "mal_id"
    NAME = "name"
    FAVORITES = "favorites"

    def __str__(self) -> str:
        return str(self.value)
