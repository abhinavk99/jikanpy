from enum import Enum


class ClubDataCategory(str, Enum):
    ACTORS_ARTISTS = "actors & artists"
    ANIME = "anime"
    CHARACTERS = "characters"
    CITIES_NEIGHBORHOODS = "cities & neighborhoods"
    COMPANIES = "companies"
    CONVENTIONS = "conventions"
    GAMES = "games"
    JAPAN = "japan"
    MANGA = "manga"
    MUSIC = "music"
    OTHERS = "others"
    SCHOOLS = "schools"

    def __str__(self) -> str:
        return str(self.value)
