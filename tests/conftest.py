import pytest

import json


@pytest.fixture
def response_mock():
    class ResponseMock:
        def __init__(self):
            self.status = 403
            self.status_code = 403
            # simulate a banned user
            self.text = """<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.15.5 (Ubuntu)</center>
</body>
</html>
"""

        def json(self):
            raise json.decoder.JSONDecodeError("Failed", "", 0)

    return ResponseMock()


@pytest.fixture
def anime_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_id",
        "url",
        "image_url",
        "trailer_url",
        "title",
        "title_english",
        "title_japanese",
        "title_synonyms",
        "type",
        "source",
        "episodes",
        "status",
        "airing",
        "aired",
        "duration",
        "rating",
        "score",
        "scored_by",
        "rank",
        "popularity",
        "members",
        "favorites",
        "synopsis",
        "background",
        "premiered",
        "broadcast",
        "related",
        "producers",
        "licensors",
        "studios",
        "genres",
        "opening_themes",
        "ending_themes",
    }


@pytest.fixture
def anime_episodes_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "episodes_last_page",
        "episodes",
    }


@pytest.fixture
def episode_keys():
    return {
        "episode_id",
        "title",
        "title_japanese",
        "title_romanji",
        "aired",
        "filler",
        "recap",
        "video_url",
        "forum_url",
    }


@pytest.fixture
def manga_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_id",
        "url",
        "title",
        "title_english",
        "title_synonyms",
        "title_japanese",
        "status",
        "image_url",
        "type",
        "volumes",
        "chapters",
        "publishing",
        "published",
        "rank",
        "score",
        "scored_by",
        "popularity",
        "members",
        "favorites",
        "synopsis",
        "background",
        "related",
        "genres",
        "authors",
        "serializations",
    }


@pytest.fixture
def character_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_id",
        "url",
        "name",
        "name_kanji",
        "nicknames",
        "about",
        "member_favorites",
        "image_url",
        "animeography",
        "mangaography",
        "voice_actors",
    }


@pytest.fixture
def person_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_id",
        "url",
        "image_url",
        "website_url",
        "name",
        "given_name",
        "family_name",
        "alternate_names",
        "birthday",
        "member_favorites",
        "about",
        "voice_acting_roles",
        "anime_staff_positions",
        "published_manga",
    }


@pytest.fixture
def search_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "results",
        "last_page",
    }


@pytest.fixture
def season_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "season_name",
        "season_year",
        "anime",
    }


@pytest.fixture
def seasonal_anime_keys():
    return {
        "mal_id",
        "url",
        "title",
        "image_url",
        "synopsis",
        "type",
        "airing_start",
        "episodes",
        "members",
        "genres",
        "source",
        "producers",
        "score",
        "licensors",
        "r18",
        "kids",
        "continuing",
    }


@pytest.fixture
def season_archive_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "archive"}


@pytest.fixture
def archived_years_keys():
    return {"year", "seasons"}


@pytest.fixture
def schedule_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "monday"}


@pytest.fixture
def top_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "top"}


@pytest.fixture
def top_anime_keys():
    return {
        "mal_id",
        "rank",
        "url",
        "image_url",
        "title",
        "type",
        "score",
        "members",
        "start_date",
        "end_date",
        "episodes",
    }


@pytest.fixture
def genre_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_url",
        "item_count",
        "anime",
    }


@pytest.fixture
def producer_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "meta", "anime"}


@pytest.fixture
def subset_anime_keys():
    return {
        "mal_id",
        "url",
        "title",
        "image_url",
        "synopsis",
        "type",
        "airing_start",
        "episodes",
        "members",
        "genres",
        "source",
        "producers",
        "score",
        "licensors",
        "r18",
        "kids",
    }


@pytest.fixture
def magazine_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "meta", "manga"}


@pytest.fixture
def magazine_manga_keys():
    return {
        "mal_id",
        "url",
        "title",
        "image_url",
        "synopsis",
        "type",
        "publishing_start",
        "volumes",
        "members",
        "genres",
        "authors",
        "score",
        "serialization",
    }


@pytest.fixture
def user_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "username",
        "url",
        "image_url",
        "last_online",
        "gender",
        "birthday",
        "location",
        "joined",
        "anime_stats",
        "manga_stats",
        "favorites",
        "about",
    }


@pytest.fixture
def animelist_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "anime"}


@pytest.fixture
def club_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_id",
        "url",
        "image_url",
        "title",
        "members_count",
        "pictures_count",
        "category",
        "created",
        "type",
        "staff",
        "anime_relations",
        "manga_relations",
        "character_relations",
    }


@pytest.fixture
def header_keys():
    return {
        "X-Cache-Status",
        "X-Request-Hash",
        "X-Request-Cached",
        "X-Request-Cache-Ttl",
        "ETag",
    }
