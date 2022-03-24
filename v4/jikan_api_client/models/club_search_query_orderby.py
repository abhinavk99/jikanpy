from enum import Enum


class ClubSearchQueryOrderby(str, Enum):
    MAL_ID = "mal_id"
    TITLE = "title"
    MEMBERS_COUNT = "members_count"
    PICTURES_COUNT = "pictures_count"
    CREATED = "created"

    def __str__(self) -> str:
        return str(self.value)
