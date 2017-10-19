import pytest
import vcr

from jikanpy.jikan import Jikan
from jikanpy.exceptions import APIException

MUSHISHI_ID = 457
FULLMETAL_ID = 25

@pytest.fixture
def anime_keys():
   return {"link-canonical", "synopsis", "title", "image", "title-english",
           "japanese", "type", "episodes", "status", "aired", "premiered",
           "broadcast", "producer", "licensor", "studio", "source", "genre",
           "duration", "rating", "score", "ranked", "popularity", "members",
           "favorites", "background", "related", "opening-theme", "ending-theme"}
    
@pytest.fixture
def manga_keys():
   return {"link-canonical", "synopsis", "title", "title-english", "japanese",
           "image", "type", "volumes", "chapters", "status", "published",
           "genre", "author", "serialization", "ranked", "score", "popularity",
           "members", "favorites", "background", "related"}

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
    print(manga_keys - manga_info.keys())
    assert manga_keys.issubset(manga_info.keys())

@vcr.use_cassette('tests/vcr_cassettes/anime-failure.yaml')
def test_anime_failure(jikan):
    with pytest.raises(APIException):
        jikan.anime(-1)

@vcr.use_cassette('tests/vcr_cassettes/manga-failure.yaml')
def test_manga_failure(jikan):
    with pytest.raises(APIException):
        jikan.manga(-1)
    