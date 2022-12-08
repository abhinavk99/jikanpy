# type: ignore
# pylint: disable=missing-module-docstring,missing-function-docstring

# pylint: disable=import-error
from jikanpy import utils


def test_get_main_url():
    assert (
        utils.get_main_url(utils.BASE_URL, "anime", 2, extension=None, page=None)
        == "https://api.jikan.moe/v4/anime/2"
    )


def test_get_main_url_with_extension():
    assert (
        utils.get_main_url(
            utils.BASE_URL, "manga", 2, extension="characters", page=None
        )
        == "https://api.jikan.moe/v4/manga/2/characters"
    )


def test_get_main_url_with_extension_and_page():
    assert (
        utils.get_main_url(utils.BASE_URL, "anime", 2, extension="episodes", page=2)
        == "https://api.jikan.moe/v4/anime/2/episodes?page=2"
    )


def test_get_main_url_with_no_extension_and_page():
    assert (
        utils.get_main_url(utils.BASE_URL, "manga", 2, extension=None, page=2)
        == "https://api.jikan.moe/v4/manga/2?page=2"
    )


def test_get_search_url():
    assert (
        utils.get_search_url(
            utils.BASE_URL, "anime", "jojo", page=None, parameters=None
        )
        == "https://api.jikan.moe/v4/anime?q=jojo"
    )


def test_get_search_url_with_page():
    assert (
        utils.get_search_url(utils.BASE_URL, "anime", "jojo", page=2, parameters=None)
        == "https://api.jikan.moe/v4/anime?q=jojo&page=2"
    )


def test_get_search_url_with_parameters():
    assert (
        utils.get_search_url(
            utils.BASE_URL, "anime", "jojo", page=None, parameters={"a": "x", "b": "y"},
        )
        == "https://api.jikan.moe/v4/anime?q=jojo&a=x&b=y"
    )


def test_get_search_url_with_page_and_parameters():
    assert (
        utils.get_search_url(
            utils.BASE_URL, "anime", "jojo", page=2, parameters={"a": "x", "b": "y"},
        )
        == "https://api.jikan.moe/v4/anime?q=jojo&page=2&a=x&b=y"
    )


def test_get_season_url():
    assert (
        utils.get_season_url(utils.BASE_URL, 2020, "Spring")
        == "https://api.jikan.moe/v4/seasons/2020/spring"
    )


def test_get_schedule_url():
    assert (
        utils.get_schedule_url(utils.BASE_URL, day=None)
        == "https://api.jikan.moe/v4/schedules"
    )


def test_get_schedule_url_with_day():
    assert (
        utils.get_schedule_url(utils.BASE_URL, day="Tuesday")
        == "https://api.jikan.moe/v4/schedules?filter=tuesday"
    )


def test_get_season_archive_url():
    assert (
        utils.get_season_url(utils.BASE_URL)
        == "https://api.jikan.moe/v4/seasons"
    )


def test_get_season_upcoming_url():
    assert (
        utils.get_season_url(utils.BASE_URL, extension='upcoming')
        == "https://api.jikan.moe/v4/seasons/upcoming"
    )


def test_get_top_url():
    assert (
        utils.get_top_url(utils.BASE_URL, type="Anime", page=None)
        == "https://api.jikan.moe/v4/top/anime"
    )


def test_get_top_url_with_page():
    assert (
        utils.get_top_url(utils.BASE_URL, "Anime", page=2)
        == "https://api.jikan.moe/v4/top/anime?page=2"
    )


def test_get_top_url_with_page_and_subtype():
    assert (
        utils.get_top_url(utils.BASE_URL, "Anime", page=2, parameters={"filter":"upcoming"})
        == "https://api.jikan.moe/v4/top/anime?page=2&filter=upcoming"
    )


def test_get_genre_url():
    assert (
        utils.get_genre_url(utils.BASE_URL, type="Anime")
        == "https://api.jikan.moe/v4/genres/anime"
    )


def test_get_genre_url_with_page():
    assert (
        utils.get_genre_url(utils.BASE_URL, type="Anime")
        == "https://api.jikan.moe/v4/genres/anime"
    )


def test_get_user_url():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            extension=None,
            page=None,
            parameters=None,
        )
        == "https://api.jikan.moe/v4/users/xinil"
    )


def test_get_user_url_with_profile():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            extension='profile',
            page=None,
            parameters=None,
        )
        == "https://api.jikan.moe/v4/users/xinil/profile"
    )


def test_get_user_url_with_anime_history():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            extension="history",
            page=None,
            parameters={'type':'anime'},
        )
        == "https://api.jikan.moe/v4/users/xinil/history?type=anime"
    )


def test_get_user_url_with_friends_and_page():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            extension="friends",
            page=2,
            parameters=None,
        )
        == "https://api.jikan.moe/v4/users/xinil/friends?page=2"
    )

