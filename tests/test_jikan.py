import pytest
import vcr

from jikanpy.jikan import Jikan
from jikanpy.exceptions import APIException

MUSHISHI_ID = 457
FULLMETAL_ID = 25
GINKO_ID = 425

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
def character_keys():
    return {"animeography", "mangaography", "member-favorites", "name",
            "name-japanese", "about", "voice-actors"}

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

