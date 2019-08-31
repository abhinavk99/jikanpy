import pytest

from jikanpy.abstractjikan import AbstractJikan
from jikanpy import ClientException


@pytest.fixture
def abstract_jikan():
    AbstractJikan.__abstractmethods__ = set()
    return AbstractJikan()


def test_get_creator_url_type_failure(abstract_jikan):
    with pytest.raises(ClientException):
        abstract_jikan._get_creator_url("x", 1, 1)


def test_wrap_response_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan._wrap_response(None, None)


def test_get_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan._get(None, None, None)


def test_get_creator_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan._get_creator(None, None)


def test_search_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.search(None, None)


def test_season_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.season(None, None)


def test_season_archive_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.season_archive()


def test_season_later_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.season_later()


def test_schedule_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.schedule()


def test_top_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.top(None)


def test_genre_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.genre(None, None)


def test_user_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.user(None, None)


def test_meta_not_implemented(abstract_jikan):
    with pytest.raises(NotImplementedError):
        abstract_jikan.meta(None, None, None, None)
