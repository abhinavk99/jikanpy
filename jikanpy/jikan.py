from typing import Optional, Dict, Any, Mapping, Union

from jikanpy.abstractjikan import AbstractJikan
from jikanpy import session


class Jikan(AbstractJikan):
    """Synchronous Jikan wrapper"""

    def _get(
        self,
        endpoint: str,
        id: int,
        extension: Optional[str],
        page: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_url(endpoint, id, extension, page)
        response: Any = session.get(url)
        self._check_response(response, id=id, endpoint=endpoint)
        return response.json()

    def _get_creator(
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict:
        url: str = self._get_creator_url(creator_type, creator_id, page)
        response: Any = session.get(url)
        self._check_response(response, id=creator_id, endpoint=creator_type)
        return response.json()

    def search(
        self,
        search_type: str,
        query: str,
        page: Optional[int] = None,
        parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]] = None,
    ) -> Dict:
        url: str = self._get_search_url(search_type, query, page, parameters)
        response: Any = session.get(url)
        kwargs: Dict[str, str] = {"search type": search_type, "query": query}
        self._check_response(response, **kwargs)
        return response.json()

    def season(self, year: int, season: str) -> Dict:
        url: str = self._get_season_url(year, season)
        response: Any = session.get(url)
        self._check_response(response, year=year, season=season)
        return response.json()

    def season_archive(self) -> Dict:
        response: Any = session.get(self.season_archive_url)
        self._check_response(response)
        return response.json()

    def season_later(self) -> Dict:
        response: Any = session.get(self.season_later_url)
        self._check_response(response)
        return response.json()

    def schedule(self, day: Optional[str] = None) -> Dict:
        url: str = self._get_schedule_url(day)
        response: Any = session.get(url)
        self._check_response(response, day=day)
        return response.json()

    def top(
        self, type: str, page: Optional[int] = None, subtype: Optional[str] = None
    ) -> Dict:
        url: str = self._get_top_url(type, page, subtype)
        response: Any = session.get(url)
        self._check_response(response, type=type)
        return response.json()

    def genre(self, type: str, genre_id: int, page: Optional[int] = None) -> Dict:
        url: str = self._get_genre_url(type, genre_id, page)
        response: Any = session.get(url)
        self._check_response(response, id=genre_id, type=type)
        return response.json()

    def user(
        self,
        username: str,
        request: Optional[str] = None,
        argument: Optional[Union[int, str]] = None,
        page: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_user_url(username, request, argument, page)
        response: Any = session.get(url)
        self._check_response(response, username=username, request=request)
        return response.json()

    def meta(
        self,
        request: str,
        type: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_meta_url(request, type, period, offset)
        response: Any = session.get(url)
        self._check_response(response, request=request, type=type, period=period)
        return response.json()
