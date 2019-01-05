import pytest

import asyncio

from jikanpy.aiojikan import AioJikan
from jikanpy.exceptions import APIException, ClientException

from constants import *
from fixtures import *


@pytest.fixture
def aio_jikan(event_loop):
    return AioJikan(loop=event_loop)


@pytest.mark.asyncio
def test_anime_success(anime_keys, aio_jikan):
    anime_info = yield from aio_jikan.anime(MUSHISHI_ID)

    assert isinstance(anime_info, dict)
    assert anime_info['title'] == 'Mushishi'
    assert anime_keys.issubset(anime_info.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_manga_success(manga_keys, aio_jikan):
    manga_info = yield from aio_jikan.manga(FULLMETAL_ID)

    assert isinstance(manga_info, dict)
    assert manga_info['title'] == 'Fullmetal Alchemist'
    assert manga_keys.issubset(manga_info.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_character_success(character_keys, aio_jikan):
    character_info = yield from aio_jikan.character(GINKO_ID)

    assert isinstance(character_info, dict)
    assert character_info['name'] == 'Ginko'
    assert character_keys.issubset(character_info.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_person_success(person_keys, aio_jikan):
    person_info = yield from aio_jikan.person(KANA_HANAZAWA_ID)

    assert isinstance(person_info, dict)
    assert person_info['name'] == 'Kana Hanazawa'
    assert person_keys.issubset(person_info.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_search_success(search_keys, aio_jikan):
    search_info = yield from aio_jikan.search(search_type='anime', query='naruto')

    assert isinstance(search_info, dict)
    assert search_keys.issubset(search_info.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_season_success(season_keys, seasonal_anime_keys, aio_jikan):
    season_info = yield from aio_jikan.season(year=YEAR, season=SEASON)

    assert isinstance(season_info, dict)
    assert season_keys.issubset(season_info.keys())
    for anime in season_info['anime']:
        assert seasonal_anime_keys.issubset(anime.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_season_archive_success(season_archive_keys, archived_years_keys, aio_jikan):
    season_archive_info = yield from aio_jikan.season_archive()

    assert isinstance(season_archive_info, dict)
    assert season_archive_keys.issubset(season_archive_info.keys())
    for year_info in season_archive_info['archive']:
        assert archived_years_keys.issubset(year_info.keys())
        assert isinstance(year_info['year'], int)
        assert isinstance(year_info['seasons'], list)
    aio_jikan.close()


@pytest.mark.asyncio
def test_season_later_success(season_keys, seasonal_anime_keys, aio_jikan):
    season_later_info = yield from aio_jikan.season_later()

    assert isinstance(season_later_info, dict)
    assert season_keys.issubset(season_later_info.keys())
    for anime in season_later_info['anime']:
        assert seasonal_anime_keys.issubset(anime.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_schedule_success(schedule_keys, subset_anime_keys, aio_jikan):
    schedule_info = yield from aio_jikan.schedule(day=DAY)

    assert isinstance(schedule_info, dict)
    assert schedule_keys.issubset(schedule_info.keys())
    assert DAY.lower() in schedule_info
    for anime in schedule_info[DAY]:
        assert subset_anime_keys.issubset(anime.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_top_success(top_keys, top_anime_keys, aio_jikan):
    top_info = yield from aio_jikan.top(type=TYPE)

    assert isinstance(top_info, dict)
    assert top_keys.issubset(top_info.keys())
    for anime in top_info['top']:
        assert top_anime_keys.issubset(anime.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_genre_success(genre_keys, subset_anime_keys, aio_jikan):
    genre_info = yield from aio_jikan.genre(type=TYPE, genre_id=GENRE)

    assert isinstance(genre_info, dict)
    assert genre_keys.issubset(genre_info.keys())
    for anime in genre_info['anime']:
        assert subset_anime_keys.issubset(anime.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_producer_success(producer_keys, subset_anime_keys, aio_jikan):
    producer_info = yield from aio_jikan.producer(producer_id=PRODUCER)

    assert isinstance(producer_info, dict)
    assert producer_keys.issubset(producer_info.keys())
    for anime in producer_info['anime']:
        assert subset_anime_keys.issubset(anime.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_magazine_success(magazine_keys, magazine_manga_keys, aio_jikan):
    magazine_info = yield from aio_jikan.magazine(magazine_id=MAGAZINE)

    assert isinstance(magazine_info, dict)
    assert magazine_keys.issubset(magazine_info.keys())
    for manga in magazine_info['manga']:
        assert magazine_manga_keys.issubset(manga.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_user_success(user_keys, aio_jikan):
    user_info = yield from aio_jikan.user(username=USERNAME)

    assert isinstance(user_info, dict)
    assert user_info['username'] == 'Nekomata1037'
    assert user_info['gender'] == 'Male'
    assert user_keys.issubset(user_info.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_club_success(club_keys, aio_jikan):
    club_info = yield from aio_jikan.club(CLUB_ID)

    assert isinstance(club_info, dict)
    assert club_info['title'] == 'Fantasy Anime League'
    assert club_keys.issubset(club_info.keys())
    aio_jikan.close()


@pytest.mark.asyncio
def test_meta_success(aio_jikan):
    meta_info = yield from aio_jikan.meta(request='requests', type='anime', period='today')

    assert isinstance(meta_info, dict)
    aio_jikan.close()


@pytest.mark.asyncio
def test_anime_failure(aio_jikan):
    with pytest.raises(APIException):
        yield from aio_jikan.anime(-1)
    aio_jikan.close()


@pytest.mark.asyncio
def test_manga_failure(aio_jikan):
    with pytest.raises(APIException):
        yield from aio_jikan.manga(-1)
    aio_jikan.close()


@pytest.mark.asyncio
def test_character_failure(aio_jikan):
    with pytest.raises(APIException):
        yield from aio_jikan.character(-1)
    aio_jikan.close()


@pytest.mark.asyncio
def test_season_failure(aio_jikan):
    with pytest.raises(APIException):
        yield from aio_jikan.season(year=-1, season=SEASON)
    aio_jikan.close()


@pytest.mark.asyncio
def test_schedule_failure(aio_jikan):
    with pytest.raises(ClientException):
        yield from aio_jikan.schedule(day='x')
    aio_jikan.close()


@pytest.mark.asyncio
def test_top_failure(aio_jikan):
    with pytest.raises(ClientException):
        yield from aio_jikan.top(type='x')
    aio_jikan.close()


@pytest.mark.asyncio
def test_genre_failure(aio_jikan):
    with pytest.raises(ClientException):
        yield from aio_jikan.genre(type='x', genre_id=1)
    aio_jikan.close()


@pytest.mark.asyncio
def test_producer_failure(aio_jikan):
    with pytest.raises(ClientException):
        yield from aio_jikan.producer(producer_id='producer')
    aio_jikan.close()


@pytest.mark.asyncio
def test_magazine_failure(aio_jikan):
    with pytest.raises(ClientException):
        yield from aio_jikan.magazine(magazine_id='magazine')
    aio_jikan.close()


@pytest.mark.asyncio
def test_user_failure(aio_jikan):
    with pytest.raises(ClientException):
        yield from aio_jikan.user(username='user', request='friends', argument='x')
    aio_jikan.close()


@pytest.mark.asyncio
def test_club_failure(aio_jikan):
    with pytest.raises(APIException):
        yield from aio_jikan.club(-1)
    aio_jikan.close()


@pytest.mark.asyncio
def test_meta_failure(aio_jikan):
    with pytest.raises(ClientException):
        yield from aio_jikan.meta(request='x', type='x', period='x')
    aio_jikan.close()
