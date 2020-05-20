import json
from typing import Optional, Dict, Mapping, Union

import requests

from jikanpy import utils
from jikanpy.exceptions import DeprecatedEndpoint


class Jikan:
    """
    Synchronous Jikan wrapper for the jikan.moe unofficial MyAnimeList API.

    Note that the API has a limit of 30 requests/minute and 2 requests/second;
    this module does not make any effort to prevent abuse of that limit,
    so use it responsibly.
    """

    def __init__(
        self,
        selected_base: Optional[str] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        """
        Constructor for Jikan object

        Keyword Arguments:
        selected_base -- base url of Jikan API (default https://api.jikan.moe/v3)
        session -- requests session
        """
        self.base = utils.BASE_URL if selected_base is None else selected_base
        self.session = requests.Session() if session is None else session

    def _wrap_response(
        self, response: requests.Response, url: str, **kwargs: Union[int, Optional[str]]
    ) -> Dict:
        """Parses the response as json, then runs check_response and add_jikan_metadata"""
        json_response: Dict = {}
        try:
            json_response = response.json()
        except json.decoder.JSONDecodeError:
            # json failed to be parsed
            # this could happen, for example, when someone has been IP banned
            # and it returns the typical nginx 403 forbidden page
            pass
        utils.check_response(
            response_dict=json_response,
            response_status_code=response.status_code,
            **kwargs,
        )
        return utils.add_jikan_metadata(response, json_response, url)

    def _get(
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
        url = utils.get_main_url(endpoint, id, extension, page)
        response = self.session.get(url)
        return self._wrap_response(response, url, id=id, endpoint=endpoint)

    def _get_creator(
        self, creator_type: str, creator_id: int, page: Optional[int] = None
    ) -> Dict:
        """Gets the response from Jikan API for producer and magazine"""
        url = utils.get_creator_url(creator_type, creator_id, page)
        response = self.session.get(url)
        return self._wrap_response(response, url, id=creator_id, endpoint=creator_type)

    def anime(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        """
        Gets information on an anime

        Keyword Arguments:
        id -- id of the anime to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        return self._get("anime", id, extension, page)

    def manga(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        """
        Gets information on a manga

        Keyword Arguments:
        id -- id of the manga to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        return self._get("manga", id, extension, page)

    def character(self, id: int, extension: Optional[str] = None) -> Dict:
        """
        Gets information on a character

        Keyword Arguments:
        id -- id of the character to get the information of
        extension -- special information to get, possible values in the docs
        """
        return self._get("character", id, extension)

    def person(self, id: int, extension: Optional[str] = None) -> Dict:
        """
        Gets information on a person

        Keyword Arguments:
        id -- id of the person to get the information of
        extension -- special information to get, possible values in the docs
        """
        return self._get("person", id, extension)

    def club(
        self, id: int, extension: Optional[str] = None, page: Optional[int] = None
    ) -> Dict:
        """
        Gets information on a club

        Keyword Arguments:
        id -- id of the club to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        return self._get("club", id, extension, page)

    def user_list(self, id: int, extension: Optional[str] = None) -> Dict:
        """Gets user list information"""
        raise DeprecatedEndpoint("user_list is a deprecated endpoint")

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
        url = utils.get_search_url(search_type, query, page, parameters)
        response = self.session.get(url)
        kwargs = {"search type": search_type, "query": query}
        return self._wrap_response(response, url, **kwargs)

    def season(self, year: int, season: str) -> Dict:
        """
        Gets information on anime of the specific season

        Keyword Arguments:
        year -- year to get anime of
        season -- season to get anime of (winter, spring, summer, fall)
        """
        url = utils.get_season_url(year, season)
        response = self.session.get(url)
        return self._wrap_response(response, url, year=year, season=season)

    def season_archive(self) -> Dict:
        """Gets all the years and their respective seasons from MyAnimeList"""
        response = self.session.get(utils.SEASON_ARCHIVE_URL)
        return self._wrap_response(response, utils.SEASON_ARCHIVE_URL)

    def season_later(self) -> Dict:
        """Gets anime that have been announced for upcoming seasons"""
        response = self.session.get(utils.SEASON_LATER_URL)
        return self._wrap_response(response, utils.SEASON_LATER_URL)

    def schedule(self, day: Optional[str] = None) -> Dict:
        """
        Gets anime scheduled for the specific day

        Keyword Arguments:
        day -- day to get anime of (default None)
        """
        url = utils.get_schedule_url(day)
        response = self.session.get(url)
        return self._wrap_response(response, url, day=day)

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
        url = utils.get_top_url(type, page, subtype)
        response = self.session.get(url)
        return self._wrap_response(response, url, type=type)

    def genre(self, type: str, genre_id: int, page: Optional[int] = None) -> Dict:
        """
        Gets anime or manga by genre

        Keyword Arguments:
        type -- type to get items from (anime, manga)
        genre_id -- genre ID from MyAnimeList
        page -- page number of the results (default None)
        """
        url = utils.get_genre_url(type, genre_id, page)
        response = self.session.get(url)
        return self._wrap_response(response, url, id=genre_id, type=type)

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

    def user(
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
        url = utils.get_user_url(username, request, argument, page, parameters)
        response = self.session.get(url)
        return self._wrap_response(response, url, username=username, request=request)

    def meta(
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
        url = utils.get_meta_url(request, type, period, offset)
        response = self.session.get(url)
        return self._wrap_response(
            response, url, request=request, type=type, period=period
        )
