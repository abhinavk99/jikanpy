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

monday = jikan.schedule(day='monday')
print(monday)

top_anime = jikan.top(type='anime')
print(top_anime.keys())

meta = jikan.meta(request='requests', type='anime', period='today')
print(meta)
