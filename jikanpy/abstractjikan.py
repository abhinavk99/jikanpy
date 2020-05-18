from abc import ABC, abstractmethod
from typing import Mapping, Dict, Optional, Union, Any

import requests
import aiohttp

from jikanpy.exceptions import APIException, DeprecatedEndpoint


class AbstractJikan(ABC):
    """
    Base class for wrapper for calls to the jikan.moe unofficial MyAnimeList API.

    Note that the API has a limit of 30 requests/minute and 2 requests/second;
    this module does not make any effort to prevent abuse of that limit,
    so use it responsibly.
    """

    BASE_URL = "https://api.jikan.moe/v3/"

    def __init__(self, selected_base: str = None) -> None:
        super().__init__()
        if selected_base is None:
            selected_base = self.BASE_URL
        self.base: str = selected_base + "{endpoint}/{id}"
        self.search_base: str = selected_base + "search/{search_type}?q={query}"
        self.season_base: str = selected_base + "season/{year}/{season}"
        self.schedule_base: str = selected_base + "schedule"
        self.top_base: str = selected_base + "top/{type}"
        self.meta_base: str = selected_base + "meta/{request}"
        self.genre_base: str = selected_base + "genre/{type}/{genre_id}"
        self.creator_base: str = selected_base + "{creator_type}/{creator_id}"
        self.user_base: str = selected_base + "user/{username}"
        self.season_archive_url: str = selected_base + "season/archive"
        self.season_later_url: str = selected_base + "season/later"

    def _check_response(
        self,
        response_dict: Dict,
        response_status_code: int,
        **kwargs: Union[int, Optional[str]],
    ) -> None:
        """
        Check if the response is an error

        Keyword Arguments:
        response_dict -- parsed response from the API call
                         is empty ({}) when there was a json.decoder.JSONDecodeError
        response_status -- the corresponding http code for the response
        kwargs -- keyword arguments
        """
        if response_status_code >= 400:
            error_msg = response_dict.get("error", "")
            err_str: str = "{} {}: error for ".format(response_status_code, error_msg)
            err_str += ", ".join("=".join((str(k), str(v))) for k, v in kwargs.items())
            raise APIException(err_str)

    def _add_jikan_metadata(
        self,
        response: Union[requests.Response, aiohttp.ClientResponse],
        response_dict: Dict,
        url: str,
    ) -> Dict:
        """Adds the response headers and jikan endpoint url to response dictionary"""
        response_dict["jikan_url"] = url
        # dict() is to convert from CIMultiDictProxy for aiohttp.ClientResponse
        response_dict["headers"] = dict(response.headers)
        return response_dict

    @abstractmethod
    def _wrap_response(
        self,
        response: Any,  # Union[requests.Response, aiohttp.ClientResponse
        url: str,
        **kwargs: Union[int, Optional[str]],
    ) -> Dict:
        """Parses the response as json, then runs _check_response and _add_jikan_metadata"""
        raise NotImplementedError

    def _get_url_with_page(
        self, url: str, page: Optional[int], delimiter: str = "/"
    ) -> str:
        """Add page to URL if it exists"""
        return url if page is None else f"{url}{delimiter}{page}"

    def _get_url(
        self, endpoint: str, id: int, extension: Optional[str], page: Optional[int]
    ) -> str:
        """Create URL for anime, manga, character, person, and club endpoints"""
        url: str = self.base.format(endpoint=endpoint, id=id)
        if extension is not None:
            url += f"/{extension}"
            url = self._get_url_with_page(url, page)
        return url

    def _get_search_url(
        self,
        search_type: str,
        query: str,
        page: Optional[int],
        parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]],
    ) -> str:
        """Create URL for search endpoint"""
        url: str = self.search_base.format(search_type=search_type, query=query)
        url = self._get_url_with_page(url, page, delimiter="&page=")
        if parameters is not None:
            url += "".join(f"&{k}={v}" for k, v in parameters.items())
        return url

    def _get_season_url(self, year: int, season: str) -> str:
        """Create URL for season endpoint"""
        return self.season_base.format(year=year, season=season.lower())

    def _get_schedule_url(self, day: Optional[str]) -> str:
        """Create URL for schedule endpoint"""
        return (
            self.schedule_base if day is None else f"{self.schedule_base}/{day.lower()}"
        )

    def _get_top_url(
        self, type: str, page: Optional[int], subtype: Optional[str]
    ) -> str:
        """Create URL for top endpoint"""
        url: str = self.top_base.format(type=type.lower())
        url = self._get_url_with_page(url, page)
        return url if subtype is None else f"{url}/{subtype.lower()}"

    def _get_genre_url(self, type: str, genre_id: int, page: Optional[int]) -> str:
        """Create URL for genre endpoint"""
        url: str = self.genre_base.format(type=type.lower(), genre_id=genre_id)
        return self._get_url_with_page(url, page)

    def _get_creator_url(
        self, creator_type: str, creator_id: int, page: Optional[int]
    ) -> str:
        """Create URL for producer and magazine endpoints"""
        url: str = self.creator_base.format(
            creator_type=creator_type.lower(), creator_id=creator_id
        )
        return self._get_url_with_page(url, page)

    def _get_user_url(
        self,
        username: str,
        request: Optional[str],
        argument: Optional[Union[int, str]],
        page: Optional[int],
        parameters: Optional[Mapping],
    ) -> str:
        """Create URL for user endpoint"""
        url: str = self.user_base.format(username=username.lower())
        if request is not None:
            url += f"/{request}"
            if argument is not None:
                url += f"/{argument}"
                url = self._get_url_with_page(url, page)
        if parameters is not None:
            param_str = "&".join(f"{k}={v}" for k, v in parameters.items())
            url += f"?{param_str}"
        return url

    def _get_meta_url(
        self,
        request: str,
        type: Optional[str],
        period: Optional[str],
        offset: Optional[int],
    ) -> str:
        """Create URL for meta endpoint"""
        url: str = self.meta_base.format(request=request)
        url += f"/{type}/{period}"
        return self._get_url_with_page(url, offset)

    @abstractmethod
    def _get(
        self,
        endpoint: str,
        id: int,
        extension: Optional[str],
        page: Optional[int] = None,
    ) -> Dict:
        """
        Gets the response from Jikan API given the endpoint

        Keyword Arguments:
        endpoint -- endpoint of API (anime, manga, character, person, club)
        id -- id of what to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        raise NotImplementedError

    @abstractmethod
    def _get_creator(
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict:
        """Gets the response from Jikan API for producer and magazine"""
        raise NotImplementedError

    def anime(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        return self._get("anime", id, extension, page)

    def manga(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        return self._get("manga", id, extension, page)

    def character(self, id: int, extension: Optional[str] = None) -> Dict:
        return self._get("character", id, extension)

    def person(self, id: int, extension: Optional[str] = None) -> Dict:
        return self._get("person", id, extension)

    def club(self, id: int, extension: Optional[str] = None) -> Dict:
        return self._get("club", id, extension)

    def user_list(self, id: int, extension: Optional[str] = None) -> Dict:
        """Gets user list information"""
        raise DeprecatedEndpoint("user_list is a deprecated endpoint")

    @abstractmethod
    def search(
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
        raise NotImplementedError

    @abstractmethod
    def season(self, year: int, season: str) -> Dict:
        """
        Gets information on anime of the specific season

        Keyword Arguments:
        year -- year to get anime of
        season -- season to get anime of (winter, spring, summer, fall)
        """
        raise NotImplementedError

    @abstractmethod
    def season_archive(self) -> Dict:
        """
        Gets all the years and their respective seasons from MyAnimeList
        """
        raise NotImplementedError

    @abstractmethod
    def season_later(self) -> Dict:
        """
        Gets anime that have been announced for upcoming seasons
        """
        raise NotImplementedError

    @abstractmethod
    def schedule(self, day: Optional[str] = None) -> Dict:
        """
        Gets anime scheduled for the specific day

        Keyword Arguments:
        day -- day to get anime of (default None)
        """
        raise NotImplementedError

    @abstractmethod
    def top(
        self, type: str, page: Optional[int] = None, subtype: Optional[str] = None
    ) -> Dict:
        """
        Gets top items on MyAnimeList

        Keyword Arguments:
        type -- type to get top items from (anime, manga)
        page -- page number of the results (default None)
        subtype -- subtype to get filtered top items, possible values in docs
        """
        raise NotImplementedError

    @abstractmethod
    def genre(self, type: str, genre_id: int, page: Optional[int] = None) -> Dict:
        """
        Gets anime or manga by genre

        Keyword Arguments:
        type -- type to get items from (anime, manga)
        genre_id -- genre ID from MyAnimeList
        page -- page number of the results (default None)
        """
        raise NotImplementedError

    def producer(self, producer_id: int, page: Optional[int] = None) -> Dict:
        """
        Gets anime by the producer/studio/licensor

        Keyword Arguments:
        producer_id -- producer ID from MyAnimeList
        page -- page number of the results (default None)
        """
        return self._get_creator("producer", producer_id, page)

    def magazine(self, magazine_id: int, page: Optional[int] = None) -> Dict:
        """
        Gets manga by the magazine/serializer/publisher

        Keyword Arguments:
        magazine_id -- magazine ID from MyAnimeList
        page -- page number of the results (default None)
        """
        return self._get_creator("magazine", magazine_id, page)

    @abstractmethod
    def user(
        self,
        username: str,
        request: Optional[str],
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
        raise NotImplementedError

    @abstractmethod
    def meta(
        self,
        request: str,
        type: Optional[str],
        period: Optional[str],
        offset: Optional[int],
    ) -> Dict:
        """
        Gets meta information regarding the Jikan REST API

        Keyword Arguments:
        request -- requests (requests, status)
        type -- type to get info on, possible values in docs
        period -- time period (today, weekly, monthly)
        offset -- 1,000 requests are shown per page, offset used to show more
        """
        raise NotImplementedError
