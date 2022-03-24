from enum import Enum


class AnimeSearchQueryOrderby(str, Enum):
    MAL_ID = "mal_id"
    TITLE = "title"
    TYPE = "type"
    RATING = "rating"
    START_DATE = "start_date"
    END_DATE = "end_date"
    EPISODES = "episodes"
    SCORE = "score"
    SCORED_BY = "scored_by"
    RANK = "rank"
    POPULARITY = "popularity"
    MEMBERS = "members"
    FAVORITES = "favorites"

    def __str__(self) -> str:
        return str(self.value)
