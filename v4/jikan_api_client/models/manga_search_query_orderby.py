from enum import Enum


class MangaSearchQueryOrderby(str, Enum):
    MAL_ID = "mal_id"
    TITLE = "title"
    START_DATE = "start_date"
    END_DATE = "end_date"
    CHAPTERS = "chapters"
    VOLUMES = "volumes"
    SCORE = "score"
    SCORED_BY = "scored_by"
    RANK = "rank"
    POPULARITY = "popularity"
    MEMBERS = "members"
    FAVORITES = "favorites"

    def __str__(self) -> str:
        return str(self.value)
