import json
from typing import Optional, Dict, Mapping, Union, Any, TypeVar

import aiohttp
import asyncio

from jikanpy.abstractjikan import AbstractJikan

# Bind type variable to AioJikan so that it can be used in type hints
T = TypeVar("T", bound="AioJikan")


class AioJikan(AbstractJikan):
    """Asynchronous Jikan wrapper"""

    def __init__(
        self,
        selected_base: Optional[str] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        super().__init__(selected_base=selected_base)
        self.session = session

    async def __aenter__(self: T) -> T:
        return self

    async def __aexit__(self, *excinfo: Any) -> None:
        await self.close()

    async def close(self) -> None:
        """Close AioHTTP session"""
        if self.session is not None:
            await self.session.close()

    async def _get_session(self) -> aiohttp.ClientSession:
        """Get AioHTTP session by creating it if it doesn't already exist"""
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self.session

    async def _wrap_response(  # type: ignore
        self,
        response: aiohttp.ClientResponse,
        url: str,
        **kwargs: Union[int, Optional[str]],
    ) -> Dict:
        json_response: Dict = {}
        try:
            json_response = await response.json()
        except json.decoder.JSONDecodeError:
            pass
        self._check_response(
            response_dict=json_response, response_status_code=response.status, **kwargs
        )
        return self._add_jikan_metadata(response, json_response, url)

    async def _get(  # type: ignore
        self,
        endpoint: str,
        id: int,
        extension: Optional[str],
        page: Optional[int] = None,
    ) -> Dict:
        session = await self._get_session()
        url: str = self._get_url(endpoint, id, extension, page)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(response, url, id=id, endpoint=endpoint)

    async def _get_creator(  # type: ignore
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict:
        session = await self._get_session()
        url: str = self._get_creator_url(creator_type, creator_id, page)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(
            response, url, id=creator_id, endpoint=creator_type
        )

    async def search(  # type: ignore
        self,
        search_type: str,
        query: str,
        page: Optional[int] = None,
        parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]] = None,
    ) -> Dict:
        session = await self._get_session()
        url: str = self._get_search_url(search_type, query, page, parameters)
        response: aiohttp.ClientResponse = await session.get(url)
        kwargs: Dict[str, str] = {"search type": search_type, "query": query}
        return await self._wrap_response(response, url, **kwargs)

    async def season(self, year: int, season: str) -> Dict:  # type: ignore
        session = await self._get_session()
        url: str = self._get_season_url(year, season)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(response, url, year=year, season=season)

    async def season_archive(self) -> Dict:  # type: ignore
        session = await self._get_session()
        response: aiohttp.ClientResponse = await session.get(self.season_archive_url)
        return await self._wrap_response(response, self.season_archive_url)

    async def season_later(self) -> Dict:  # type: ignore
        session = await self._get_session()
        response: aiohttp.ClientResponse = await session.get(self.season_later_url)
        return await self._wrap_response(response, self.season_later_url)

    async def schedule(self, day: Optional[str] = None) -> Dict:  # type: ignore
        session = await self._get_session()
        url: str = self._get_schedule_url(day)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(response, url, day=day)

    async def top(  # type: ignore
        self, type: str, page: Optional[int] = None, subtype: Optional[str] = None
    ) -> Dict:
        session = await self._get_session()
        url: str = self._get_top_url(type, page, subtype)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(response, url, type=type)

    async def genre(  # type: ignore
        self, type: str, genre_id: int, page: Optional[int] = None
    ) -> Dict:
        session = await self._get_session()
        url: str = self._get_genre_url(type, genre_id, page)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(response, url, id=genre_id, type=type)

    async def user(  # type: ignore
        self,
        username: str,
        request: Optional[str] = None,
        argument: Optional[Union[int, str]] = None,
        page: Optional[int] = None,
        parameters: Optional[Mapping] = None,
    ) -> Dict:
        session = await self._get_session()
        url: str = self._get_user_url(username, request, argument, page, parameters)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(
            response, url, username=username, request=request
        )

    async def meta(  # type: ignore
        self,
        request: str,
        type: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Dict:
        session = await self._get_session()
        url: str = self._get_meta_url(request, type, period, offset)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(
            response, url, request=request, type=type, period=period
        )
