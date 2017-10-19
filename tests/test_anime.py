import pytest
import vcr

from jikanpy.jikan import Jikan
from jikanpy.exceptions import APIException

MUSHISHI_ID = 457

@pytest.fixture
def anime_keys():
   return {"link-canonical", "synopsis", "title", "image", "title-english",
           "japanese", "type", "episodes", "status", "aired", "premiered",
           "broadcast", "producer", "licensor", "studio", "source", "genre",
           "duration", "rating", "score", "ranked", "popularity", "members",
           "favorites", "background", "related", "opening-theme", "ending-theme"}

@pytest.fixture
def jikan():
    return Jikan()

@vcr.use_cassette('tests/vcr_cassettes/anime-success.yaml')
def test_anime_success(anime_keys, jikan):
    anime_info = jikan.anime(MUSHISHI_ID)
    
    assert isinstance(anime_info, dict)
    assert anime_info['title'] == 'Mushishi'
    assert anime_keys.issubset(anime_info.keys())

@vcr.use_cassette('tests/vcr_cassettes/anime-failure.yaml')
def test_anime_failure(anime_keys, jikan):
    with pytest.raises(APIException):
        anime_info = jikan.anime(-1)
    