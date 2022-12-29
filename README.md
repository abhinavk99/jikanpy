# JikanPy

[![Travis (.com)](https://img.shields.io/travis/com/abhinavk99/jikanpy?style=flat-square)](https://travis-ci.com/abhinavk99/jikanpy)
[![Codecov](https://img.shields.io/codecov/c/github/abhinavk99/jikanpy.svg?style=flat-square)](https://codecov.io/gh/abhinavk99/jikanpy/)
[![pypi Version](https://img.shields.io/pypi/v/jikanpy.svg?style=flat-square)](https://pypi.org/project/jikanpy-v4/)
[![PyPi downloads](https://img.shields.io/pypi/dm/jikanpy?style=flat-square)](https://pypi.org/project/jikanpy-v4/)
[![Documentation](https://readthedocs.org/projects/jikanpy/badge/?version=latest&style=flat-square)](https://jikanpy.readthedocs.io/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

JikanPy is a Python wrapper for [Jikan](https://github.com/jikan-me/jikan),
providing bindings for all API functionality, and supports Python 3.6+. Because
it is intended to be pretty much identical, please consult [Jikan's
documentation](https://docs.api.jikan.moe/) for thornier details on how it is
meant to be used. Perhaps most importantly, JikanPy does not make any attempts
to rate limit itself, so use it as responsibly as you would use the API
primitively and remember that Jikan API has limitations, check out
[this section](https://docs.api.jikan.moe/#section/Information/Rate-Limiting)
of documentation in order to see to what extent the API is limited or throttled.

You can use either Jikan or AioJikan depending on whether you want a synchronous
wrapper class or an asynchronous wrapper class respectively. More usage examples
are below.

In addition to the typical response from the Jikan API, each response contains
two additional fields:

- `jikan_url`: The URL that was requested; for example: `https://api.jikan.moe/v4/anime/1`.
- `headers`: The response headers from Jikan, detailed [here](https://docs.api.jikan.moe/#section/Information/Caching).

## Installation
You can install the package from PyPI using pip:

```shell
$ pip install jikanpy-v4
```

If you have previously installed the old version of jikanpy, then make sure to uninstall the old version first:

```shell
$ pip uninstall jikanpy
$ pip install --no-cache-dir jikanpy-v4
```

You can also install this package directly from the source:
```shell
$ git clone https://github.com/abhinavk99/jikanpy.git 
$ cd jikanpy
$ python setup.py install
```

*Note*: This package is different from `jikanpy` on PyPI, which is the old Jikan v3 compatible version of [jikanpy](https://github.com/abhinavk99/jikanpy/tree/jikanpy_v3).

## Usage Examples

Below are some basic examples of how to use Jikan and AioJikan. Please read the
[documentation below](#documentation) to see all the methods and more examples.

### Usage Examples with Jikan

```python
from jikanpy import Jikan
jikan = Jikan()

mushishi = jikan.anime(457)
mushishi_with_eps = jikan.anime(457, extension='episodes')

search_result = jikan.search('anime', 'Mushishi', page=2)

winter_2018_anime = jikan.seasons(year=2018, season='winter')

current_season = jikan.seasons(extension='now')
```

### Async Usage Examples with AioJikan

```python
import asyncio
from jikanpy import AioJikan

async def main():
    async with AioJikan() as aio_jikan:
        mushishi = await aio_jikan.anime(457)
        fma = await aio_jikan.manga(25)
        ginko = await aio_jikan.character(425)
        kana_hanazawa = await aio_jikan.person(185)
        naruto = await aio_jikan.search(search_type='anime', query='naruto')

    # You can also construct AioJikan like below, but make sure to close the object
    aio_jikan_2 = AioJikan()
    mushishi = await aio_jikan.anime(457)
    await aio_jikan_2.close()

asyncio.run(main())
```

## Documentation

Check out the documentation [here](https://jikanpy.readthedocs.io).

## Overriding default settings in Jikan and AioJikan with constructor arguments

If you're running an instance of [jikan-rest](https://github.com/jikan-me/jikan-rest)
on your system, and want to use that instead of [api.jikan.moe](https://jikan.moe/),
you can pass that to Jikan:

```python
from jikanpy import Jikan
jikan = Jikan(selected_base='http://localhost:8000/v4')
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

You can use any or all of these constructor arguments when creating an instance
of Jikan.

AioJikan also has `selected_base` and `session` (although AioJikan uses AioHTTP
session, not Requests).

```python
import aiohttp
import asyncio

from jikanpy import AioJikan

async def main():
    # Construct AioJikan with own base URL and custom AioHTTP session with custom persistent headers
    session = aiohttp.ClientSession(headers={'x-test': 'true'})
    aio_jikan = AioJikan(selected_base='http://localhost:8000/v4', session=session)
    await session.close()

asyncio.run(main())
```

## Testing

```shell
# In root of repository
$ pytest -m pytest tests/
# Optionally, you can run a single test:
$ pytest -m pytest tests/test_jikan.py::test_anime_episodes_success
```
