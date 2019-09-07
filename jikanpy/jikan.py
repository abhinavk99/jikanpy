import json
from typing import Optional, Dict, Mapping, Union

import requests

from jikanpy.abstractjikan import AbstractJikan


class Jikan(AbstractJikan):
    """Synchronous Jikan wrapper"""

    def __init__(
        self,
        selected_base: Optional[str] = None,
        use_ssl: bool = True,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(selected_base=selected_base, use_ssl=use_ssl)
        self.session = requests.Session() if session is None else session

    def _wrap_response(
        self, response: requests.Response, url: str, **kwargs: Union[int, Optional[str]]
    ) -> Dict:
        json_response: Dict = {}
        try:
            json_response = response.json()
        except json.decoder.JSONDecodeError:
            # json failed to be parsed
            # this could happen, for example, when someone has been IP banned
            # and it returns the typical nginx 403 forbidden page
            pass
        self._check_response(
            response_dict=json_response,
            response_status_code=response.status_code,
            **kwargs,
        )
        return self._add_jikan_metadata(response, json_response, url)

    def _get(
        self,
        endpoint: str,
        id: int,
        extension: Optional[str],
        page: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_url(endpoint, id, extension, page)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(response, url, id=id, endpoint=endpoint)

    def _get_creator(
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict:
        url: str = self._get_creator_url(creator_type, creator_id, page)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(response, url, id=creator_id, endpoint=creator_type)

    def search(
        self,
        search_type: str,
        query: str,
        page: Optional[int] = None,
        parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]] = None,
    ) -> Dict:
        url: str = self._get_search_url(search_type, query, page, parameters)
        response: requests.Response = self.session.get(url)
        kwargs: Dict[str, str] = {"search type": search_type, "query": query}
        return self._wrap_response(response, url, **kwargs)

    def season(self, year: int, season: str) -> Dict:
        url: str = self._get_season_url(year, season)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(response, url, year=year, season=season)

    def season_archive(self) -> Dict:
        response: requests.Response = self.session.get(self.season_archive_url)
        return self._wrap_response(response, self.season_archive_url)

    def season_later(self) -> Dict:
        response: requests.Response = self.session.get(self.season_later_url)
        return self._wrap_response(response, self.season_later_url)

    def schedule(self, day: Optional[str] = None) -> Dict:
        url: str = self._get_schedule_url(day)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(response, url, day=day)

    def top(
        self, type: str, page: Optional[int] = None, subtype: Optional[str] = None
    ) -> Dict:
        url: str = self._get_top_url(type, page, subtype)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(response, url, type=type)

    def genre(self, type: str, genre_id: int, page: Optional[int] = None) -> Dict:
        url: str = self._get_genre_url(type, genre_id, page)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(response, url, id=genre_id, type=type)

    def user(
        self,
        username: str,
        request: Optional[str] = None,
        argument: Optional[Union[int, str]] = None,
        page: Optional[int] = None,
        parameters: Optional[Mapping] = None,
    ) -> Dict:
        url: str = self._get_user_url(username, request, argument, page, parameters)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(response, url, username=username, request=request)

    def meta(
        self,
        request: str,
        type: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_meta_url(request, type, period, offset)
        response: requests.Response = self.session.get(url)
        return self._wrap_response(
            response, url, request=request, type=type, period=period
        )
