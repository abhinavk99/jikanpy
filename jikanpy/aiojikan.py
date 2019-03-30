import aiohttp
import asyncio

from jikanpy.abstractjikan import AbstractJikan
from jikanpy.exceptions import APIException


class AioJikan(AbstractJikan):
    """Asynchronous Jikan wrapper"""
    def __init__(self, use_ssl=True, session=None, loop=None):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.session = aiohttp.ClientSession(
            loop=self.loop) if session is None else session
        super().__init__(use_ssl=use_ssl)

    @asyncio.coroutine
    def _check_response(self, response, **kwargs):
        """Overrides _check_response in AbstractJikan"""
        if response.status >= 400:
            json = yield from response.json()
            err_str = '{} {}: error for '.format(
                response.status,
                json.get('error')
            )
            err_str += ', '.join('='.join((str(k), str(v))) for k, v in kwargs.items())
            raise APIException(err_str)

    @asyncio.coroutine
    def _get(self, endpoint, id, extension, page=None):
        url = self._get_url(endpoint, id, extension, page)
        response = yield from self.session.get(url)
        yield from self._check_response(response, id=id, endpoint=endpoint)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def _get_creator(self, creator_type, creator_id, page=None):
        url = self._get_creator_url(creator_type, creator_id, page)
        response = yield from self.session.get(url)
        yield from self._check_response(response, id=creator_id, endpoint=creator_type)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def search(self, search_type, query, page=None, parameters=None):
        url = self._get_search_url(search_type, query, page, parameters)
        response = yield from self.session.get(url)
        kwargs = {'search type': search_type, 'query': query}
        yield from self._check_response(response, **kwargs)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def season(self, year, season):
        url = self._get_season_url(year, season)
        response = yield from self.session.get(url)
        yield from self._check_response(response, year=year, season=season)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def season_archive(self):
        response = yield from self.session.get(self.season_archive_url)
        yield from self._check_response(response)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def season_later(self):
        response = yield from self.session.get(self.season_later_url)
        yield from self._check_response(response)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def schedule(self, day=None):
        url = self._get_schedule_url(day)
        response = yield from self.session.get(url)
        yield from self._check_response(response, day=day)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def top(self, type, page=None, subtype=None):
        url = self._get_top_url(type, page, subtype)
        response = yield from self.session.get(url)
        yield from self._check_response(response, type=type)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def genre(self, type, genre_id, page=None):
        url = self._get_genre_url(type, genre_id, page)
        response = yield from self.session.get(url)
        yield from self._check_response(response, id=genre_id, type=type)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def user(self, username, request=None, argument=None, page=None):
        url = self._get_user_url(username, request, argument, page)
        response = yield from self.session.get(url)
        yield from self._check_response(response, username=username, request=request)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def meta(self, request, type=None, period=None, offset=None):
        url = self._get_meta_url(request, type, period, offset)
        response = yield from self.session.get(url)
        yield from self._check_response(response, request=request, type=type, period=period)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def close(self):
        yield from self.session.close()
