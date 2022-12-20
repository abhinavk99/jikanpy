from jikanpy import Jikan
from pprint import pprint

jikan = Jikan()

# The following are examples only. Running this many at once
# will get you rate limited if you are not self hosting

mushishi = jikan.anime(457)
pprint(mushishi)

fma = jikan.manga(25)
pprint(fma)

ginko = jikan.characters(425)
pprint(ginko)

kana_hanazawa = jikan.people(185)
pprint(kana_hanazawa)

naruto_search = jikan.search(search_type="anime", query="naruto")
pprint(naruto)

winter_2018 = jikan.seasons(year=2018, season="winter")
pprint(winter_2018)

seasons = jikan.season_history()
pprint(seasons)

upcoming = jikan.seasons(extension='upcoming')
pprint(upcoming)

current_season = jikan.seasons(extension='now')
pprint(current_season)

monday = jikan.schedules(day="monday")
pprint(monday)

top_anime = jikan.top(type="anime")
pprint(top_anime)

action = jikan.genres(type="anime")
pprint(action)

deen = jikan.producers(37)
pprint(deen)

nekomata1037 = jikan.users(username="Nekomata1037")
pprint(nekomata1037)

fantasy_anime_league = jikan.clubs(379)
pprint(fantasy_anime_league)
