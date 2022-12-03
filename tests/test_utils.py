# type: ignore
# pylint: disable=missing-module-docstring,missing-function-docstring

# pylint: disable=import-error
from jikanpy import utils


def test_get_url_with_page():
    assert utils.get_url_with_page(utils.BASE_URL, 2) == "https://api.jikan.moe/v4/2"


def test_get_url_with_page_none_page():
    assert utils.get_url_with_page(utils.BASE_URL, None) == utils.BASE_URL


def test_get_url_with_page_delimiter():
    assert (
        utils.get_url_with_page(utils.BASE_URL, 2, "&page=")
        == "https://api.jikan.moe/v4&page=2"
    )


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
        == "https://api.jikan.moe/v4/anime/2/episodes/2"
    )


def test_get_main_url_with_no_extension_and_page():
    assert (
        utils.get_main_url(utils.BASE_URL, "manga", 2, extension=None, page=2)
        == "https://api.jikan.moe/v4/manga/2"
    )


def test_get_creator_url():
    assert (
        utils.get_creator_url(utils.BASE_URL, "producer", 2, page=None)
        == "https://api.jikan.moe/v4/producer/2"
    )


def test_get_creator_url_with_page():
    assert (
        utils.get_creator_url(utils.BASE_URL, "producer", 2, page=2)
        == "https://api.jikan.moe/v4/producer/2/2"
    )


def test_get_search_url():
    assert (
        utils.get_search_url(
            utils.BASE_URL, "anime", "jojo", page=None, parameters=None
        )
        == "https://api.jikan.moe/v4/search/anime?q=jojo"
    )


def test_get_search_url_with_page():
    assert (
        utils.get_search_url(utils.BASE_URL, "anime", "jojo", page=2, parameters=None)
        == "https://api.jikan.moe/v4/search/anime?q=jojo&page=2"
    )


def test_get_search_url_with_parameters():
    assert (
        utils.get_search_url(
            utils.BASE_URL, "anime", "jojo", page=None, parameters={"a": "x", "b": "y"},
        )
        == "https://api.jikan.moe/v4/search/anime?q=jojo&a=x&b=y"
    )


def test_get_search_url_with_page_and_parameters():
    assert (
        utils.get_search_url(
            utils.BASE_URL, "anime", "jojo", page=2, parameters={"a": "x", "b": "y"},
        )
        == "https://api.jikan.moe/v4/search/anime?q=jojo&page=2&a=x&b=y"
    )


def test_get_season_url():
    assert (
        utils.get_season_url(utils.BASE_URL, 2020, "Spring")
        == "https://api.jikan.moe/v4/season/2020/spring"
    )


def test_get_schedule_url():
    assert (
        utils.get_schedule_url(utils.BASE_URL, day=None)
        == "https://api.jikan.moe/v4/schedule"
    )


def test_get_schedule_url_with_day():
    assert (
        utils.get_schedule_url(utils.BASE_URL, "Tuesday")
        == "https://api.jikan.moe/v4/schedule/tuesday"
    )


def test_get_season_archive_url():
    assert (
        utils.get_season_archive_url(utils.BASE_URL)
        == "https://api.jikan.moe/v4/season/archive"
    )


def test_get_season_later_url():
    assert (
        utils.get_season_later_url(utils.BASE_URL)
        == "https://api.jikan.moe/v4/season/later"
    )


def test_get_top_url():
    assert (
        utils.get_top_url(utils.BASE_URL, "Anime", page=None, subtype=None)
        == "https://api.jikan.moe/v4/top/anime"
    )


def test_get_top_url_with_page():
    assert (
        utils.get_top_url(utils.BASE_URL, "Anime", page=2, subtype=None)
        == "https://api.jikan.moe/v4/top/anime/2"
    )


def test_get_top_url_with_page_and_subtype():
    assert (
        utils.get_top_url(utils.BASE_URL, "Anime", page=2, subtype="upcoming")
        == "https://api.jikan.moe/v4/top/anime/2/upcoming"
    )


def test_get_genre_url():
    assert (
        utils.get_genre_url(utils.BASE_URL, "Anime", 2, page=None)
        == "https://api.jikan.moe/v4/genre/anime/2"
    )


def test_get_genre_url_with_page():
    assert (
        utils.get_genre_url(utils.BASE_URL, "Anime", 2, page=2)
        == "https://api.jikan.moe/v4/genre/anime/2/2"
    )


def test_get_user_url():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            request=None,
            argument=None,
            page=None,
            parameters=None,
        )
        == "https://api.jikan.moe/v4/user/xinil"
    )


def test_get_user_url_with_profile():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            request="profile",
            argument=None,
            page=None,
            parameters=None,
        )
        == "https://api.jikan.moe/v4/user/xinil/profile"
    )


def test_get_user_url_with_anime_history():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            request="history",
            argument="anime",
            page=None,
            parameters=None,
        )
        == "https://api.jikan.moe/v4/user/xinil/history/anime"
    )


def test_get_user_url_with_friends_and_page():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            request="friends",
            argument=None,
            page=2,
            parameters=None,
        )
        == "https://api.jikan.moe/v4/user/xinil/friends/2"
    )


def test_get_user_url_with_animelist_and_page_parameter():
    assert (
        utils.get_user_url(
            utils.BASE_URL,
            "Xinil",
            request="animelist",
            argument="completed",
            page=None,
            parameters={"page": 2},
        )
        == "https://api.jikan.moe/v4/user/xinil/animelist/completed?page=2"
    )

