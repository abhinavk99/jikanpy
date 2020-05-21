import pytest
import vcr

from jikanpy import AioJikan, utils, APIException, DeprecatedEndpoint

from constants import (
    MUSHISHI_ID,
    FULLMETAL_ID,
    GINKO_ID,
    KANA_HANAZAWA_ID,
    YEAR,
    SEASON,
    DAY,
    TYPE,
    SUBTYPE,
    GENRE,
    PRODUCER,
    MAGAZINE,
    USERNAME,
    CLUB_ID,
)

pytestmark = pytest.mark.asyncio


@pytest.fixture
def aio_jikan():
    return AioJikan()


async def test_construct_using_async_with():
    async with AioJikan() as aio_jikan:
        assert isinstance(aio_jikan, AioJikan)


@vcr.use_cassette("tests/vcr_cassettes/aio-wrap-response.yaml")
async def test_wrap_response(aio_jikan):
    anime_info = await aio_jikan.anime(MUSHISHI_ID)
    mushishi_url = utils.get_main_url("anime", MUSHISHI_ID, extension=None, page=None)

    assert isinstance(anime_info, dict)
    assert "jikan_url" in anime_info
    assert "headers" in anime_info
    assert isinstance(anime_info["headers"], dict)
    assert mushishi_url == anime_info["jikan_url"]
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-anime-success.yaml")
async def test_anime_success(anime_keys, aio_jikan):
    anime_info = await aio_jikan.anime(MUSHISHI_ID)

    assert isinstance(anime_info, dict)
    assert anime_info["title"] == "Mushishi"
    assert anime_keys.issubset(anime_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-anime-episodes-success.yaml")
async def test_anime_episodes_success(anime_episodes_keys, episode_keys, aio_jikan):
    anime_episodes_info = await aio_jikan.anime(
        MUSHISHI_ID, extension="episodes", page=1
    )

    assert isinstance(anime_episodes_info, dict)
    assert isinstance(anime_episodes_info["episodes"], list)
    for episode in anime_episodes_info["episodes"]:
        assert episode_keys.issubset(episode.keys())
    assert anime_episodes_keys.issubset(anime_episodes_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-manga-success.yaml")
async def test_manga_success(manga_keys, aio_jikan):
    manga_info = await aio_jikan.manga(FULLMETAL_ID)

    assert isinstance(manga_info, dict)
    assert manga_info["title"] == "Fullmetal Alchemist"
    assert manga_keys.issubset(manga_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-character-success.yaml")
async def test_character_success(character_keys, aio_jikan):
    character_info = await aio_jikan.character(GINKO_ID)

    assert isinstance(character_info, dict)
    assert character_info["name"] == "Ginko"
    assert character_keys.issubset(character_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-person-success.yaml")
async def test_person_success(person_keys, aio_jikan):
    person_info = await aio_jikan.person(KANA_HANAZAWA_ID)

    assert isinstance(person_info, dict)
    assert person_info["name"] == "Kana Hanazawa"
    assert person_keys.issubset(person_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-search-success.yaml")
async def test_search_success(search_keys, aio_jikan):
    search_info = await aio_jikan.search(
        search_type="anime", query="naruto", parameters={"genre": "1,2", "limit": 10}
    )

    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-search-genre-exclude-success.yaml")
async def test_search_genre_exclude_success(search_keys, aio_jikan):
    search_info = await aio_jikan.search(
        search_type="anime",
        query="naruto",
        parameters={"genre": "1,2", "genre_exclude": True, "limit": 2},
    )

    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())
    assert (
        search_info["results"][0]["title"]
        == 'Naruto: Shippuuden - Shippuu! "Konoha Gakuen" Den'
    )
    assert (
        search_info["results"][1]["title"] == "Narutaru: Mukuro Naru Hoshi Tama Taru Ko"
    )
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-season-success.yaml")
async def test_season_success(season_keys, seasonal_anime_keys, aio_jikan):
    season_info = await aio_jikan.season(year=YEAR, season=SEASON)

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())
    for anime in season_info["anime"]:
        assert seasonal_anime_keys.issubset(anime.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-season-archive-success.yaml")
async def test_season_archive_success(
    season_archive_keys, archived_years_keys, aio_jikan
):
    season_archive_info = await aio_jikan.season_archive()

    assert isinstance(season_archive_info, dict)
    assert season_archive_keys.issubset(season_archive_info.keys())
    for year_info in season_archive_info["archive"]:
        assert archived_years_keys.issubset(year_info.keys())
        assert isinstance(year_info["year"], int)
        assert isinstance(year_info["seasons"], list)
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-season-later-success.yaml")
async def test_season_later_success(season_keys, seasonal_anime_keys, aio_jikan):
    season_later_info = await aio_jikan.season_later()

    assert isinstance(season_later_info, dict)
    assert season_keys.issubset(season_later_info.keys())
    for anime in season_later_info["anime"]:
        assert seasonal_anime_keys.issubset(anime.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-schedule-success.yaml")
async def test_schedule_success(schedule_keys, subset_anime_keys, aio_jikan):
    schedule_info = await aio_jikan.schedule(day=DAY)

    assert isinstance(schedule_info, dict)
    assert schedule_keys.issubset(schedule_info.keys())
    assert DAY.lower() in schedule_info
    for anime in schedule_info[DAY]:
        assert subset_anime_keys.issubset(anime.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-top-success.yaml")
async def test_top_success(top_keys, top_anime_keys, aio_jikan):
    top_info = await aio_jikan.top(type=TYPE, page=1, subtype=SUBTYPE)

    assert isinstance(top_info, dict)
    assert top_keys.issubset(top_info.keys())
    for anime in top_info["top"]:
        assert top_anime_keys.issubset(anime.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-genre-success.yaml")
async def test_genre_success(genre_keys, subset_anime_keys, aio_jikan):
    genre_info = await aio_jikan.genre(type=TYPE, genre_id=GENRE)

    assert isinstance(genre_info, dict)
    assert genre_keys.issubset(genre_info.keys())
    for anime in genre_info["anime"]:
        assert subset_anime_keys.issubset(anime.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-producer-success.yaml")
async def test_producer_success(producer_keys, subset_anime_keys, aio_jikan):
    producer_info = await aio_jikan.producer(producer_id=PRODUCER)

    assert isinstance(producer_info, dict)
    assert producer_keys.issubset(producer_info.keys())
    for anime in producer_info["anime"]:
        assert subset_anime_keys.issubset(anime.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-magazine-success.yaml")
async def test_magazine_success(magazine_keys, magazine_manga_keys, aio_jikan):
    magazine_info = await aio_jikan.magazine(magazine_id=MAGAZINE)

    assert isinstance(magazine_info, dict)
    assert magazine_keys.issubset(magazine_info.keys())
    for manga in magazine_info["manga"]:
        assert magazine_manga_keys.issubset(manga.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-user-success.yaml")
async def test_user_success(user_keys, aio_jikan):
    user_info = await aio_jikan.user(username=USERNAME)

    assert isinstance(user_info, dict)
    assert user_info["username"] == "Nekomata1037"
    assert user_info["gender"] == "Male"
    assert user_keys.issubset(user_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-animelist-success.yaml")
async def test_animelist_success(animelist_keys, aio_jikan):
    animelist_info = await aio_jikan.user(
        username=USERNAME,
        request="animelist",
        argument="all",
        parameters={"search": "fate"},
    )

    assert isinstance(animelist_info, dict)
    assert animelist_keys.issubset(animelist_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-club-success.yaml")
async def test_club_success(club_keys, aio_jikan):
    club_info = await aio_jikan.club(CLUB_ID)

    assert isinstance(club_info, dict)
    assert club_info["title"] == "Fantasy Anime League"
    assert club_keys.issubset(club_info.keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-meta-success.yaml")
async def test_meta_success(aio_jikan):
    meta_info = await aio_jikan.meta(request="requests", type="anime", period="today")

    assert isinstance(meta_info, dict)
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-anime-failure.yaml")
async def test_anime_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.anime(-1)
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-manga-failure.yaml")
async def test_manga_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.manga(-1)
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-character-failure.yaml")
async def test_character_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.character(-1)
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-season-failure.yaml")
async def test_season_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.season(year=-1, season=SEASON)
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-club-failure.yaml")
async def test_club_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.club(-1)
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-user-list-failure.yaml")
async def test_user_list_failure(aio_jikan):
    with pytest.raises(DeprecatedEndpoint):
        await aio_jikan.user_list(1)
    await aio_jikan.close()


async def test_empty_response_json(aio_jikan, response_mock):
    with pytest.raises(APIException):
        await aio_jikan._wrap_response(response_mock, url="")
    await aio_jikan.close()
