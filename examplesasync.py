from jikanpy import AioJikan
import asyncio

loop = asyncio.get_event_loop()

aio_jikan = AioJikan(loop=loop)


@asyncio.coroutine
def main(loop):
    mushishi = yield from aio_jikan.anime(457)
    print(mushishi)

    fma = yield from aio_jikan.manga(25)
    print(fma)

    ginko = yield from aio_jikan.character(425)
    print(ginko)

    naruto = yield from aio_jikan.search(search_type='anime', query='naruto')
    print(naruto)

    winter_2018 = yield from aio_jikan.season(year=2018, season='winter')
    print(winter_2018)

    monday = yield from aio_jikan.schedule(day='monday')
    print(monday)

    top_anime = yield from aio_jikan.top(type='anime')
    print(top_anime)

    meta = yield from aio_jikan.meta(request='requests', type='anime', period='today')
    print(meta)

    # Close the connection to Jikan API
    yield from aio_jikan.close()


loop.run_until_complete(main(loop))

# Using async/await syntax (only supported in Python 3.5+)
#
# async def main(loop):
#     mushishi = await aio_jikan.anime(457)
#     print(mushishi)

#     fma = await aio_jikan.manga(25)
#     print(fma)

#     # Close the connection to Jikan API
#     await aio_jikan.close()

# loop.run_until_complete(main(loop))