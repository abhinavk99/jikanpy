# type: ignore
# pylint: disable=missing-module-docstring,missing-function-docstring
# pylint: disable=redefined-outer-name,protected-access

import pytest
import vcr

# pylint: disable=import-error
from jikanpy import Jikan, utils, APIException, DeprecatedEndpoint

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


@pytest.fixture
def jikan():
    return Jikan()


def test_strip_base_url():
    temp_jikan = Jikan("http://localhost:8000/v4/")
    assert temp_jikan.base == "http://localhost:8000/v4"

    temp_jikan_2 = Jikan("http://localhost:8000/v4/ ")
    assert temp_jikan_2.base == "http://localhost:8000/v4"


@vcr.use_cassette("tests/vcr_cassettes/wrap-response.yaml")
def test_wrap_response(header_keys, jikan):
    anime_info = jikan.anime(MUSHISHI_ID)
    mushishi_url = utils.get_main_url(
        jikan.base, "anime", MUSHISHI_ID, extension=None, page=None
    )

    assert isinstance(anime_info, dict)
    assert "jikan_url" in anime_info
    assert "headers" in anime_info
    assert isinstance(anime_info["headers"], dict)
    assert mushishi_url == anime_info["jikan_url"]
    # Test against headers mentioned in documentation
    # https://jikan.docs.apiary.io/#introduction/information/caching
    assert header_keys.issubset(anime_info["headers"].keys())


def test_wrap_non_dict_response(jikan, response_non_dict_mock):
    wrapped_response = jikan._wrap_response(response_non_dict_mock, "")

    assert isinstance(wrapped_response, dict)
    assert "data" in wrapped_response
    assert wrapped_response["data"] == response_non_dict_mock.json()


@vcr.use_cassette("tests/vcr_cassettes/anime-success.yaml")
def test_anime_success(anime_keys, jikan):
    anime_info = jikan.anime(MUSHISHI_ID)

    assert isinstance(anime_info, dict)
    assert anime_info["data"]["title"] == "Mushishi"
    assert anime_keys.issubset(anime_info["data"].keys())


@vcr.use_cassette("tests/vcr_cassettes/anime-episodes-success.yaml")
def test_anime_episodes_success(anime_episodes_keys, episode_keys, jikan):
    anime_episodes_info = jikan.anime(MUSHISHI_ID, extension="episodes")

    assert isinstance(anime_episodes_info, dict)
    for episode in anime_episodes_info["data"]:
        assert anime_episodes_keys.issubset(episode.keys())


@vcr.use_cassette("tests/vcr_cassettes/manga-success.yaml")
def test_manga_success(manga_keys, jikan):
    manga_info = jikan.manga(FULLMETAL_ID)

    assert isinstance(manga_info, dict)
    assert manga_info["data"]["title"] == "Fullmetal Alchemist"
    assert manga_keys.issubset(manga_info["data"].keys())


@vcr.use_cassette("tests/vcr_cassettes/character-success.yaml")
def test_character_success(character_keys, jikan):
    character_info = jikan.character(GINKO_ID)

    assert isinstance(character_info, dict)
    assert character_info["data"]["name"] == "Ginko"
    assert character_keys.issubset(character_info["data"].keys())


@vcr.use_cassette("tests/vcr_cassettes/person-success.yaml")
def test_person_success(person_keys, jikan):
    person_info = jikan.people(KANA_HANAZAWA_ID)

    assert isinstance(person_info, dict)
    assert person_info["data"]["name"] == "Kana Hanazawa"
    assert person_keys.issubset(person_info["data"].keys())


@vcr.use_cassette("tests/vcr_cassettes/search-success.yaml")
def test_search_success(search_keys, jikan):
    search_info = jikan.search(
        search_type="anime", query="naruto", parameters={"genre": "1,2", "limit": 10}
    )

    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/search-genre-exclude-success.yaml")
def test_search_genre_exclude_success(search_keys, jikan):
    search_info = jikan.search(
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


@vcr.use_cassette("tests/vcr_cassettes/season-success.yaml")
def test_season_success(season_keys, jikan):
    season_info = jikan.season(year=YEAR, season=SEASON)

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())

@vcr.use_cassette("tests/vcr_cassettes/season-anime-success.yaml")
def test_season_anime_success(season_keys, seasonal_anime_keys, jikan):
    season_info = jikan.season(year=YEAR, season=SEASON)

    assert isinstance(season_info, dict)
    assert seasonal_anime_keys.issubset(season_info["data"][0].keys())


@vcr.use_cassette("tests/vcr_cassettes/season-history-success.yaml")
def test_season_history_success(season_archive_keys, archived_years_keys, jikan):
    season_archive_info = jikan.season_history()

    assert isinstance(season_archive_info, dict)
    assert season_archive_keys.issubset(season_archive_info.keys())
    for year_info in season_archive_info["data"]:
        assert archived_years_keys.issubset(year_info.keys())
        assert isinstance(year_info["year"], int)
        assert isinstance(year_info["seasons"], list)


@vcr.use_cassette("tests/vcr_cassettes/season-upcoming-success.yaml")
def test_season_upcoming_success(season_keys, seasonal_anime_keys, jikan):
    season_later_info = jikan.season_upcoming()

    assert isinstance(season_later_info, dict)
    assert season_keys.issubset(season_later_info.keys())
    for anime in season_later_info["data"]:
        assert seasonal_anime_keys.issubset(anime.keys())

@vcr.use_cassette("tests/vcr_cassettes/current-season-success.yaml")
def test_season_current_success(season_keys, seasonal_anime_keys, jikan):
    season_info = jikan.season()

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())
    for anime in season_info["data"]:
        assert seasonal_anime_keys.issubset(anime.keys())

@vcr.use_cassette("tests/vcr_cassettes/schedule-success.yaml")
def test_schedule_success(schedule_keys, subset_anime_keys, jikan):
    schedule_info = jikan.schedule(day=DAY)

    assert isinstance(schedule_info, dict)
    assert schedule_keys.issubset(schedule_info.keys())
    for anime in schedule_info["data"]:
        assert subset_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/top-success.yaml")
def test_top_success(top_keys, top_anime_keys, jikan):
    top_info = jikan.top(type=TYPE, page=1, parameters={'type': SUBTYPE})

    assert isinstance(top_info, dict)
    assert top_keys.issubset(top_info.keys())
    for anime in top_info["data"]:
        assert top_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/genre-success.yaml")
def test_genre_success(genre_keys, subset_anime_keys, jikan):
    genre_info = jikan.genre(type=TYPE, genre_id=GENRE)

    assert isinstance(genre_info, dict)
    assert genre_keys.issubset(genre_info.keys())
    for anime in genre_info["anime"]:
        assert subset_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/producer-success.yaml")
def test_producer_success(producer_keys, subset_anime_keys, jikan):
    producer_info = jikan.producer(producer_id=PRODUCER)

    assert isinstance(producer_info, dict)
    assert producer_keys.issubset(producer_info.keys())
    for anime in producer_info["anime"]:
        assert subset_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/magazine-success.yaml")
def test_magazine_success(magazine_keys, magazine_manga_keys, jikan):
    magazine_info = jikan.magazine(magazine_id=MAGAZINE)

    assert isinstance(magazine_info, dict)
    assert magazine_keys.issubset(magazine_info.keys())
    for manga in magazine_info["manga"]:
        assert magazine_manga_keys.issubset(manga.keys())


@vcr.use_cassette("tests/vcr_cassettes/user-success.yaml")
def test_user_success(user_keys, jikan):
    user_info = jikan.user(username=USERNAME)

    assert isinstance(user_info, dict)
    assert user_info["username"] == "Nekomata1037"
    assert user_info["gender"] == "Male"
    assert user_keys.issubset(user_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/animelist-success.yaml")
def test_animelist_success(animelist_keys, jikan):
    animelist_info = jikan.user(
        username=USERNAME,
        request="animelist",
        argument="all",
        parameters={"search": "fate"},
    )

    assert isinstance(animelist_info, dict)
    assert animelist_keys.issubset(animelist_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/club-success.yaml")
def test_club_success(club_keys, jikan):
    club_info = jikan.club(CLUB_ID)

    assert isinstance(club_info, dict)
    assert club_info["title"] == "Fantasy Anime League"
    assert club_keys.issubset(club_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/anime-failure.yaml")
def test_anime_failure(jikan):
    with pytest.raises(APIException):
        jikan.anime(-1)


@vcr.use_cassette("tests/vcr_cassettes/manga-failure.yaml")
def test_manga_failure(jikan):
    with pytest.raises(APIException):
        jikan.manga(-1)


@vcr.use_cassette("tests/vcr_cassettes/character-failure.yaml")
def test_character_failure(jikan):
    with pytest.raises(APIException):
        jikan.character(-1)


@vcr.use_cassette("tests/vcr_cassettes/season-failure.yaml")
def test_season_failure(jikan):
    with pytest.raises(APIException):
        jikan.season(year=-1, season=SEASON)


@vcr.use_cassette("tests/vcr_cassettes/club-failure.yaml")
def test_club_failure(jikan):
    with pytest.raises(APIException):
        jikan.club(-1)


@vcr.use_cassette("tests/vcr_cassettes/user-list-failure.yaml")
def test_user_list_failure(jikan):
    with pytest.raises(DeprecatedEndpoint):
        jikan.user_list(1)


@pytest.mark.parametrize("response_mock", (True, False), indirect=True)
def test_empty_response_json(jikan, response_mock):
    with pytest.raises(APIException) as err_info:
        jikan._wrap_response(response_mock, url=utils.BASE_URL, param=1)

    err = err_info.value
    err_text = response_mock.text
    assert err.status_code == response_mock.status_code
    assert isinstance(err.error_json, dict)
    assert "error" in err.error_json
    assert err.error_json["error"] == err_text
    assert isinstance(err.relevant_params, dict)
    assert "param" in err.relevant_params
    assert err.relevant_params["param"] == 1
    assert (
        str(err) == f"HTTP {response_mock.status_code} - error={err_text} for param=1"
    )
    assert repr(err).startswith(
        f"APIException(status_code={response_mock.status_code}, error_json={{'error': '"
    )
    assert repr(err).endswith("'}, relevant_params={'param': 1})")


def test_season_urls(jikan):
    season_archive_url = utils.get_season_archive_url(jikan.base)
    season_later_url = utils.get_season_later_url(jikan.base)
    assert season_archive_url.endswith("season/archive")
    assert season_later_url.endswith("season/later")
    assert season_archive_url.startswith(jikan.base)
