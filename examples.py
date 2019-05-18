from jikanpy import Jikan
from pprint import pprint

jikan = Jikan()

mushishi = jikan.anime(457)
pprint(mushishi)

fma = jikan.manga(25)
pprint(fma)

ginko = jikan.character(425)
pprint(ginko)

kana_hanazawa = jikan.person(189)
pprint(kana_hanazawa)

naruto = jikan.search(search_type="anime", query="naruto")
pprint(naruto)

winter_2018 = jikan.season(year=2018, season="winter")
pprint(winter_2018)

archive = jikan.season_archive()
pprint(archive)

later = jikan.season_later()
pprint(later)

monday = jikan.schedule(day="monday")
pprint(monday)

top_anime = jikan.top(type="anime")
pprint(top_anime)

action = jikan.genre(type="anime", genre_id=1)
pprint(action)

deen = jikan.producer(producer_id=37)
pprint(deen)

jump = jikan.magazine(magazine_id=83)
pprint(jump)

nekomata1037 = jikan.user(username="Nekomata1037")
pprint(nekomata1037)

fantasy_anime_league = jikan.club(379)
pprint(fantasy_anime_league)

meta = jikan.meta(request="requests", type="anime", period="today")
pprint(meta)
