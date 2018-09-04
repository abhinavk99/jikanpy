import pytest
import vcr

from jikanpy.jikan import Jikan
from jikanpy.exceptions import APIException, ClientException

from constants import *


@pytest.fixture
def anime_keys():
    return {'request_hash', 'request_cached', 'request_cache_expiry', 'mal_id',
            'url', 'image_url', 'trailer_url', 'title', 'title_english',
            'title_japanese', 'title_synonyms', 'type', 'source', 'episodes',
            'status', 'airing', 'aired', 'duration', 'rating', 'score',
            'scored_by', 'rank', 'popularity', 'members', 'favorites',
            'synopsis', 'background', 'premiered', 'broadcast', 'related',
            'producers', 'licensors', 'studios', 'genres', 'opening_themes',
            'ending_themes'}


@pytest.fixture
def manga_keys():
    return {'request_hash', 'request_cached', 'request_cache_expiry', 'mal_id',
            'url', 'title', 'title_english', 'title_synonyms', 'title_japanese',
            'status', 'image_url', 'type', 'volumes', 'chapters', 'publishing',
            'published', 'rank', 'score', 'scored_by', 'popularity', 'members',
            'favorites', 'synopsis', 'background', 'related', 'genres',
            'authors', 'serializations'}


@pytest.fixture
def character_keys():
    return {'request_hash', 'request_cached', 'request_cache_expiry', 'mal_id',
            'url', 'name', 'name_kanji', 'nicknames', 'about',
            'member_favorites', 'image_url', 'animeography', 'mangaography',
            'voice_actors'}


@pytest.fixture
def search_keys():
    return {'request_hash', 'request_cached', 'request_cache_expiry', 'results',
            'last_page'}


@pytest.fixture
def season_keys():
    return {'request_hash', 'request_cached', 'request_cache_expiry',
            'season_name', 'season_year', 'anime'}


@pytest.fixture
def seasonal_anime_keys():
    return {'mal_id', 'url', 'title', 'image_url', 'synopsis', 'type',
            'airing_start', 'episodes', 'members', 'genres', 'source',
            'producers', 'score', 'licensors', 'r18', 'kids', 'continuing'}


@pytest.fixture
def schedule_keys():
    return {'request_hash', 'request_cached', 'request_cache_expiry', 'monday'}


@pytest.fixture
def schedule_anime_keys():
    return {'mal_id', 'url', 'title', 'image_url', 'synopsis', 'type',
            'airing_start', 'episodes', 'members', 'genres', 'source',
            'producers', 'score', 'licensors', 'r18', 'kids'}


@pytest.fixture
def top_keys():
    return {'request_hash', 'request_cached', 'request_cache_expiry', 'top'}


@pytest.fixture
def top_anime_keys():
    return {'mal_id', 'rank', 'url', 'image_url', 'title', 'type', 'score',
            'members', 'start_date', 'end_date', 'episodes'}


@pytest.fixture
def jikan():
    return Jikan()


@vcr.use_cassette('tests/vcr_cassettes/anime-success.yaml')
def test_anime_success(anime_keys, jikan):
    anime_info = jikan.anime(MUSHISHI_ID)

    assert isinstance(anime_info, dict)
    assert anime_info['title'] == 'Mushishi'
    assert anime_keys.issubset(anime_info.keys())


@vcr.use_cassette('tests/vcr_cassettes/manga-success.yaml')
def test_manga_success(manga_keys, jikan):
    manga_info = jikan.manga(FULLMETAL_ID)

    assert isinstance(manga_info, dict)
    assert manga_info['title'] == 'Fullmetal Alchemist'
    assert manga_keys.issubset(manga_info.keys())


@vcr.use_cassette('tests/vcr_cassettes/character-success.yaml')
def test_character_success(character_keys, jikan):
    character_info = jikan.character(GINKO_ID)

    assert isinstance(character_info, dict)
    assert character_info['name'] == 'Ginko'
    assert character_keys.issubset(character_info.keys())


@vcr.use_cassette('tests/vcr_cassettes/search-success.yaml')
def test_search_success(search_keys, jikan):
    search_info = jikan.search(search_type='anime', query='naruto')

    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())


@vcr.use_cassette('tests/vcr_cassettes/season-success.yaml')
def test_season_success(season_keys, seasonal_anime_keys, jikan):
    season_info = jikan.season(year=YEAR, season=SEASON)

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())
    for anime in season_info['anime']:
        assert seasonal_anime_keys.issubset(anime.keys())


@vcr.use_cassette('tests/vcr_cassettes/schedule-success.yaml')
def test_schedule_success(schedule_keys, schedule_anime_keys, jikan):
    schedule_info = jikan.schedule(day=DAY)

    assert isinstance(schedule_info, dict)
    assert schedule_keys.issubset(schedule_info.keys())
    assert DAY.lower() in schedule_info
    for anime in schedule_info[DAY]:
        assert schedule_anime_keys.issubset(anime.keys())


@vcr.use_cassette('tests/vcr_cassettes/top-success.yaml')
def test_top_success(top_keys, top_anime_keys, jikan):
    top_info = jikan.top(type=TYPE)

    assert isinstance(top_info, dict)
    assert top_keys.issubset(top_info.keys())
    for anime in top_info['top']:
        assert top_anime_keys.issubset(anime.keys())


@vcr.use_cassette('tests/vcr_cassettes/meta-success.yaml')
def test_meta_success(jikan):
    meta_info = jikan.meta(request='requests', type='anime', period='today')

    assert isinstance(meta_info, dict)


@vcr.use_cassette('tests/vcr_cassettes/anime-failure.yaml')
def test_anime_failure(jikan):
    with pytest.raises(APIException):
        jikan.anime(-1)


@vcr.use_cassette('tests/vcr_cassettes/manga-failure.yaml')
def test_manga_failure(jikan):
    with pytest.raises(APIException):
        jikan.manga(-1)


@vcr.use_cassette('tests/vcr_cassettes/character-failure.yaml')
def test_character_failure(jikan):
    with pytest.raises(APIException):
        jikan.character(-1)


@vcr.use_cassette('tests/vcr_cassettes/season-failure.yaml')
def test_season_failure(jikan):
    with pytest.raises(APIException):
        jikan.season(year=-1, season=SEASON)


@vcr.use_cassette('tests/vcr_cassettes/schedule-failure.yaml')
def test_schedule_failure(jikan):
    with pytest.raises(ClientException):
        jikan.schedule(day='x')


@vcr.use_cassette('tests/vcr_cassettes/top-failure.yaml')
def test_top_failure(jikan):
    with pytest.raises(ClientException):
        jikan.top(type='x')


@vcr.use_cassette('tests/vcr_cassettes/meta-failure.yaml')
def test_meta_failure(jikan):
    with pytest.raises(ClientException):
        jikan.meta(request='x', type='x', period='x')
