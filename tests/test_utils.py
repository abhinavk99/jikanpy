import pytest

from jikanpy import utils


def test_get_url_with_page():
    assert utils.get_url_with_page("url", 2) == "url/2"


def test_get_url_with_page_none_page():
    assert utils.get_url_with_page("url", None) == "url"


def test_get_url_with_page_delimiter():
    assert utils.get_url_with_page("url", 2, "&page=") == "url&page=2"


def test_get_main_url():
    assert (
        utils.get_main_url("url", "anime", 2, extension=None, page=None)
        == "url/anime/2"
    )


def test_get_main_url_with_extension():
    assert (
        utils.get_main_url("url", "manga", 2, extension="characters", page=None)
        == "url/manga/2/characters"
    )


def test_get_main_url_with_extension_and_page():
    assert (
        utils.get_main_url("url", "anime", 2, extension="episodes", page=2)
        == "url/anime/2/episodes/2"
    )


def test_get_main_url_with_no_extension_and_page():
    assert (
        utils.get_main_url("url", "manga", 2, extension=None, page=2) == "url/manga/2"
    )


def test_get_creator_url():
    assert utils.get_creator_url("url", "producer", 2, page=None) == "url/producer/2"


def test_get_creator_url_with_page():
    assert utils.get_creator_url("url", "producer", 2, page=2) == "url/producer/2/2"


def test_get_search_url():
    assert (
        utils.get_search_url("url", "anime", "jojo", page=None, parameters=None)
        == "url/search/anime?q=jojo"
    )


def test_get_search_url_with_page():
    assert (
        utils.get_search_url("url", "anime", "jojo", page=2, parameters=None)
        == "url/search/anime?q=jojo&page=2"
    )


def test_get_search_url_with_parameters():
    assert (
        utils.get_search_url(
            "url", "anime", "jojo", page=None, parameters={"a": "x", "b": "y"}
        )
        == "url/search/anime?q=jojo&a=x&b=y"
    )


def test_get_search_url_with_page_and_parameters():
    assert (
        utils.get_search_url(
            "url", "anime", "jojo", page=2, parameters={"a": "x", "b": "y"}
        )
        == "url/search/anime?q=jojo&page=2&a=x&b=y"
    )


def test_get_season_url():
    assert utils.get_season_url("url", 2020, "Spring") == "url/season/2020/spring"


def test_get_schedule_url():
    assert utils.get_schedule_url("url", day=None) == "url/schedule"


def test_get_schedule_url_with_day():
    assert utils.get_schedule_url("url", "Tuesday") == "url/schedule/tuesday"


def test_get_season_archive_url():
    assert utils.get_season_archive_url("url") == "url/season/archive"


def test_get_season_later_url():
    assert utils.get_season_later_url("url") == "url/season/later"


def test_get_top_url():
    assert utils.get_top_url("url", "Anime", page=None, subtype=None) == "url/top/anime"


def test_get_top_url_with_page():
    assert utils.get_top_url("url", "Anime", page=2, subtype=None) == "url/top/anime/2"


def test_get_top_url_with_page_and_subtype():
    assert (
        utils.get_top_url("url", "Anime", page=2, subtype="upcoming")
        == "url/top/anime/2/upcoming"
    )


def test_get_genre_url():
    assert utils.get_genre_url("url", "Anime", 2, page=None) == "url/genre/anime/2"


def test_get_genre_url_with_page():
    assert utils.get_genre_url("url", "Anime", 2, page=2) == "url/genre/anime/2/2"


def test_get_user_url():
    assert (
        utils.get_user_url(
            "url", "Xinil", request=None, argument=None, page=None, parameters=None
        )
        == "url/user/xinil"
    )


def test_get_user_url_with_profile():
    assert (
        utils.get_user_url(
            "url", "Xinil", request="profile", argument=None, page=None, parameters=None
        )
        == "url/user/xinil/profile"
    )


def test_get_user_url_with_anime_history():
    assert (
        utils.get_user_url(
            "url",
            "Xinil",
            request="history",
            argument="anime",
            page=None,
            parameters=None,
        )
        == "url/user/xinil/history/anime"
    )


def test_get_user_url_with_friends_and_page():
    assert (
        utils.get_user_url(
            "url", "Xinil", request="friends", argument=None, page=2, parameters=None
        )
        == "url/user/xinil/friends/2"
    )


def test_get_user_url_with_animelist_and_page_parameter():
    assert (
        utils.get_user_url(
            "url",
            "Xinil",
            request="animelist",
            argument="completed",
            page=None,
            parameters={"page": 2},
        )
        == "url/user/xinil/animelist/completed?page=2"
    )


def test_get_meta_url():
    assert (
        utils.get_meta_url("url", "status", type=None, period=None, offset=None)
        == "url/meta/status"
    )


def test_get_meta_url_with_type_and_no_period():
    assert (
        utils.get_meta_url("url", "requests", type="anime", period=None, offset=None)
        == "url/meta/requests"
    )


def test_get_meta_url_with_no_type_and_period():
    assert (
        utils.get_meta_url("url", "requests", type=None, period="weekly", offset=None)
        == "url/meta/requests"
    )


def test_get_meta_url_with_weekly_anime_requests_and_offset():
    assert (
        utils.get_meta_url("url", "requests", type="anime", period="weekly", offset=2)
        == "url/meta/requests/anime/weekly/2"
    )
