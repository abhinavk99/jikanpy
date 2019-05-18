from jikanpy import AioJikan
import asyncio
from pprint import pprint

loop = asyncio.get_event_loop()

aio_jikan = AioJikan(loop=loop)


async def main(loop):
    mushishi = await aio_jikan.anime(457)
    pprint(mushishi)

    fma = await aio_jikan.manga(25)
    pprint(fma)

    ginko = await aio_jikan.character(425)
    pprint(ginko)

    naruto = await aio_jikan.search(search_type="anime", query="naruto")
    pprint(naruto)

    winter_2018 = await aio_jikan.season(year=2018, season="winter")
    pprint(winter_2018)

    monday = await aio_jikan.schedule(day="monday")
    pprint(monday)

    top_anime = await aio_jikan.top(type="anime")
    pprint(top_anime)

    meta = await aio_jikan.meta(request="requests", type="anime", period="today")
    pprint(meta)

    # Close the connection to Jikan API
    await aio_jikan.close()


loop.run_until_complete(main(loop))
