Jikanpy
=======

Jikanpy is a Python wrapper for [Jikan](https://github.com/jikan-me/jikan),
providing bindings for all API functionality. Because it is intended to be
pretty much identical, please consult [Jikan's
documentation](https://jikan.docs.apiary.io/#) for thornier details on how it is meant to
be used. Perhaps most importantly, Jikanpy does not make any attempts to rate
limit itself, so use it as responsibly as you would use the API primitively.

## Installation
```shell
$ pip install git+git://github.com/AWConant/jikanpy.git
```

## Usage
```python
from jikanpy import Jikan
jikan = Jikan()

# json of all anime info specified by Jikan docs
mushishi = jikan.anime(457)

# same as above, but with extra info
# (see Jikan docs for information about which endpoints have which extensions)
mushishi_with_eps = jikan.anime(457, extension='episodes')
mushishi_with_eps_2 = jikan.anime(457, extension='episodes', page=2)
mushishi_with_characters_and_staff = jikan.anime(457, extension='characters_staff')

# you can also query characters
ginko = jikan.character(425)

# and manga
mushishi_manga = jikan.manga(418)

# search
search_result = jikan.search('anime', 'Mushishi')
# add a page number to the search request
search_result = jikan.search('anime', 'Mushishi', page=2)
# add a filter to the search (see Jikan docs about what filters are legal)
search_result = jikan.search('anime', 'Mushishi', key='type', value='tv')
search_result = jikan.search('anime', 'Mushishi', key='genre', value=37)
# use it all!
search_result = jikan.search('anime', 'Mushishi', page=3, key='type', value='tv')

# seasonal anime
winter_2018 = jikan.season(year=2018, season='winter')
spring_2016 = jikan.season(year=2016, season='spring')

# scheduled anime
scheduled = jikan.schedule()
# add a day of the week if you only want the day's schedule
monday = jikan.schedule(day='monday')

# top anime
top_anime = jikan.top(type='anime')
# add a page and subtype if you want
top_anime = jikan.top(type='anime', page=2, subtype='upcoming')

# meta info about the Jikan REST API
# meta info about what requests have been done
requests = jikan.meta(request='requests', type='anime', period='today')
# meta info about API's status
status = jikan.meta(request='status', type='anime', period='today')
```