from jikanpy import Jikan

jikan = Jikan()

mushishi = jikan.anime(457)
print(mushishi)

fma = jikan.manga(25)
print(fma)

ginko = jikan.character(425)
print(ginko)

naruto = jikan.search(search_type='anime', query='naruto')
print(naruto)

winter_2018 = jikan.season(year=2018, season='winter')
print(winter_2018)

archive = jikan.season_archive()
print(archive)

later = jikan.season_later()
print(later)

monday = jikan.schedule(day='monday')
print(monday)

top_anime = jikan.top(type='anime')
print(top_anime)

action = jikan.genre(type='anime', genre_id=1)
print(action)

deen = jikan.producer(producer_id=37)
print(deen)

jump = jikan.magazine(magazine_id=83)
print(jump)

nekomata1037 = jikan.user(username='Nekomata1037')
print(nekomata1037)

meta = jikan.meta(request='requests', type='anime', period='today')
print(meta)
