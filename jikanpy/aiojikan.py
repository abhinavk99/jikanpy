import asyncio
import json
from typing import Optional, Dict, Mapping, Union, Any, TypeVar

import aiohttp

from jikanpy import utils
from jikanpy.exceptions import DeprecatedEndpoint

# Bind type variable to AioJikan so that it can be used in type hints
T = TypeVar("T", bound="AioJikan")


class AioJikan:
    """
    Asynchronous Jikan wrapper for the jikan.moe unofficial MyAnimeList API.

    Note that the API has a limit of 30 requests/minute and 2 requests/second;
    this module does not make any effort to prevent abuse of that limit,
    so use it responsibly.
    """

    def __init__(
        self,
        selected_base: Optional[str] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        """
        Constructor for AioJikan object

        Keyword Arguments:
        selected_base -- base url of Jikan API (default https://api.jikan.moe/v3)
        session -- aiohttp session
        """
        self.base = utils.BASE_URL if selected_base is None else selected_base
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

    async def _wrap_response(
        self,
        response: aiohttp.ClientResponse,
        url: str,
        **kwargs: Union[int, Optional[str]],
    ) -> Dict:
        """Parses the response as json, then runs check_response and add_jikan_metadata"""
        json_response: Dict = {}
        try:
            json_response = await response.json()
        except json.decoder.JSONDecodeError:
            pass
        utils.check_response(
            response_dict=json_response, response_status_code=response.status, **kwargs
        )
        return utils.add_jikan_metadata(response, json_response, url)

    async def _get(
        self,
        endpoint: str,
        id: int,
        extension: Optional[str],
        page: Optional[int] = None,
    ) -> Dict:
        """
        Gets the response from Jikan API given the endpoint:
        anime, manga, character, person, club
        """
        session = await self._get_session()
        url = utils.get_main_url(endpoint, id, extension, page)
        response: aiohttp.ClientResponse = await session.get(url)
        return await self._wrap_response(response, url, id=id, endpoint=endpoint)

    async def _get_creator(
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict:
        """Gets the response from Jikan API for producer and magazine"""
        session = await self._get_session()
        url = utils.get_creator_url(creator_type, creator_id, page)
        response = await session.get(url)
        return await self._wrap_response(
            response, url, id=creator_id, endpoint=creator_type
        )

    async def anime(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        """
        Gets information on an anime

        Keyword Arguments:
        id -- id of the anime to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        return await self._get("anime", id, extension, page)

    async def manga(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        """
        Gets information on a manga

        Keyword Arguments:
        id -- id of the manga to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        return await self._get("manga", id, extension, page)

    async def character(self, id: int, extension: Optional[str] = None) -> Dict:
        """
        Gets information on a character

        Keyword Arguments:
        id -- id of the character to get the information of
        extension -- special information to get, possible values in the docs
        """
        return await self._get("character", id, extension)

    async def person(self, id: int, extension: Optional[str] = None) -> Dict:
        """
        Gets information on a person

        Keyword Arguments:
        id -- id of the person to get the information of
        extension -- special information to get, possible values in the docs
        """
        return await self._get("person", id, extension)

    async def club(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        """
        Gets information on a club

        Keyword Arguments:
        id -- id of the club to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        return await self._get("club", id, extension, page)

    async def user_list(self, id: int, extension: Optional[str] = None) -> Dict:
        """Gets user list information"""
        raise DeprecatedEndpoint("user_list is a deprecated endpoint")

    async def search(
        self,
        search_type: str,
        query: str,
        page: Optional[int] = None,
        parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]] = None,
    ) -> Dict:
        """
        Searches for a query on MyAnimeList

        Keyword Arguments:
        search_type -- where to search (anime, manga, person, character)
        query -- query to search for
        page -- page number of the results (default None)
        parameters -- dictionary containing key,value pairs for ?key=value in url query
        """
        session = await self._get_session()
        url = utils.get_search_url(search_type, query, page, parameters)
        response = await session.get(url)
        kwargs = {"search type": search_type, "query": query}
        return await self._wrap_response(response, url, **kwargs)

    async def season(self, year: int, season: str) -> Dict:
        """
        Gets information on anime of the specific season

        Keyword Arguments:
        year -- year to get anime of
        season -- season to get anime of (winter, spring, summer, fall)
        """
        session = await self._get_session()
        url = utils.get_season_url(year, season)
        response = await session.get(url)
        return await self._wrap_response(response, url, year=year, season=season)

    async def season_archive(self) -> Dict:
        """Gets all the years and their respective seasons from MyAnimeList"""
        session = await self._get_session()
        response = await session.get(utils.SEASON_ARCHIVE_URL)
        return await self._wrap_response(response, utils.SEASON_ARCHIVE_URL)

    async def season_later(self) -> Dict:
        """Gets anime that have been announced for upcoming seasons"""
        session = await self._get_session()
        response = await session.get(utils.SEASON_LATER_URL)
        return await self._wrap_response(response, utils.SEASON_LATER_URL)

    async def schedule(self, day: Optional[str] = None) -> Dict:
        """
        Gets anime scheduled for the specific day

        Keyword Arguments:
        day -- day to get anime of (default None)
        """
        session = await self._get_session()
        url = utils.get_schedule_url(day)
        response = await session.get(url)
        return await self._wrap_response(response, url, day=day)

    async def top(
        self, type: str, page: Optional[int] = None, subtype: Optional[str] = None
    ) -> Dict:
        """
        Gets top items on MyAnimeList

        Keyword Arguments:
        type -- type to get top items from (anime, manga)
        page -- page number of the results (default None)
        subtype -- subtype to get filtered top items, possible values in docs
        """
        session = await self._get_session()
        url = utils.get_top_url(type, page, subtype)
        response = await session.get(url)
        return await self._wrap_response(response, url, type=type)

    async def genre(self, type: str, genre_id: int, page: Optional[int] = None) -> Dict:
        """
        Gets anime or manga by genre

        Keyword Arguments:
        type -- type to get items from (anime, manga)
        genre_id -- genre ID from MyAnimeList
        page -- page number of the results (default None)
        """
        session = await self._get_session()
        url = utils.get_genre_url(type, genre_id, page)
        response = await session.get(url)
        return await self._wrap_response(response, url, id=genre_id, type=type)

    async def producer(self, producer_id: int, page: Optional[int] = None) -> Dict:
        """
        Gets anime by the producer/studio/licensor

        Keyword Arguments:
        producer_id -- producer ID from MyAnimeList
        page -- page number of the results (default None)
        """
        return await self._get_creator("producer", producer_id, page)

    async def magazine(self, magazine_id: int, page: Optional[int] = None) -> Dict:
        """
        Gets manga by the magazine/serializer/publisher

        Keyword Arguments:
        magazine_id -- magazine ID from MyAnimeList
        page -- page number of the results (default None)
        """
        return await self._get_creator("magazine", magazine_id, page)

    async def user(
        self,
        username: str,
        request: Optional[str] = None,
        argument: Optional[Union[int, str]] = None,
        page: Optional[int] = None,
        parameters: Optional[Mapping] = None,
    ) -> Dict:
        """
        Gets user data

        Keyword Arguments:
        username -- MyAnimeList username
        request -- type of data to get (profile, history, friends, animelist, mangalist)
        argument -- data for history (anime, manga), page number for friends, type of list
        page -- page number for animelist and mangalist
        parameters -- dictionary containing key,value pairs for ?key=value in url query
        """
        session = await self._get_session()
        url = utils.get_user_url(username, request, argument, page, parameters)
        response = await session.get(url)
        return await self._wrap_response(
            response, url, username=username, request=request
        )

    async def meta(
        self,
        request: str,
        type: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Dict:
        """
        Gets meta information regarding the Jikan REST API

        Keyword Arguments:
        request -- requests (requests, status)
        type -- type to get info on, possible values in docs
        period -- time period (today, weekly, monthly)
        offset -- 1,000 requests are shown per page, offset used to show more
        """
        session = await self._get_session()
        url = utils.get_meta_url(request, type, period, offset)
        response = await session.get(url)
        return await self._wrap_response(
            response, url, request=request, type=type, period=period
        )
