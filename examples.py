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