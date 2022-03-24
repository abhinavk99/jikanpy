from enum import Enum


class MagazinesQueryOrderby(str, Enum):
    MAL_ID = "mal_id"
    NAME = "name"
    COUNT = "count"

    def __str__(self) -> str:
        return str(self.value)
