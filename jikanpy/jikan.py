from abc import ABC, abstractmethod

from jikanpy import session
from jikanpy.exceptions import APIException, ClientException, DeprecatedEndpoint
from jikanpy.parameters import *

BASE_URL = 'http://api.jikan.moe/v3'
BASE_URL_SSL = 'https://api.jikan.moe/v3'


class AbstractJikan(ABC):
    """
    Base class for wrapper for calls to the jikan.moe unofficial MyAnimeList API.

    Note that the API has a limit of 30 requests/minute and 2 requests/second;
    this module does not make any effort to prevent abuse of that limit,
    so use it responsibly.
    """
    def __init__(self, use_ssl=True):
        selected_base = BASE_URL_SSL if use_ssl else BASE_URL
        self.base = selected_base + '{endpoint}/{id}'
        self.search_base = selected_base + 'search/{search_type}/{query}'
        self.season_base = selected_base + 'season/{year}/{season}'
        self.schedule_base = selected_base + 'schedule'
        self.top_base = selected_base + 'top/{type}'
        self.meta_base = selected_base + 'meta/{request}/{type}/{period}'
        self.genre_base = selected_base + 'genre/{type}/{genre_id}'
        self.producer_base = selected_base + 'producer/{producer_id}'
        self.magazine_base = selected_base + 'magazine/{magazine_id}'
        self.user_base = selected_base + 'user/{username}/{request}'
        super().__init__()

    def _check_response(self, response, **kwargs):
        """
        Check if the response is an error

        Keyword Arguments:
        response -- response from the API call
        kwargs -- keyword arguments
        """
        if response.status_code >= 400:
            err_str = '{} {}: error for '.format(
                response.status_code,
                response.json().get('error')
            )
            err_str += ', '.join('='.join((str(k), str(v))) for k, v in kwargs.items())
            raise APIException(err_str)

    def _get_url(self, endpoint, id, extension, page):
        """Create URL for anime, manga, character, and person endpoints"""
        url = self.base.format(endpoint=endpoint, id=id)
        # Check if extension is valid
        if extension is not None:
            if extension not in EXTENSIONS[endpoint]:
                raise ClientException('The extension is not valid')
            url += '/' + extension
            if extension == 'episodes' and isinstance(page, int):
                url += '/' + str(page)
        return url

    def _get_search_url(self, search_type, query, page, key, value):
        """Create URL for search endpoint"""
        url = self.search_base.format(search_type=search_type, query=query)
        if page is not None:
            if not isinstance(page, int):
                raise ClientException('The parameter \'page\' must be an integer')
            url += '/' + str(page)
        if key is not None:
            if value is None:
                raise ClientException('You need to pass a value with the key')
            values = SEARCH_PARAMS.get(key, d=None)
            if values is None:
                raise ClientException('The key is not valid')
            elif isinstance(values, list) and value not in values:
                raise ClientException('The value is not valid')
            url += '?' + key + '=' + value
        return url

    def _get_season_url(self, year, season):
        """Create URL for season endpoint"""
        url = self.season_base.format(year=year, season=season.lower())
        # Check if year and season are valid
        if not (isinstance(year, int) and season.lower() in SEASONS):
            raise ClientException('Season or year is not valid')
        return url

    def _get_schedule_url(self, day):
        """Create URL for schedule endpoint"""
        url = self.schedule_base
        # Check if day is valid
        if day is not None:
            if day.lower() not in DAYS:
                raise ClientException('Day is not valid')
            else:
                url += '/' + day.lower()
        return url

    def _get_top_url(self, type, page, subtype):
        """Create URL for top endpoint"""
        url = self.top_base.format(type=type.lower())
        # Check if type is valid
        if type.lower() not in SUBTYPES:
            raise ClientException('Type must be anime or manga')
        # Check if page is valid
        if page is not None:
            if not isinstance(page, int):
                raise ClientException('The parameter \'page\' must be an integer')
            url += '/' + str(page)
        # Check if subtype is valid
        if subtype is not None:
            if subtype.lower() not in SUBTYPES[type.lower()]:
                raise ClientException('Subtype is not valid for ' + type)
            url += '/' + subtype.lower()
        return url

    def _get_meta_url(self, request, type, period):
        """Create URL for meta endpoint"""
        url = self.meta_base.format(request=request, type=type, period=period)
        # Check if request is valid
        if request not in META['request']:
            raise ClientException('Request must be \'requests\' or \'status\'')
        if type not in META['type']:
            raise ClientException('Type is not valid')
        if period not in META['period']:
            raise ClientException('Period must be \'today\', \'weekly\', or \'monthly\'')
        return url

    @abstractmethod
    def _get(self, endpoint, id, extension, page=None):
        """
        Gets the response from Jikan API given the endpoint

        Keyword Arguments:
        endpoint -- endpoint of API (anime, manga, character, person)
        id -- id of what to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        pass

    @abstractmethod
    def anime(self, id, extension=None, page=None):
        """Gets anime information"""
        pass

    @abstractmethod
    def manga(self, id, extension=None):
        """Gets manga information"""
        pass

    @abstractmethod
    def character(self, id, extension=None):
        """Gets character information"""
        pass

    @abstractmethod
    def person(self, id, extension=None):
        """Gets person information"""
        pass

    def user_list(self, id, extension=None):
        """Gets user list information"""
        raise DeprecatedEndpoint('user_list is a deprecated endpoint')

    @abstractmethod
    def search(self, search_type, query, page=None, key=None, value=None):
        """
        Searches for a query on MyAnimeList

        Keyword Arguments:
        search_type -- where to search (anime, manga, person, character)
        query -- query to search for
        page -- page number of the results (default None)
        key -- key for ?key=value URL query (default None)
        value -- value for ?key=value URL query (default None)
        """
        pass

    @abstractmethod
    def season(self, year, season):
        """
        Gets information on anime of the specific season

        Keyword Arguments:
        year -- year to get anime of
        season -- season to get anime of (winter, spring, summer, fall)
        """
        pass

    @abstractmethod
    def schedule(self, day=None):
        """
        Gets anime scheduled for the specific day

        Keyword Arguments:
        day -- day to get anime of (default None)
        """
        pass

    @abstractmethod
    def top(self, type, page=None, subtype=None):
        """
        Gets top items on MyAnimeList

        Keyword Arguments:
        type -- type to get top items from (anime, manga)
        page -- page number of the results (default None)
        subtype -- subtype to get filtered top items, possible values in docs
        """
        pass

    @abstractmethod
    def genre(self, type, genre_id, page=None):
        """
        Gets anime or manga by genre

        Keyword Arguments:
        type -- type to get items from (anime, manga)
        genre_id -- genre ID from MyAnimeList
        page -- page number of the results (default None)
        """
        pass

    @abstractmethod
    def producer(self, producer_id, page=None):
        """
        Gets anime by the producer/studio/licensor

        Keyword Arguments:
        producer_id -- producer ID from MyAnimeList
        page -- page number of the results (default None)
        """
        pass

    @abstractmethod
    def magazine(self, magazine_id, page=None):
        """
        Gets manga by the magazine/serializer/publisher

        Keyword Arguments:
        magazine_id -- magazine ID from MyAnimeList
        page -- page number of the results (default None)
        """
        pass

    @abstractmethod
    def user(self, username, request, argument=None):
        """
        Gets user data

        Keyword Arguments:
        username -- MyAnimeList username
        request -- type of data to get (profile, history, friends)
        argument -- data for history (anime, manga) or page number for friends
        """

    @abstractmethod
    def meta(self, request, type, period):
        """
        Gets meta information regarding the Jikan REST API

        Keyword Arguments:
        request -- requests (requests, status)
        type -- type to get info on, possible values in docs
        period -- time period (today, weekly, monthly)
        """
        pass


class Jikan(AbstractJikan):
    """Synchronous Jikan wrapper"""
    def _get(self, endpoint, id, extension, page=None):
        url = self._get_url(endpoint, id, extension, page)
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, id=id, endpoint=endpoint)
        return response.json()

    def anime(self, id, extension=None, page=None):
        return self._get('anime', id, extension, page)

    def manga(self, id, extension=None):
        return self._get('manga', id, extension)

    def character(self, id, extension=None):
        return self._get('character', id, extension)

    def person(self, id, extension=None):
        return self._get('person', id, extension)

    def search(self, search_type, query, page=None, key=None, value=None):
        url = self._get_search_url(search_type, query, page, key, value)
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        kwargs = {'search type': search_type, 'query': query}
        self._check_response(response, **kwargs)
        return response.json()

    def season(self, year, season):
        url = self._get_season_url(year, season)
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, year=year, season=season)
        return response.json()

    def schedule(self, day=None):
        url = self._get_schedule_url(day)
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, day=day)
        return response.json()

    def top(self, type, page=None, subtype=None):
        url = self._get_top_url(type, page, subtype)
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, type=type)
        return response.json()

    def meta(self, request, type, period):
        url = self._get_meta_url(request, type, period)
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, request=request, type=type, period=period)
        return response.json()
