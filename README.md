# Jikanpy

[![Travis (.org)](https://img.shields.io/travis/abhinavk99/jikanpy.svg?style=flat-square)](https://travis-ci.org/abhinavk99/jikanpy)
[![Codecov](https://img.shields.io/codecov/c/github/abhinavk99/jikanpy.svg?style=flat-square)](https://codecov.io/gh/abhinavk99/jikanpy/)
[![pypi Version](https://img.shields.io/pypi/v/jikanpy.svg?style=flat-square)](https://pypi.org/project/jikanpy/)
[![PyPi downloads](https://img.shields.io/pypi/dm/jikanpy?style=flat-square)](https://pypi.org/project/jikanpy/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Jikanpy is a Python wrapper for [Jikan](https://github.com/jikan-me/jikan),
providing bindings for all API functionality, and supports Python 3.6+. Because it is intended to be
pretty much identical, please consult [Jikan's
documentation](https://jikan.docs.apiary.io/#) for thornier details on how it is meant to
be used. Perhaps most importantly, Jikanpy does not make any attempts to rate
limit itself, so use it as responsibly as you would use the API primitively and
remember that Jikan API has limitations, check out [this section](https://jikan.docs.apiary.io/#introduction/information/rate-limiting)
of documentation in order to see to what extent the API is limited or throttled.

In addition to the typical response from the API, each response contains two additional fields:

- `jikan_url`: The URL that was requested; for example: `https://api.jikan.moe/v3/anime/1`.
- `headers`: The response headers from Jikan, detailed [here](https://jikan.docs.apiary.io/#introduction/information/caching).

## Installation

```shell
$ pip install jikanpy
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

# search up people too
kana_hanazawa = jikan.person(185)

# search
search_result = jikan.search('anime', 'Mushishi')
# add a page number to the search request
search_result = jikan.search('anime', 'Mushishi', page=2)
# add a filter to the search (see Jikan docs about what filters are legal)
search_result = jikan.search('anime', 'Mushishi', parameters={'type': 'tv'})
search_result = jikan.search('anime', 'Mushishi', parameters={'genre': 37})
# use multiple query parameters
search_result = jikan.search('anime', 'Mushishi', parameters={'genre': 37, 'type': 'tv'})
# use it all!
search_result = jikan.search('anime', 'Mushishi', page=3, parameters={'genre': 37, 'type': 'tv'})

# seasonal anime
winter_2018 = jikan.season(year=2018, season='winter')
spring_2016 = jikan.season(year=2016, season='spring')

# all the years and seasons on MAL
archive = jikan.season_archive()

# anime in upcoming seasons
later = jikan.season_later()

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
nekomata1037 = jikan.user(username='Nekomata1037', request='animelist', argument='completed', page=2)
# manga list
xinil = jikan.user(username='Xinil', request='mangalist')
xinil = jikan.user(username='Xinil', request='mangalist', argument='all')
# user info filters (see Jikan docs for valid filters)
nekomata1037 = jikan.user(username='Nekomata1037', request='animelist', parameters={'year': 2019})

# clubs
fantasy_anime_league = jikan.club(379)

# meta info about the Jikan REST API
# meta info about what requests have been done
requests = jikan.meta(request='requests', type='anime', period='today')
# meta info about API's status
status = jikan.meta(request='status', type='anime', period='today')
```

## Async Usage

```python
import asyncio
from jikanpy import AioJikan

loop = asyncio.get_event_loop()

async def main(loop):
    aio_jikan = AioJikan(loop=loop)

    mushishi = await aio_jikan.anime(457)
    fma = await aio_jikan.manga(25)
    ginko = await aio_jikan.character(425)
    kana_hanazawa = await aio_jikan.person(185)
    naruto = await aio_jikan.search(search_type='anime', query='naruto')
    winter_2018 = await aio_jikan.season(year=2018, season='winter')
    archive = await aio_jikan.season_archive()
    later = await aio_jikan.season_later()
    monday = await aio_jikan.schedule(day='monday')
    top_anime = await aio_jikan.top(type='anime')
    meta = await aio_jikan.meta(request='requests', type='anime', period='today')
    action = await aio_jikan.genre(type='anime', genre_id=1)
    deen = await aio_jikan.producer(producer_id=37)
    jump = await aio_jikan.magazine(magazine_id=83)
    nekomata1037 = await aio_jikan.user(username='Nekomata1037')
    fantasy_anime_league = await aio_jikan.club(379)
    # Close the connection to Jikan API
    await aio_jikan.close()


loop.run_until_complete(main(loop))
```

## Overriding default settings in Jikan and AioJikan with constructor arguments

If you're running an instance of [jikan-rest](https://github.com/jikan-me/jikan-rest) on your system, and want to use that instead of [api.jikan.moe](https://jikan.moe/), you can pass that to Jikan:

```python
from jikanpy import Jikan
jikan = Jikan(selected_base='http://localhost:8000/v3/')
```

You can also choose whether or not to use the HTTPS version of the [api.jikan.moe](https://jikan.moe/) URL or not,
which defaults to True.

```python
from jikanpy import Jikan
jikan_1 = Jikan()               # HTTPS
jikan_2 = Jikan(use_ssl=True)   # HTTPS
jikan_3 = Jikan(use_ssl=False)  # HTTP
```

If you want to use your own Requests session, you can do that too.

```python
import requests
from jikanpy import Jikan

session = requests.Session()
# Set custom persistent headers that will be used with all HTTP requests with your session
session.headers.update({'x-test': 'true'})

jikan = Jikan(session=session)
```

You can use any or all of these constructor arguments when creating an instance of Jikan.

AioJikan also has `selected_base`, `use_ssl`, and `session` (although AioJikan uses AioHTTP session, not Requests),
but also has `loop`, to provide your own asynchronous event loop.

```python
import aiohttp
import asyncio

from jikanpy import AioJikan

loop = asyncio.get_event_loop()

async def main(loop):
    # Construct AioJikan with own base URL and custom AioHTTP session with custom persistent headers and event loop
    session = aiohttp.ClientSession(loop=loop, headers={'x-test': 'true'})
    aio_jikan_1 = AioJikan(selected_base='http://localhost:8000/v3/', session=session)

    # Construct AioJikan with jikan.moe HTTP URL and event loop that will be used in internal AioHTTP session
    aio_jikan_2 = AioJikan(use_ssl=False, loop=loop)

    await aio_jikan_1.close()
    await aio_jikan_2.close()

loop.run_until_complete(main(loop))
```

## Testing

```shell
# In root of repository
$ pytest
```
