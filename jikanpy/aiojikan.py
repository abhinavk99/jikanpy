import aiohttp
import asyncio

from jikanpy.jikan import AbstractJikan
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
        # Get information from the API
        response = yield from self.session.get(url)
        # Check if there's an error with the response
        yield from self._check_response(response, id=id, endpoint=endpoint)
        json = yield from response.json()
        return json

    def anime(self, id, extension=None, page=None):
        return self._get('anime', id, extension, page)

    def manga(self, id, extension=None):
        return self._get('manga', id, extension)

    def character(self, id, extension=None):
        return self._get('character', id, extension)

    def person(self, id, extension=None):
        return self._get('person', id, extension)

    @asyncio.coroutine
    def search(self, search_type, query, page=None, key=None, value=None):
        url = self._get_search_url(search_type, query, page, key, value)
        # Get information from the API
        response = yield from self.session.get(url)
        # Check if there's an error with the response
        kwargs = {'search type': search_type, 'query': query}
        yield from self._check_response(response, **kwargs)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def season(self, year, season):
        url = self._get_season_url(year, season)
        # Get information from the API
        response = yield from self.session.get(url)
        # Check if there's an error with the response
        yield from self._check_response(response, year=year, season=season)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def schedule(self, day=None):
        url = self._get_schedule_url(day)
        # Get information from the API
        response = yield from self.session.get(url)
        # Check if there's an error with the response
        yield from self._check_response(response, day=day)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def top(self, type, page=None, subtype=None):
        url = self._get_top_url(type, page, subtype)
        # Get information from the API
        response = yield from self.session.get(url)
        # Check if there's an error with the response
        yield from self._check_response(response, type=type)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def meta(self, request, type, period):
        url = self._get_meta_url(request, type, period)
        # Get information from the API
        response = yield from self.session.get(url)
        # Check if there's an error with the response
        yield from self._check_response(response, request=request, type=type, period=period)
        json = yield from response.json()
        return json

    @asyncio.coroutine
    def close(self):
        yield from self.session.close()
