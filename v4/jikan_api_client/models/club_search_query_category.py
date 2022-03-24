from enum import Enum


class ClubSearchQueryCategory(str, Enum):
    ANIME = "anime"
    MANGA = "manga"
    ACTORS_AND_ARTISTS = "actors_and_artists"
    CHARACTERS = "characters"
    CITIES_AND_NEIGHBORHOODS = "cities_and_neighborhoods"
    COMPANIES = "companies"
    CONVENTIONS = "conventions"
    GAMES = "games"
    JAPAN = "japan"
    MUSIC = "music"
    OTHER = "other"
    SCHOOLS = "schools"

    def __str__(self) -> str:
        return str(self.value)
