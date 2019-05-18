import pytest
import vcr

from jikanpy import Jikan
from jikanpy import APIException, ClientException, DeprecatedEndpoint

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


@vcr.use_cassette("tests/vcr_cassettes/anime-success.yaml")
def test_anime_success(anime_keys, jikan):
    anime_info = jikan.anime(MUSHISHI_ID)

    assert isinstance(anime_info, dict)
    assert anime_info["title"] == "Mushishi"
    assert anime_keys.issubset(anime_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/anime-episodes-success.yaml")
def test_anime_episodes_success(anime_episodes_keys, episode_keys, jikan):
    anime_episodes_info = jikan.anime(MUSHISHI_ID, extension="episodes", page=1)

    assert isinstance(anime_episodes_info, dict)
    assert isinstance(anime_episodes_info["episodes"], list)
    for episode in anime_episodes_info["episodes"]:
        assert episode_keys.issubset(episode.keys())
    assert anime_episodes_keys.issubset(anime_episodes_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/manga-success.yaml")
def test_manga_success(manga_keys, jikan):
    manga_info = jikan.manga(FULLMETAL_ID)

    assert isinstance(manga_info, dict)
    assert manga_info["title"] == "Fullmetal Alchemist"
    assert manga_keys.issubset(manga_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/character-success.yaml")
def test_character_success(character_keys, jikan):
    character_info = jikan.character(GINKO_ID)

    assert isinstance(character_info, dict)
    assert character_info["name"] == "Ginko"
    assert character_keys.issubset(character_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/person-success.yaml")
def test_person_success(person_keys, jikan):
    person_info = jikan.person(KANA_HANAZAWA_ID)

    assert isinstance(person_info, dict)
    assert person_info["name"] == "Kana Hanazawa"
    assert person_keys.issubset(person_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/search-success.yaml")
def test_search_success(search_keys, jikan):
    search_info = jikan.search(
        search_type="anime", query="naruto", parameters={"genre": 1}
    )

    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/season-success.yaml")
def test_season_success(season_keys, seasonal_anime_keys, jikan):
    season_info = jikan.season(year=YEAR, season=SEASON)

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())
    for anime in season_info["anime"]:
        assert seasonal_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/season-archive-success.yaml")
def test_season_archive_success(season_archive_keys, archived_years_keys, jikan):
    season_archive_info = jikan.season_archive()

    assert isinstance(season_archive_info, dict)
    assert season_archive_keys.issubset(season_archive_info.keys())
    for year_info in season_archive_info["archive"]:
        assert archived_years_keys.issubset(year_info.keys())
        assert isinstance(year_info["year"], int)
        assert isinstance(year_info["seasons"], list)


@vcr.use_cassette("tests/vcr_cassettes/season-later-success.yaml")
def test_season_later_success(season_keys, seasonal_anime_keys, jikan):
    season_later_info = jikan.season_later()

    assert isinstance(season_later_info, dict)
    assert season_keys.issubset(season_later_info.keys())
    for anime in season_later_info["anime"]:
        assert seasonal_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/schedule-success.yaml")
def test_schedule_success(schedule_keys, subset_anime_keys, jikan):
    schedule_info = jikan.schedule(day=DAY)

    assert isinstance(schedule_info, dict)
    assert schedule_keys.issubset(schedule_info.keys())
    assert DAY.lower() in schedule_info
    for anime in schedule_info[DAY]:
        assert subset_anime_keys.issubset(anime.keys())


@vcr.use_cassette("tests/vcr_cassettes/top-success.yaml")
def test_top_success(top_keys, top_anime_keys, jikan):
    top_info = jikan.top(type=TYPE, page=1, subtype=SUBTYPE)

    assert isinstance(top_info, dict)
    assert top_keys.issubset(top_info.keys())
    for anime in top_info["top"]:
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
    animelist_info = jikan.user(username=USERNAME, request="animelist", argument="all")

    assert isinstance(animelist_info, dict)
    assert animelist_keys.issubset(animelist_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/club-success.yaml")
def test_club_success(club_keys, jikan):
    club_info = jikan.club(CLUB_ID)

    assert isinstance(club_info, dict)
    assert club_info["title"] == "Fantasy Anime League"
    assert club_keys.issubset(club_info.keys())


@vcr.use_cassette("tests/vcr_cassettes/meta-success.yaml")
def test_meta_success(jikan):
    meta_info = jikan.meta(request="requests", type="anime", period="today")

    assert isinstance(meta_info, dict)


@vcr.use_cassette("tests/vcr_cassettes/anime-failure.yaml")
def test_anime_failure(jikan):
    with pytest.raises(APIException):
        jikan.anime(-1)


@vcr.use_cassette("tests/vcr_cassettes/anime-extension-failure.yaml")
def test_anime_extension_failure(jikan):
    with pytest.raises(ClientException):
        jikan.anime(MUSHISHI_ID, extension="x")


@vcr.use_cassette("tests/vcr_cassettes/manga-failure.yaml")
def test_manga_failure(jikan):
    with pytest.raises(APIException):
        jikan.manga(-1)


@vcr.use_cassette("tests/vcr_cassettes/character-failure.yaml")
def test_character_failure(jikan):
    with pytest.raises(APIException):
        jikan.character(-1)


@vcr.use_cassette("tests/vcr_cassettes/search-key-failure.yaml")
def test_search_key_failure(jikan):
    with pytest.raises(ClientException):
        jikan.search(search_type="anime", query="naruto", parameters={"x": "tv"})


@vcr.use_cassette("tests/vcr_cassettes/search-value-failure.yaml")
def test_search_value_failure(jikan):
    with pytest.raises(ClientException):
        jikan.search(search_type="anime", query="naruto", parameters={"type": "x"})


@vcr.use_cassette("tests/vcr_cassettes/season-failure.yaml")
def test_season_failure(jikan):
    with pytest.raises(APIException):
        jikan.season(year=-1, season=SEASON)


@vcr.use_cassette("tests/vcr_cassettes/season-client-failure.yaml")
def test_season_client_failure(jikan):
    with pytest.raises(ClientException):
        jikan.season(year="x", season=SEASON)


@vcr.use_cassette("tests/vcr_cassettes/schedule-failure.yaml")
def test_schedule_failure(jikan):
    with pytest.raises(ClientException):
        jikan.schedule(day="x")


@vcr.use_cassette("tests/vcr_cassettes/top-failure.yaml")
def test_top_failure(jikan):
    with pytest.raises(ClientException):
        jikan.top(type="x")


@vcr.use_cassette("tests/vcr_cassettes/top-subtype-failure.yaml")
def test_top_subtype_failure(jikan):
    with pytest.raises(ClientException):
        jikan.top(type=TYPE, page=1, subtype="x")


@vcr.use_cassette("tests/vcr_cassettes/top-page-failure.yaml")
def test_top_page_failure(jikan):
    with pytest.raises(ClientException):
        jikan.top(type=TYPE, subtype=SUBTYPE)


@vcr.use_cassette("tests/vcr_cassettes/genre-failure.yaml")
def test_genre_failure(jikan):
    with pytest.raises(ClientException):
        jikan.genre(type="x", genre_id=GENRE)


@vcr.use_cassette("tests/vcr_cassettes/genre-id-failure.yaml")
def test_genre_id_failure(jikan):
    with pytest.raises(ClientException):
        jikan.genre(type=TYPE, genre_id="x")


@vcr.use_cassette("tests/vcr_cassettes/producer-failure.yaml")
def test_producer_failure(jikan):
    with pytest.raises(ClientException):
        jikan.producer(producer_id="producer")


@vcr.use_cassette("tests/vcr_cassettes/magazine-failure.yaml")
def test_magazine_failure(jikan):
    with pytest.raises(ClientException):
        jikan.magazine(magazine_id="magazine")


@vcr.use_cassette("tests/vcr_cassettes/user-failure.yaml")
def test_user_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="friends", argument="x")


@vcr.use_cassette("tests/vcr_cassettes/user-request-failure.yaml")
def test_user_request_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="x", argument="x")


@vcr.use_cassette("tests/vcr_cassettes/user-profile-failure.yaml")
def test_user_profile_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="profile", argument="x")


@vcr.use_cassette("tests/vcr_cassettes/user-animelist-failure.yaml")
def test_user_animelist_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="animelist", page=1)


@vcr.use_cassette("tests/vcr_cassettes/user-page-failure.yaml")
def test_user_page_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="animelist", page="x", argument="all")


@vcr.use_cassette("tests/vcr_cassettes/user-history-failure.yaml")
def test_user_history_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="history", argument="x")


@vcr.use_cassette("tests/vcr_cassettes/user-animelist-argument-failure.yaml")
def test_user_animelist_argument_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="animelist", argument="x")


@vcr.use_cassette("tests/vcr_cassettes/user-mangalist-argument-failure.yaml")
def test_user_mangalist_argument_failure(jikan):
    with pytest.raises(ClientException):
        jikan.user(username="user", request="mangalist", argument="x")


@vcr.use_cassette("tests/vcr_cassettes/club-failure.yaml")
def test_club_failure(jikan):
    with pytest.raises(APIException):
        jikan.club(-1)


@vcr.use_cassette("tests/vcr_cassettes/meta-failure.yaml")
def test_meta_failure(jikan):
    with pytest.raises(ClientException):
        jikan.meta(request="x", type="x", period="x")


@vcr.use_cassette("tests/vcr_cassettes/meta-type-failure.yaml")
def test_meta_type_failure(jikan):
    with pytest.raises(ClientException):
        jikan.meta(request="requests", type="x", period="x")


@vcr.use_cassette("tests/vcr_cassettes/meta-period-failure.yaml")
def test_meta_period_failure(jikan):
    with pytest.raises(ClientException):
        jikan.meta(request="requests", type="anime", period="x")


@vcr.use_cassette("tests/vcr_cassettes/meta-status-failure.yaml")
def test_meta_status_failure(jikan):
    with pytest.raises(ClientException):
        jikan.meta(request="status", type="x", period="x")


@vcr.use_cassette("tests/vcr_cassettes/user-list-failure.yaml")
def test_user_list_failure(jikan):
    with pytest.raises(DeprecatedEndpoint):
        jikan.user_list(1)


def test_empty_response_json(jikan, response_mock):
    with pytest.raises(APIException):
        jikan._check_response(response_mock)
