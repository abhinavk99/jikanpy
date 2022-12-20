from pprint import pprint

import asyncio
from jikanpy import AioJikan


aio_jikan = AioJikan()

# The following are examples only. Running this many at once
# will get you rate limited if you are not self hosting

async def main():
    async with AioJikan() as aio_jikan:
        mushishi = await aio_jikan.anime(457)
        pprint(mushishi)

        fma = await aio_jikan.manga(25)
        pprint(fma)

        ginko = await aio_jikan.characters(425)
        pprint(ginko)

        naruto = await aio_jikan.search(search_type="anime", query="naruto")
        pprint(naruto)

        winter_2018 = await aio_jikan.seasons(year=2018, season="winter")
        pprint(winter_2018)

        monday = await aio_jikan.schedules(day="monday")
        pprint(monday)

        top_anime = await aio_jikan.top(type="anime")
        pprint(top_anime)


asyncio.run(main())
