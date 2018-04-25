import pytest
import vcr

from jikanpy.jikan import Jikan
from jikanpy.exceptions import APIException

MUSHISHI_ID = 457
FULLMETAL_ID = 25
GINKO_ID = 425

@pytest.fixture
def anime_keys():
   return {'request_hash', 'request_cached', 'mal_id', 'link_canonical',
           'title', 'title_english', 'title_japanese', 'title_synonyms',
           'image_url', 'type', 'source', 'episodes', 'status', 'airing',
           'aired_string', 'aired', 'duration', 'rating', 'score', 'scored_by',
           'rank', 'popularity', 'members', 'favorites', 'synopsis',
           'background', 'premiered', 'broadcast', 'related', 'producer',
           'licensor', 'studio', 'genre', 'opening_theme', 'ending_theme'}
    
@pytest.fixture
def manga_keys():
   return {'request_hash', 'request_cached', 'mal_id', 'link_canonical',
           'title', 'title_english', 'title_synonyms', 'title_japanese',
           'status', 'image_url', 'type', 'volumes', 'chapters', 'publishing',
           'published_string', 'published', 'rank', 'score', 'scored_by',
           'popularity', 'members', 'favorites', 'synopsis', 'background',
           'related', 'genre', 'author', 'serialization'}
    
@pytest.fixture
def character_keys():
    return {'request_hash', 'request_cached', 'mal_id', 'link_canonical',
            'name', 'name_kanji', 'nicknames', 'about', 'member_favorites',
            'image_url', 'animeography', 'mangaography', 'voice_actor'}

@pytest.fixture
def search_keys():
    return {'request_hash', 'request_cached', 'result', 'result_last_page'}

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
