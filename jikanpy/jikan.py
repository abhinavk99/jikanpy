from jikanpy.abstractjikan import AbstractJikan
from jikanpy import session


class Jikan(AbstractJikan):
    """Synchronous Jikan wrapper"""
    def _get(self, endpoint, id, extension, page=None):
        url = self._get_url(endpoint, id, extension, page)
        response = session.get(url)
        self._check_response(response, id=id, endpoint=endpoint)
        return response.json()

    def _get_creator(self, creator_type, creator_id, page=None):
        url = self._get_creator_url(creator_type, creator_id, page)
        response = session.get(url)
        self._check_response(response, id=creator_id, endpoint=creator_type)
        return response.json()

    def search(self, search_type, query, page=None, key=None, value=None):
        url = self._get_search_url(search_type, query, page, key, value)
        response = session.get(url)
        kwargs = {'search type': search_type, 'query': query}
        self._check_response(response, **kwargs)
        return response.json()

    def season(self, year, season):
        url = self._get_season_url(year, season)
        response = session.get(url)
        self._check_response(response, year=year, season=season)
        return response.json()

    def schedule(self, day=None):
        url = self._get_schedule_url(day)
        response = session.get(url)
        self._check_response(response, day=day)
        return response.json()

    def top(self, type, page=None, subtype=None):
        url = self._get_top_url(type, page, subtype)
        response = session.get(url)
        self._check_response(response, type=type)
        return response.json()

    def genre(self, type, genre_id, page=None):
        url = self._get_genre_url(type, genre_id, page)
        response = session.get(url)
        self._check_response(response, id=genre_id, type=type)
        return response.json()

    def user(self, username, request=None, argument=None):
        url = self._get_user_url(username, request, argument)
        response = session.get(url)
        self._check_response(response, username=username, request=request)
        return response.json()

    def meta(self, request, type, period):
        url = self._get_meta_url(request, type, period)
        response = session.get(url)
        self._check_response(response, request=request,
                             type=type, period=period)
        return response.json()
