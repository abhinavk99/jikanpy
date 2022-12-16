"""AioJikan
====================================
aiojikan.py contains the AioJikan class, an asynchronous Jikan wrapper.
"""

import json
from typing import Optional, Dict, Union, Any, TypeVar

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
            >>> aio_jikan_2 = AioJikan(selected_base='http://localhost:8000/v4')
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

    async def anime(
        self,
        id: int,
        extension: Optional[str] = None,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Gets information on an anime.

        Args:
            id (:obj:`int`): ID of the anime to get the information of.
            extension (:obj:`str`, optional): Special information (via URL param)
                to get of the anime. Possible values are in the Jikan API documentation.
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

    # Extended functionality because this endpoint is the only outlier to the pattern
    async def anime_episode_by_id(
        self, anime_id: int, episode_id: int
    ) -> Dict[str, Any]:
        """Gets episode by anime ID and episode ID.

        Args:
            anime_id (:obj:`int`): ID of the anime to get the episode of.
            episode_id (:obj:`int`): ID of the episode to get.

        Returns:
            Dict: Dictionary containing information about the episode.

        Examples:
            >>> await jikan.anime_episode_by_id(anime_id=1, episode_id=1)
        """
        url = f"{self.base}/anime/{anime_id}/episodes/{episode_id}"
        return await self._request(url)

    async def manga(
        self,
        id: int,
        extension: Optional[str] = None,
        page: Optional[int] = None,
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

    async def characters(
        self,
        id: int,
        extension: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets information on a character.

        Args:
            id (:obj:`int`): ID of the character to get the information of.
            extension (:obj:`str`, optional): Special information (via URL param)
                to get of the character. Possible values are in the Jikan API
                documentation. Defaults to None.

        Returns:
            Dict: Dictionary containing information about the character.

        Examples:
            >>> await jikan.character(6356)
        """
        return await self._get("characters", id, extension)

    async def people(
        self,
        id: int,
        extension: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets information on a person.

        Args:
            id (:obj:`int`): ID of the person to get the information of.
            extension (:obj:`str`, optional): Special information (via URL param)
                to get of the person. Possible values are in the Jikan API
                documentation. Defaults to None.

        Returns:
            Dict: Dictionary containing information about the person.

        Examples:
            >>> await jikan.people(2)
            >>> await jikan.people(2, extension='pictures')
            >>> await jikan.people(2,
                    extension='pictures',
                    parameters={'limit': 10}
                )
        """
        return await self._get("people", id, extension)

    async def clubs(
        self,
        id: int,
        extension: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets information on a club.

        Args:
            id (:obj:`int`): ID of the club to get the information of.
            extension (:obj:`str`, optional): Special information (via URL param)
                to get of the club. Possible values are in the Jikan API documentation.
                Defaults to None.

        Returns:
            Dict: Dictionary containing information about the club.

        Examples:
            >>> await jikan.clubs(379)
        """
        return await self._get("clubs", id, extension)

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
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Searches for a query on MyAnimeList.

        Args:
            search_type (:obj:`str`): Where to search. Possible values are
                anime, characters, clubs, magazines, manga, people, producers,
                and users.
            query (:obj:`str`): Query to search for.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Check API doc for information
                on the parameters each search endpoint accepts. Defaults to None.

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

    async def seasons(
        self,
        year: Optional[int] = None,
        season: Optional[str] = None,
        extension: Optional[str] = None,
        page: Optional[int] = None,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Gets information on anime of the specific season or the current seasaon if
            no parameters are specified.

        Args:
            year (:obj:`int`, optional): Year to get anime of. Defaults to None.
            season (:obj:`str`, optional): Season to get anime of. Possible values are
                winter, spring, summer, and fall. Defaults to None.
            extension (:obj:`str`, optional): Special information (via URL param) to
                get of the season. Possible values are in the Jikan API documentation.
                Note: getSeasonsList is unsupported here, instead use season_history.
                Defaults to None.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Defaults to None.

        Returns:
            Dict: Dictionary containing information on anime of the season.

        Examples:
            >>> jikan.seasons()
            >>> jikan.seasons(year=2018, season='winter')
            >>> jikan.seasons(year=2016, season='spring')
            >>> jikan.seasons(extension='now')
            >>> jikan.seasons(extension='upcoming')
            >>> jikan.seasons(
                    year=2021,
                    season='winter',
                    page=2,
                    parameters={'filter': 'tv'}
                )
        """
        url = utils.get_season_url(self.base, year, season, extension, page, parameters)
        return await self._request(
            url, year=year, season=season, extension=extension, page=page
        )

    async def season_history(self) -> Dict[str, Any]:
        """Gets all the years and their respective season names from MyAnimeList.

        Returns:
            Dict: Dictionary containing all the years and season names.

        Examples:
            >>> await jikan.season_history()
        """
        url = utils.get_season_history_url(self.base)
        return await self._request(url)

    async def schedules(
        self,
        day: Optional[str] = None,
        page: Optional[int] = None,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Gets anime scheduled.

        Args:
            day (:obj:`str`, optional): Day of the week to get the scheduled
                anime. Defaults to None.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Defaults to None.

        Returns:
            Dict: Dictionary containing anime scheduled.

        Examples:
            >>> await jikan.schedules()
            >>> await jikan.schedules(day='monday')
        """
        if page is not None:
            if parameters is None:
                parameters = {}

            parameters["page"] = page

        url = utils.get_schedule_url(self.base, day=day, parameters=parameters)
        return await self._request(url, day=day)

    async def top(
        self,
        type: str,
        page: Optional[int] = None,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Gets top items on MyAnimeList.

        Args:
            type (:obj:`str`): Type to get top items from. Possible values are
                anime, manga, people, characters, and reviews.
            page (:obj:`int`, optional): Page number of the results. Defaults to
                None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Defaults to None.

        Returns:
            Dict: Dictionary containing top items on MyAnimeList.

        Examples:
            >>> await jikan.top(type='manga')
            >>> await jikan.top(type='anime', page=2)
        """
        url = utils.get_top_url(self.base, type, page, parameters)
        return await self._request(url, type=type)

    async def genres(
        self,
        type: str,
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets anime or manga by genre.

        Args:
            type (:obj:`str`): Type to get items from. Possible values are anime
                and manga.
            filter (:obj:`str`, optional): Filter genres by "genres", "explicity_genres",
                "themes", or "demographics". Defaults to None.

        Returns:
           Dict: Dictionary containing MAL genres and search URLs

        Examples:
            >>> await jikan.genres(type='anime')
            >>> await jikan.genres(type='manga', filter='themes')
        """
        url = utils.get_genre_url(self.base, type=type, filter=filter)
        return await self._request(url, type=type, filter=filter)

    async def producers(
        self,
        id: int,
        extension: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Gets anime by the producer/studio/licensor.

        Args:
            id (:obj:`int`, optional): Producer ID from MyAnimeList.
            extension (:obj:`str`, optional): Special information (via URL param)
                to get of the producer. Possible values are in the Jikan API
                documentation. Defaults to None.

        Returns:
            Dict: Dictionary containing producer information

        Examples:
            >>> await jikan.producers(producer_id=4)
            >>> await jikan.producers(id=4, extension='full')
            >>> await jikan.producers(id=4, extension='external')
        """
        return await self._get("producers", id, extension)

    async def magazine(
        self, magazine_id: int, page: Optional[int] = None
    ) -> Dict[str, Any]:
        """Deprecated: Gets Magazine information by ID."""
        raise DeprecatedEndpoint("magazine is a deprecated endpoint")

    async def users(
        self,
        username: str,
        extension: Optional[str] = None,
        page: Optional[int] = None,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Gets information about the user.

        Args:
            username (:obj:`str`): MyAnimeList username.
            extension (:obj:`str`, optional): Special information (via URL param)
                to get of the producer. Possible values are in the Jikan API documentation.
                Defaults to None.
            page (:obj:`int`, optional): Page number of the results. Check API doc
                for information on which extensions accept paging. Defaults to
                None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Defaults to None.


        Returns:
            Dict: Dictionary containing information about the user.

        Examples:
            >>> await jikan.users(username='Xinil')
            >>> await jikan.users(username='Xinil', extension='full')
            >>> await jikan.users(username='Xinil', extension='friends', page=2)
            >>> await jikan.users(username='Xinil', extension='history', paramters={'type': 'anime'})
        """
        url = utils.get_user_url(self.base, username, extension, page, parameters)
        return await self._request(url, username=username, extension=extension)

    async def user_by_id(
        self,
        user_id: int,
    ) -> Dict[str, Any]:
        """Gets user name and url from MAL ID

        Args:
            user_id (:obj:`int`): MyAnimeList user ID

        Returns:
            Dict: Dictionary containing information about the user ID

        Examples:
            >>> await jikan.user_by_id(user_id=1)
        """
        url = utils.get_user_id_url(self.base, user_id)
        return await self._request(url, user_id=user_id)

    async def meta(
        self,
        request: str,
        type: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Deprecated: Gets meta information."""
        raise DeprecatedEndpoint("meta is a deprecated endpoint")

    async def random(self, type: str) -> Dict[str, Any]:
        """Gets a random `type` resource.

        Args:
            type (:obj:`str`): Type of resource to get. Available types
                are: anime, manga, characters, people, users.

        Returns:
            Dict: Dictionary containing resource information.

        Examples:
            >>> await jikan.random(type='anime')
            >>> await jikan.random(type='characters')
            >>> await jikan.random(type='users')
        """

        url = utils.get_random_url(self.base, type)
        return await self._request(url, type=type)

    async def recommendations(
        self,
        type: str,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Gets recommendations for `type` resource.

        Args:
            type (:obj:`str`): Type of of resource to get. Available types
                are: anime and manga.
            page (:obj:`int`, optional): Page number of the results. Defaults
                to None.

        Returns:
            Dict: Dictionary containing resource information.

        Examples:
            >>> await jikan.recommendations(type='anime')
            >>> await jikan.recommendations(type='manga', page=2)
        """

        url = utils.get_recommendations_url(self.base, type=type, page=page)
        return await self._request(url, type=type, page=page)

    async def reviews(
        self,
        type: str,
        page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Gets reviews for `type` resource.

        Args:
            type (:obj:`str`): Type of of resource to get. Available types
                are: anime and manga.
            page (:obj:`int`, optional): Page number of the results. Defaults
                to None.

        Returns:
            Dict: Dictionary containing resource information.

        Examples:
            >>> await jikan.reviews(type='anime')
            >>> await jikan.reviews(type='manga', page=2)
        """

        url = utils.get_reviews_url(self.base, type=type, page=page)
        return await self._request(url, type=type, page=page)

    async def watch(
        self,
        extension: str,
        parameters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Gets information about recent activity of `type` resource.

        Args:
            extension (:obj:`str`, optional): Special information (via URL param)
                to get of the producer. Possible values are in the Jikan API documentation.
                Defaults to None.
            parameters (:obj:`dict`, optional): Dictionary containing key,value
                pairs for ?key=value in url query. Defaults to None.

        Returns:
            Dict: Dictionary containing information about recent/popular episodes or promos

        Examples:
            >>> await   jikan.watch(extension='episodes')
            >>> await jikan.watch(extension='episodes/popular')
            >>> await jikan.watch(extension='promos')
            >>> await jikan.watch(extension='promos/popular', paramters={'limit': 10})
        """
        url = utils.get_watch_url(self.base, extension, parameters)
        return await self._request(url, extension=extension)
