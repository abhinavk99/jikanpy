from enum import Enum


class PeopleSearchQueryOrderby(str, Enum):
    MAL_ID = "mal_id"
    NAME = "name"
    BIRTHDAY = "birthday"
    FAVORITES = "favorites"

    def __str__(self) -> str:
        return str(self.value)
