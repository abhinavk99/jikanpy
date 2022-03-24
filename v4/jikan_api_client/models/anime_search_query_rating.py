from enum import Enum


class AnimeSearchQueryRating(str, Enum):
    G = "g"
    PG = "pg"
    PG13 = "pg13"
    R17 = "r17"
    R = "r"
    RX = "rx"

    def __str__(self) -> str:
        return str(self.value)
