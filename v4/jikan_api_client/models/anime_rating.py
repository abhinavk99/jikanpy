from enum import Enum


class AnimeRating(str, Enum):
    G_ALL_AGES = "G - All Ages"
    PG_CHILDREN = "PG - Children"
    PG_13_TEENS_13_OR_OLDER = "PG-13 - Teens 13 or older"
    R_17_VIOLENCE_PROFANITY = "R - 17+ (violence & profanity)"
    R_MILD_NUDITY = "R+ - Mild Nudity"
    RX_HENTAI = "Rx - Hentai"

    def __str__(self) -> str:
        return str(self.value)
