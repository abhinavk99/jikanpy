"""AioJikan
====================================
aiojikan.py contains the AioJikan class, an asynchronous Jikan wrapper.
"""

import json
from typing import Optional, Dict, Mapping, Union, Any, TypeVar

import aiohttp
import simplejson

from jikanpy import utils
from jikanpy.exceptions import APIException, DeprecatedEndpoint

# Bind type variable to AioJikan so that it can be used in type hints
AioJikanT = TypeVar("AioJikanT", bound="AioJikan")


class AioJikan:
    """Asynchronous Jikan wrapper for the jikan.moe unofficial MyAnimeList API.

    Note that the API has a limit of 30 requests/minute and 2 requests/second;
    this module does not make any effort to prevent abuse of that limit,
    so use it responsibly.

    Usage Example:
        ::

            import asyncio
            from jikanpy import AioJikan

            async def main():
                async with AioJikan() as aio_jikan:
                    pass

                # You can also construct AioJikan like below, but make sure to close
                # the object
                aio_jikan_2 = AioJikan()
                await aio_jikan_2.close()

            asyncio.run(main())

    Attributes:
        base: The base URL of the Jikan API being accessed.
        session: The aiohttp session.
    """

    def __init__(
        self,
        selected_base: Optional[str] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        """Constructs the AioJikan object.

        Args:
            selected_base (str, optional): Base url of Jikan API. Defaults to
                the official Jikan API URL.
            session (aiohttp.ClientSession, optional) -- Requests session.
                Defaults to a new aiohttp session object.

        Returns:
            AioJikan: Instance of AioJikan.

        Examples:
            >>> aio_jikan_1 = AioJikan()
            >>> aio_jikan_2 = AioJikan(selected_base='http://localhost:8000/v3')
            >>> aio_jikan_3 = AioJikan(
                    session=aiohttp.ClientSession(headers={'x-test': 'true'})
                )
        """
        self.base = (
            utils.BASE_URL if selected_base is None else selected_base.rstrip("/ ")
        )
        self.session = session

    async def __aenter__(self: AioJikanT) -> AioJikanT:
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
    ) -> Dict[str, Any]:
        """Parses the response as json, then runs check_response and
        add_jikan_metadata
        """
        json_response: Dict[str, Any] = {}
        try:
            json_response = await response.json()
            if not isinstance(json_response, dict):
                json_response = {"data": json_response}
        except (json.decoder.JSONDecodeError, simplejson.JSONDecodeError):
            json_response = {"error": await response.text()}
        if response.status >= 400:
            raise APIException(response.status, json_response, **kwargs)
        return utils.add_jikan_metadata(response, json_response, url)

    async def _request(
        self, url: str, **kwargs: Union[int, Optional[str]]
    ) -> Dict[str, Any]:
        """Makes a request to the Jikan API given the url and wraps the response."""
        session = await self._get_session()
        response = await session.get(url)
        return await self._wrap_response(response, url, **kwargs)

    async def _get(
        self,
        endpoint: str,
        id: int,
        extension: Optional[str],
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Gets the response from Jikan API given the endpoint:
        anime, manga, character, person, club
        """
        url = utils.get_main_url(self.base, endpoint, id, extension, page)
        return await self._request(url, id=id, endpoint=endpoint)

    async def _get_creator(
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets the response from Jikan API for producer and magazine"""
        url = utils.get_creator_url(self.base, creator_type, creator_id, page)
        return await self._request(url, id=creator_id, endpoint=creator_type)

    async def anime(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets information on an anime.

        Args:
            id (:obj:`int`): ID of the anime to get the information of.
            extension (:obj:`str`, optional): Special information to get of the
                anime. Possible values are in the Jikan API documentation.
                Defaults to None.
            page (:obj:`int`, optional) -- Page number of the results. Defaults
                to None.

        Returns:
            Dict[str, Any]: Dictionary containing information about the anime.

        Examples:
            >>> await jikan.anime(14719)
            >>> await jikan.anime(14719, extension='episodes')
            >>> await jikan.anime(14719, extension='episodes', page=2)
            >>> await jikan.anime(14719, extension='news')
        """
        return await self._get("anime", id, extension, page)

    async def manga(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets information on a manga.

        Args:
            id (:obj:`int`): ID of the manga to get the information of.
            extension (:obj:`str`, optional): Special information to get of the
                manga. Possible values are in the Jikan API documentation.
                Defaults to None.
            page (:obj:`int`, optional) -- Page number of the results. Defaults
                to None.

        Returns:
            Dict: Dictionary containing information about the manga.

        Examples:
            >>> await jikan.manga(1630)
        """
        return await self._get("manga", id, extension, page)

    async def character(
        self, id: int, extension: Optional[str] = None
    ) -> Dict[str, Any]:
        """Gets information on a character.

        Args:
            id (:obj:`int`): ID of the character to get the information of.
            extension (:obj:`str`, optional): Special information to get of the
                character. Possible values are in the Jikan API documentation.
                Defaults to None.

        Returns:
            Dict: Dictionary containing information about the character.

        Examples:
            >>> await jikan.character(6356)
        """
        return await self._get("character", id, extension)

    async def person(self, id: int, extension: Optional[str] = None) -> Dict[str, Any]:
        """Gets information on a person.

        Args:
            id (:obj:`int`): ID of the person to get the information of.
            extension (:obj:`str`, optional): Special information to get of the
                person. Possible values are in the Jikan API documentation.
                Defaults to None.

        Returns:
            Dict: Dictionary containing information about the person.

        Examples:
            >>> await jikan.person(2)
        """
        return await self._get("person", id, extension)

    async def club(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets information on a club.

        Args:
            id (:obj:`int`): ID of the club to get the information of.
            extension (:obj:`str`, optional): Special information to get of the
                club. Possible values are in the Jikan API documentation.
                Defaults to None.
            page (:obj:`int`, optional) -- Page number of the results. Defaults
                to None.

        Returns:
            Dict: Dictionary containing information about the club.

        Examples:
            >>> await jikan.club(379)
        """
        return await self._get("club", id, extension, page)

    async def user_list(
        self, id: int, extension: Optional[str] = None
    ) -> Dict[str, Any]:
        """Deprecated: Gets user list information."""
        raise DeprecatedEndpoint("user_list is a deprecated endpoint")

    async def search(
        self,
        search_type: str,
        query: str,
        page: Optional[int] = None,
        parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]] = None,
    ) -> Dict[str, Any]:
        """Searches for a query on MyAnimeList.

        Args:
            search_type (:obj:`str`): Where to search. Possible values are
                anime, manga, person, and character.
            query (:obj:`str`): Query to search for.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Defaults to None.

        Returns:
            Dict: Dictionary containing search results.

        Examples:
            >>> await jikan.search('anime', 'Jojo')
            >>> await jikan.search('anime', 'Jojo', page=2)
            >>> await jikan.search('anime', 'Jojo', parameters={'type': 'tv'})
            >>> await jikan.search(
                    'anime', 'Jojo', page=2, parameters={'genre': 37, 'type': 'tv'}
                )
        """
        url = utils.get_search_url(self.base, search_type, query, page, parameters)
        kwargs = {"search type": search_type, "query": query}
        return await self._request(url, **kwargs)

    async def season(self, year: int, season: str) -> Dict[str, Any]:
        """Gets information on anime of the specific season.

        Args:
            year (:obj:`int`): Year to get anime of.
            season (:obj:`str`): Season to get anime of. Possible values are
                winter, spring, summer, and fall.

        Returns:
            Dict: Dictionary containing information on anime of the season.

        Examples:
            >>> await jikan.season(year=2018, season='winter')
            >>> await jikan.season(year=2016, season='spring')
        """
        url = utils.get_season_url(self.base, year, season)
        return await self._request(url, year=year, season=season)

    async def season_archive(self) -> Dict[str, Any]:
        """Gets all the years and their respective seasons from MyAnimeList.

        Returns:
            Dict: Dictionary containing all the years and seasons.

        Examples:
            >>> await jikan.season_archive()
        """
        url = utils.get_season_archive_url(self.base)
        return await self._request(url)

    async def season_later(self) -> Dict[str, Any]:
        """Gets anime that have been announced for upcoming seasons.

        Returns:
            Dict: Dictionary containing anime in upcoming seasons.

        Examples:
            >>> await jikan.season_later()
        """
        url = utils.get_season_later_url(self.base)
        return await self._request(url)

    async def schedule(self, day: Optional[str] = None) -> Dict[str, Any]:
        """Gets anime scheduled.

        Args:
            day (:obj:`str`, optional): Day of the week to get the scheduled
                anime. Defaults to None.

        Returns:
            Dict: Dictionary containing anime scheduled.

        Examples:
            >>> await jikan.schedule()
            >>> await jikan.schedule(day='monday')
        """
        url = utils.get_schedule_url(self.base, day)
        return await self._request(url, day=day)

    async def top(
        self, type: str, page: Optional[int] = None, subtype: Optional[str] = None
    ) -> Dict[str, Any]:
        """Gets top items on MyAnimeList.

        Args:
            type (:obj:`str`): Type to get top items from. Possible values are
                anime and manga.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.
            subtype (:obj:`str`, optional): Subtype to get filtered top items.
                Possible values are in the Jikan API documentation.  Defaults to
                None.

        Returns:
            Dict: Dictionary containing top items on MyAnimeList.

        Examples:
            >>> await jikan.top(type='manga')
            >>> await jikan.top(type='anime', page=2, subtype='upcoming')
        """
        url = utils.get_top_url(self.base, type, page, subtype)
        return await self._request(url, type=type)

    async def genre(
        self, type: str, genre_id: int, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets anime or manga by genre.

        Args:
            type (:obj:`str`): Type to get items from. Possible values are anime
                and manga.
            genre_id (:obj:`int`): Genre ID from MyAnimeList.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.

        Returns:
            Dict: Dictionary containing anime or manga by genre.

        Examples:
            >>> await jikan.genre(type='anime', genre_id=1)
            >>> await jikan.genre(type='manga', genre_id=2)
        """
        url = utils.get_genre_url(self.base, type, genre_id, page)
        return await self._request(url, id=genre_id, type=type)

    async def producer(
        self, producer_id: int, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets anime by the producer/studio/licensor.

        Args:
            producer_id (:obj:`int`): Producer ID from MyAnimeList.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.

        Returns:
            Dict: Dictionary containing anime by the producer/studio/licensor.

        Examples:
            >>> await jikan.producer(producer_id=4)
            >>> await jikan.producer(producer_id=4, page=2)
        """
        return await self._get_creator("producer", producer_id, page)

    async def magazine(
        self, magazine_id: int, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Gets manga by the magazine/serializer/publisher.

        Args:
            magazine_id (:obj:`int`): Magazine ID from MyAnimeList.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.

        Returns:
            Dict: Dictionary containing manga by the
                magazine/serializer/publisher.

        Examples:
            >>> await jikan.magazine(magazine_id=83)
            >>> await jikan.magazine(magazine_id=83, page=2)
        """
        return await self._get_creator("magazine", magazine_id, page)

    async def user(
        self,
        username: str,
        request: Optional[str] = None,
        argument: Optional[Union[int, str]] = None,
        page: Optional[int] = None,
        parameters: Optional[Mapping[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Gets information about the user.

        Args:
            username (:obj:`str`): MyAnimeList username.
            request (:obj:`str`, optional): Type of data to get. Possible values
                are profile, history, friends, animelist, and mangalist.
                Defaults to None.
            argument (:obj:`str` or :obj:`int`, optional): For history, possible
                values are anime and manga. For animelist and mangalist,
                possible values are in the Jikan API documentation.  Defaults to
                None.
            page (:obj:`int`, optional): Page number for friends. Defaults to
                None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Defaults to None.

        Returns:
            Dict: Dictionary containing information about the user.

        Examples:
            >>> await jikan.user(username='Xinil')
            >>> await jikan.user(username='Xinil', request='profile')
            >>> await jikan.user(username='Xinil', request='friends', page=2)
            >>> await jikan.user(username='Xinil', request='history')
            >>> await jikan.user(username='Xinil', request='animelist', argument='ptw')
            >>> await jikan.user(
                    username='Xinil', request='animelist', parameters={'page': 2}
                )
            >>> await jikan.user(
                    username='Xinil',
                    request='animelist',
                    argument='ptw',
                    parameters={'page': 2}
                )
        """
        url = utils.get_user_url(
            self.base, username, request, argument, page, parameters
        )
        return await self._request(url, username=username, request=request)

    async def meta(
        self,
        request: str,
        type: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Gets meta information regarding the Jikan API.

        Args:
            request (:obj:`str`): Type of request. Possible values are requests
                and status.
            type (:obj:`str`, optional): Type of information to get for
                requests. Possible values are in the Jikan API documentation.
                Defaults to None.
            period (:obj:`str`, optional): Time period to get for requests.
                Possible values are today, weekly, and monthly. Defaults to
                None.
            offset (:obj:`int`, optional): 1,000 requests are shown per page.
                Offset is used to show more. Defaults to None.

        Returns:
            Dict: Dictionary containing meta information.

        Examples:
            >>> await jikan.meta('requests')
            >>> await jikan.meta('requests', type='anime', period='today')
            >>> await jikan.meta('status')
        """
        url = utils.get_meta_url(self.base, request, type, period, offset)
        return await self._request(url, request=request, type=type, period=period)
