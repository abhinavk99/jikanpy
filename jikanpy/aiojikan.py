from typing import Optional, Dict, Any, Mapping, Union
import json

import aiohttp
import asyncio

from jikanpy.abstractjikan import AbstractJikan
from jikanpy.exceptions import APIException


class AioJikan(AbstractJikan):
    """Asynchronous Jikan wrapper"""

    def __init__(
        self,
        selected_base: Optional[str] = None,
        use_ssl: bool = True,
        session: Optional[Any] = None,
        loop: Optional[Any] = None,
    ) -> None:
        super().__init__(selected_base=selected_base, use_ssl=use_ssl)
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.session = (
            aiohttp.ClientSession(loop=self.loop) if session is None else session
        )

    async def _check_response(  # type: ignore
        self, response: Any, **kwargs: Union[int, Optional[str]]
    ) -> None:
        """Overrides _check_response in AbstractJikan"""
        if response.status >= 400:
            try:
                json_resp = await response.json()
                error_msg = json_resp.get("error")
            except json.decoder.JSONDecodeError:
                error_msg = ""
            err_str: str = "{} {}: error for ".format(response.status, error_msg)
            err_str += ", ".join("=".join((str(k), str(v))) for k, v in kwargs.items())
            raise APIException(err_str)

    async def _get(  # type: ignore
        self,
        endpoint: str,
        id: int,
        extension: Optional[str],
        page: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_url(endpoint, id, extension, page)
        response = await self.session.get(url)
        await self._check_response(response, id=id, endpoint=endpoint)
        json = await response.json()
        return json

    async def _get_creator(  # type: ignore
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict:
        url: str = self._get_creator_url(creator_type, creator_id, page)
        response = await self.session.get(url)
        await self._check_response(response, id=creator_id, endpoint=creator_type)
        json = await response.json()
        return json

    async def search(  # type: ignore
        self,
        search_type: str,
        query: str,
        page: Optional[int] = None,
        parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]] = None,
    ) -> Dict:
        url: str = self._get_search_url(search_type, query, page, parameters)
        response = await self.session.get(url)
        kwargs: Dict[str, str] = {"search type": search_type, "query": query}
        await self._check_response(response, **kwargs)
        json = await response.json()
        return json

    async def season(self, year: int, season: str) -> Dict:  # type: ignore
        url: str = self._get_season_url(year, season)
        response = await self.session.get(url)
        await self._check_response(response, year=year, season=season)
        json = await response.json()
        return json

    async def season_archive(self) -> Dict:  # type: ignore
        response = await self.session.get(self.season_archive_url)
        await self._check_response(response)
        json = await response.json()
        return json

    async def season_later(self) -> Dict:  # type: ignore
        response = await self.session.get(self.season_later_url)
        await self._check_response(response)
        json = await response.json()
        return json

    async def schedule(self, day: Optional[str] = None) -> Dict:  # type: ignore
        url: str = self._get_schedule_url(day)
        response = await self.session.get(url)
        await self._check_response(response, day=day)
        json = await response.json()
        return json

    async def top(  # type: ignore
        self, type: str, page: Optional[int] = None, subtype: Optional[str] = None
    ) -> Dict:
        url: str = self._get_top_url(type, page, subtype)
        response = await self.session.get(url)
        await self._check_response(response, type=type)
        json = await response.json()
        return json

    async def genre(  # type: ignore
        self, type: str, genre_id: int, page: Optional[int] = None
    ) -> Dict:
        url: str = self._get_genre_url(type, genre_id, page)
        response = await self.session.get(url)
        await self._check_response(response, id=genre_id, type=type)
        json = await response.json()
        return json

    async def user(  # type: ignore
        self,
        username: str,
        request: Optional[str] = None,
        argument: Optional[Union[int, str]] = None,
        page: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_user_url(username, request, argument, page)
        response = await self.session.get(url)
        await self._check_response(response, username=username, request=request)
        json = await response.json()
        return json

    async def meta(  # type: ignore
        self,
        request: str,
        type: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Dict:
        url: str = self._get_meta_url(request, type, period, offset)
        response = await self.session.get(url)
        await self._check_response(response, request=request, type=type, period=period)
        json = await response.json()
        return json

    async def close(self) -> None:
        await self.session.close()
