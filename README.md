Jikanpy
=======

Jikanpy is a Python wrapper for [Jikan](https://github.com/jikan-me/jikan),
providing bindings for all API functionality. Because it is intended to be
pretty much identical, please consult [Jikan's
documentation](https://jikan.docs.apiary.io/#) for thornier details on how it is meant to
be used. Also, check out [this section](https://jikan.docs.apiary.io/#introduction/information/rate-limiting)
of documentation in order to see to what extent the API is limited or throttled.

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
# see Jikan docs for information about which endpoints have which extensions
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

# all the years and seasons on MAL
archive = jikan.season_archive()

# scheduled anime
scheduled = jikan.schedule()
# add a day of the week if you only want the day's schedule
monday = jikan.schedule(day='monday')

# top anime
top_anime = jikan.top(type='anime')
# add a page and subtype if you want
top_anime = jikan.top(type='anime', page=2, subtype='upcoming')

# action anime
# See Jikan docs for mappings between genres and their IDs
action = jikan.genre(type='anime', genre_id=1)
# adventure manga
adventure = jikan.genre(type='manga', genre_id=2)

# anime made by Studio Deen (sasuga deen)
studio_deen_anime = jikan.producer(producer_id=37)
# add an optional page
studio_deen_anime = jikan.producer(producer_id=37, page=2)

# manga from Weekly Shounen Jump
jump = jikan.magazine(magazine_id=83)
# add an optional page
jump = jikan.magazine(magazine_id=83, page=2)

# user info
nekomata1037 = jikan.user(username='Nekomata1037')
# get profile info, same as above
nekomata1037 = jikan.user(username='Nekomata1037', request='profile')
# friends info
nekomata1037 = jikan.user(username='Nekomata1037', request='friends')
# history of anime/manga
nekomata1037 = jikan.user(username='Nekomata1037', request='history')
# anime list
nekomata1037 = jikan.user(username='Nekomata1037', request='animelist')
# manga list
nekomata1037 = jikan.user(username='Nekomata1037', request='mangalist')

# meta info about the Jikan REST API
# meta info about what requests have been done
requests = jikan.meta(request='requests', type='anime', period='today')
# meta info about API's status
status = jikan.meta(request='status', type='anime', period='today')
```

### Async Usage (< Python 3.5)
```python
from jikanpy import AioJikan
import asyncio

loop = asyncio.get_event_loop()

aio_jikan = AioJikan(loop=loop)


@asyncio.coroutine
def main(loop):
    mushishi = yield from aio_jikan.anime(457)
    fma = yield from aio_jikan.manga(25)
    ginko = yield from aio_jikan.character(425)
    naruto = yield from aio_jikan.search(search_type='anime', query='naruto')
    winter_2018 = yield from aio_jikan.season(year=2018, season='winter')
    archive = yield from aio_jikan.season_archive()
    monday = yield from aio_jikan.schedule(day='monday')
    top_anime = yield from aio_jikan.top(type='anime')
    meta = yield from aio_jikan.meta(request='requests', type='anime', period='today')
    action = yield from aio_jikan.genre(type='anime', genre_id=1)
    deen = yield from aio_jikan.producer(producer_id=37)
    jump = yield from aio_jikan.magazine(magazine_id=83)
    nekomata1037 = yield from aio_jikan.user(username='Nekomata1037')
    # Close the connection to Jikan API
    yield from aio_jikan.close()


loop.run_until_complete(main(loop))
```

### Async Usage (Python 3.5+)
```python
from jikanpy import AioJikan

loop = asyncio.get_event_loop()

aio_jikan = AioJikan(loop=loop)


async def main(loop):
    mushishi = await aio_jikan.anime(457)
    fma = await aio_jikan.manga(25)
    ginko = await aio_jikan.character(425)
    naruto = await aio_jikan.search(search_type='anime', query='naruto')
    winter_2018 = await aio_jikan.season(year=2018, season='winter')
    archive = await aio_jikan.season_archive()
    monday = await aio_jikan.schedule(day='monday')
    top_anime = await aio_jikan.top(type='anime')
    meta = await aio_jikan.meta(request='requests', type='anime', period='today')
    action = await aio_jikan.genre(type='anime', genre_id=1)
    deen = await aio_jikan.producer(producer_id=37)
    jump = await aio_jikan.magazine(magazine_id=83)
    nekomata1037 = await aio_jikan.user(username='Nekomata1037')
    # Close the connection to Jikan API
    await aio_jikan.close()


loop.run_until_complete(main(loop))
```

### Testing
```shell
# In root of repository
$ python -m pytest
```
