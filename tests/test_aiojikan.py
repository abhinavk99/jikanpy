# type: ignore
# pylint: disable=missing-module-docstring,missing-function-docstring
# pylint: disable=redefined-outer-name,protected-access

import pytest
import vcr

# pylint: disable=import-error
from jikanpy import AioJikan, utils, APIException, DeprecatedEndpoint

# pylint: disable=unused-import
from constants import (  # noqa: F401
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
    async with AioJikan() as temp_aio_jikan:
        assert isinstance(temp_aio_jikan, AioJikan)


async def test_strip_base_url():
    async with AioJikan("http://localhost:8000/v4/") as temp_aio_jikan:
        assert temp_aio_jikan.base == "http://localhost:8000/v4"

    async with AioJikan("http://localhost:8000/v4/ ") as temp_aio_jikan_2:
        assert temp_aio_jikan_2.base == "http://localhost:8000/v4"


@vcr.use_cassette("tests/vcr_cassettes/aio-wrap-response.yaml")
async def test_wrap_response(header_keys,aio_jikan):
    anime_info = await aio_jikan.anime(MUSHISHI_ID)
    mushishi_url = utils.get_main_url(
        aio_jikan.base, "anime", MUSHISHI_ID, extension=None, page=None
    )

    assert isinstance(anime_info, dict)
    assert "jikan_url" in anime_info
    assert "headers" in anime_info
    assert isinstance(anime_info["headers"], dict)
    assert mushishi_url == anime_info["jikan_url"]
    assert header_keys.issubset(anime_info["headers"].keys())
    await aio_jikan.close()


async def test_wrap_non_dict_response(aio_jikan, aio_response_non_dict_mock):
    wrapped_response = await aio_jikan._wrap_response(aio_response_non_dict_mock, "")

    assert isinstance(wrapped_response, dict)
    assert "data" in wrapped_response
    assert wrapped_response["data"] == await aio_response_non_dict_mock.json()
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-anime-success.yaml")
async def test_anime_success(anime_keys, aio_jikan):
    anime_info = await aio_jikan.anime(MUSHISHI_ID)

    assert isinstance(anime_info, dict)
    assert anime_info["data"]["title"] == "Mushishi"
    assert anime_keys.issubset(anime_info["data"].keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-anime-episodes-success.yaml")
async def test_anime_episodes_success(anime_episodes_keys, episode_keys, aio_jikan):
    anime_episodes_info = await aio_jikan.anime(
        MUSHISHI_ID, extension="episodes", page=1
    )

    assert isinstance(anime_episodes_info, dict)
    for episode in anime_episodes_info["data"]:
        assert anime_episodes_keys.issubset(episode.keys())
    await aio_jikan.close()

@vcr.use_cassette("tests/vcr_cassettes/aio-anime-episode-by-id-success.yaml")
def test_anime_episode_by_id_success(episode_keys, aio_jikan):
    anime_episodes_info = await aio_jikan.anime_episode_by_id(anime_id=MUSHISHI_ID, episode_id=1)

    assert isinstance(anime_episodes_info, dict)
    assert episode_keys.issubset(anime_episodes_info['data'].keys())
    await aio_jikan.close()

@vcr.use_cassette("tests/vcr_cassettes/aio-manga-success.yaml")
async def test_manga_success(manga_keys, aio_jikan):
    manga_info = await aio_jikan.manga(FULLMETAL_ID)

    assert isinstance(manga_info, dict)
    assert manga_info["data"]["title"] == "Fullmetal Alchemist"
    assert manga_keys.issubset(manga_info["data"].keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-character-success.yaml")
async def test_character_success(character_keys, aio_jikan):
    character_info = await aio_jikan.character(GINKO_ID)

    assert isinstance(character_info, dict)
    assert character_info["data"]["name"] == "Ginko"
    assert character_keys.issubset(character_info["data"].keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-person-success.yaml")
async def test_person_success(person_keys, aio_jikan):
    person_info = await aio_jikan.person(KANA_HANAZAWA_ID)

    assert isinstance(person_info, dict)
    assert person_info["data"]["name"] == "Kana Hanazawa"
    assert person_keys.issubset(person_info["data"].keys())
    await aio_jikan.close()


@vcr.use_cassette("tests/vcr_cassettes/aio-search-success.yaml")
async def test_search_success(search_keys, aio_jikan):
    search_info = await aio_jikan.search(
        search_type="anime", query="naruto", parameters={"genre": "1,2", "limit": 10}
    )

    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())
    await aio_jikan.close()

@vcr.use_cassette("tests/vcr_cassettes/aio-search-manga-success.yaml")
def test_search_manga_success(search_keys, aio_jikan):
    search_info = await aio_jikan.search(
        search_type="manga", query="jujutsu kaisen", parameters={"limit": 10}
    )
    assert search_info["data"][0]["mal_id"] == 113138
    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())
    await aio_jikan.close()

@vcr.use_cassette("tests/vcr_cassettes/aio-search-light-novel-success.yaml")
def test_search_ln_success(search_keys, aio_jikan):
    search_info = aio_jikan.search(
        search_type="manga", query="mushoku tensei", parameters={"limit": 10, "type":'lightnovel'}
    )
    assert search_info["data"][0]["mal_id"] == 70261
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
        search_info["data"][0]["title"]
        == 'Naruto: Road of Naruto'
    )
    assert (
        search_info["data"][1]["title"] == "Naruto"
    )
    await aio_jikan.close()

@vcr.use_cassette("tests/vcr_cassettes/aio-search-user-success.yaml")
def test_search_user_success(user_keys, aio_jikan):
    search_info = await aio_jikan.search(
        search_type="users", query="Xinil", parameters={"limit": 10}
    )

    assert search_info["data"][5]["username"] == 'Xinil'
    assert isinstance(search_info, dict)
    assert user_keys.issubset(search_info["data"][0].keys())
    await aio_jikan.close()

@vcr.use_cassette("tests/vcr_cassettes/aio-season-success.yaml")
async def test_season_success(season_keys, seasonal_anime_keys, aio_jikan):
    season_info = await aio_jikan.season(year=YEAR, season=SEASON)

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())
    
    await aio_jikan.close()

@vcr.use_cassette("tests/vcr_cassettes/aio-current-season-success.yaml")
async def test_season_current_success(season_keys, seasonal_anime_keys, aio_jikan):
    season_info = await aio_jikan.seasons(extension='now')

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())
    for anime in season_info["data"]:
        assert seasonal_anime_keys.issubset(anime.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-schedule-success.yaml")
async def test_schedule_success(schedule_keys, subset_anime_keys, aio_jikan):
    schedule_info = await aio_jikan.schedules(day=DAY)

    assert isinstance(schedule_info, dict)
    assert schedule_keys.issubset(schedule_info.keys())
    for anime in schedule_info["data"]:
        assert subset_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/aio-top-success.yaml")
async def test_top_success(top_keys, top_anime_keys, aio_jikan):
    top_info = await aio_jikan.top(type=TYPE, page=1, parameters={'type': SUBTYPE})

    assert isinstance(top_info, dict)
    assert top_keys.issubset(top_info.keys())
    for anime in top_info["data"]:
        assert top_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/aio-genre-anime-success.yaml")
async def test_genre_anime_success(genre_keys, aio_jikan):
    genre_info = await aio_jikan.genres(type="anime")

    assert isinstance(genre_info, dict)
    for anime in genre_info["data"]:
        assert genre_keys.issubset(anime.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-genre-manga-success.yaml")
async def test_genre_manga_success(genre_keys, aio_jikan):
    genre_info = await aio_jikan.genres(type="manga")

    assert isinstance(genre_info, dict)
    for anime in genre_info["data"]:
        assert genre_keys.issubset(anime.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-producer-success.yaml")
async def test_producer_success(producer_keys, subset_anime_keys, aio_jikan):
    producer_info = await aio_jikan.producers(id=PRODUCER)

    assert isinstance(producer_info, dict)
    assert producer_keys.issubset(producer_info["data"].keys())


@vcr.use_cassette("tests/vcr_cassettes/aio-magazine-success.yaml")
async def test_magazine_success(magazine_keys, magazine_manga_keys, aio_jikan):
    magazine_info = await aio_jikan.search("magazines",query="young")

    assert isinstance(magazine_info, dict)
    assert magazine_keys.issubset(magazine_info["data"][0].keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-user-success.yaml")
async def test_user_success(user_keys_full, aio_jikan):
    user_info = await aio_jikan.users(username=USERNAME, extension="full")

    assert isinstance(user_info, dict)
    assert user_info["data"]["username"] == "Nekomata1037"
    assert user_info["data"]["gender"] == "Male"
    assert user_keys_full.issubset(user_info["data"].keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-user-friends-success.yaml")
async def test_user_friends_success(user_keys_friends, aio_jikan):
    user_info = await aio_jikan.users(username=USERNAME, extension="friends")

    assert isinstance(user_info, dict)
    assert user_info["data"][0]["user"]["username"] == "purplepinapples"
    assert user_keys_friends.issubset(user_info["data"][0].keys())


@vcr.use_cassette("tests/vcr_cassettes/aio-user-id-success.yaml")
async def test_user_id_success(user_id_keys, aio_jikan):
    user_info = await aio_jikan.user_by_id(user_id=1)

    assert isinstance(user_info, dict)
    assert user_info["data"]["username"] == "Xinil"
    assert user_id_keys.issubset(user_info["data"].keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-club-success.yaml")
async def test_club_success(club_keys, aio_jikan):
    club_info = await aio_jikan.clubs(CLUB_ID)

    assert isinstance(club_info, dict)
    assert club_info["data"]["name"] == "Fantasy Anime League"
    assert club_keys.issubset(club_info["data"].keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-random-anime-success.yaml")
async def test_random_anime_success(anime_keys, aio_jikan):
    anime = await aio_jikan.random(type='anime')

    assert isinstance(anime, dict)
    assert anime_keys.issubset(anime['data'].keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-recommendations-success.yaml")
async def test_recommendations_success(recommendations_keys, aio_jikan):
    recommendations = await aio_jikan.recommendations(type='anime')

    assert isinstance(recommendations, dict)
    for rec in recommendations["data"]:
        assert recommendations_keys.issubset(rec.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-reviews-success.yaml")
async def test_reviews_success(reviews_keys, aio_jikan):
    reviews = await aio_jikan.reviews(type='anime')

    assert isinstance(reviews, dict)
    for rec in reviews["data"]:
        assert reviews_keys.issubset(rec.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-watch-episodes-success.yaml")
async def test_watch_episodes_success(watch_episodes_keys, aio_jikan):
    watch_eps = await aio_jikan.watch(extension='episodes')

    assert isinstance(watch_eps, dict)
    for item in watch_eps["data"]:
        assert watch_episodes_keys.issubset(item.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-watch-episodes-popular-success.yaml")
async def test_watch_episodes_success(watch_episodes_keys, aio_jikan):
    watch_eps = await aio_jikan.watch(extension='episodes/popular')

    assert isinstance(watch_eps, dict)
    for item in watch_eps["data"]:
        assert watch_episodes_keys.issubset(item.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-watch-promos-success.yaml")
async def test_watch_promos_success(watch_promos_keys, aio_jikan):
    promos = await aio_jikan.watch(extension='promos')

    assert isinstance(promos, dict)
    for item in promos["data"]:
        assert watch_promos_keys.issubset(item.keys())

@vcr.use_cassette("tests/vcr_cassettes/aio-watch-promos-popular-success.yaml")
async def test_watch_promos_success(watch_promos_keys, aio_jikan):
    promos = await aio_jikan.watch(extension='promos/popular')

    assert isinstance(promos, dict)
    for item in promos["data"]:
        assert watch_promos_keys.issubset(item.keys())


@vcr.use_cassette("tests/vcr_cassettes/aio-anime-failure.yaml")
async def test_anime_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.anime(-1)


@vcr.use_cassette("tests/vcr_cassettes/aio-manga-failure.yaml")
async def test_manga_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.manga(-1)


@vcr.use_cassette("tests/vcr_cassettes/aio-character-failure.yaml")
async def test_character_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.character(-1)


@vcr.use_cassette("tests/vcr_cassettes/aio-season-failure.yaml")
async def test_season_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.seasons(year=-1, season=SEASON)


@vcr.use_cassette("tests/vcr_cassettes/aio-club-failure.yaml")
async def test_club_failure(aio_jikan):
    with pytest.raises(APIException):
        await aio_jikan.clubs(-1)


@vcr.use_cassette("tests/vcr_cassettes/aio-user-list-failure.yaml")
async def test_user_list_failure(aio_jikan):
    with pytest.raises(DeprecatedEndpoint):
        await aio_jikan.user_list(1)


@pytest.mark.parametrize("aio_response_mock", (True, False), indirect=True)
async def test_empty_response_json(aio_jikan, aio_response_mock):
    with pytest.raises(APIException) as err_info:
        await aio_jikan._wrap_response(aio_response_mock, url=utils.BASE_URL, param=1)

    err = err_info.value
    err_text = aio_response_mock.text
    assert err.status_code == aio_response_mock.status_code
    assert isinstance(err.error_json, dict)
    assert "error" in err.error_json
    assert err.error_json["error"] == err_text
    assert isinstance(err.relevant_params, dict)
    assert "param" in err.relevant_params
    assert err.relevant_params["param"] == 1
    assert (
        str(err) == f"HTTP {aio_response_mock.status_code} - error={err_text} for param=1"
    )
    assert repr(err).startswith(
        f"APIException(status_code={aio_response_mock.status_code}, error_json={{'error': '"
    )
    assert repr(err).endswith("'}, relevant_params={'param': 1})")
