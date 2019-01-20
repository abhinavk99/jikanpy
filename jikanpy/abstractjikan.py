from abc import ABC, abstractmethod

from jikanpy.exceptions import APIException, ClientException, DeprecatedEndpoint
from jikanpy.parameters import *


BASE_URL = 'http://api.jikan.moe/v3/'
BASE_URL_SSL = 'https://api.jikan.moe/v3/'


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
        self.search_base = selected_base + 'search/{search_type}?q={query}'
        self.season_base = selected_base + 'season/{year}/{season}'
        self.schedule_base = selected_base + 'schedule'
        self.top_base = selected_base + 'top/{type}'
        self.meta_base = selected_base + 'meta/{request}/{type}/{period}'
        self.genre_base = selected_base + 'genre/{type}/{genre_id}'
        self.creator_base = selected_base + '{creator_type}/{creator_id}'
        self.user_base = selected_base + 'user/{username}'
        self.season_archive_url = selected_base + 'season/archive'
        self.season_later_url = selected_base + 'season/later'
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
            err_str += ', '.join('='.join((str(k), str(v)))
                                 for k, v in kwargs.items())
            raise APIException(err_str)

    def _get_url(self, endpoint, id, extension, page):
        """Create URL for anime, manga, character, person, and club endpoints"""
        url = self.base.format(endpoint=endpoint, id=id)
        # Check if extension is valid
        if extension is not None:
            if extension not in EXTENSIONS[endpoint]:
                raise ClientException('The extension is not valid')
            url += '/' + extension
            if extension in ('episodes', 'reviews', 'userupdates', 'members'):
                url = self._add_page_to_url(url, page)
        return url

    def _get_search_url(self, search_type, query, page, parameters):
        """Create URL for search endpoint"""
        url = self.search_base.format(search_type=search_type, query=query)
        url = self._add_page_to_url(url, page, delimiter='&page=')
        if parameters is not None:
            url += '?'
            for key, value in parameters.items():
                values = SEARCH_PARAMS.get(key)
                if values is None:
                    raise ClientException('The key is not valid')
                elif isinstance(values, tuple) and value not in values:
                    raise ClientException('The value is not valid')
                url += key + '=' + str(value) + "&"
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
        url = self._add_page_to_url(url, page)
        # Check if subtype is valid
        if subtype is not None:
            if page is None:
                raise ClientException('Page is required if subtype is given')
            if subtype.lower() not in SUBTYPES[type.lower()]:
                raise ClientException('Subtype is not valid for ' + type)
            url += '/' + subtype.lower()
        return url

    def _get_genre_url(self, type, genre_id, page):
        """Create URL for genre endpoint"""
        url = self.genre_base.format(type=type.lower(), genre_id=genre_id)
        # Check if type is valid
        if type.lower() not in GENRE_TYPES:
            raise ClientException('Type must be anime or manga')
        if not isinstance(genre_id, int):
            raise ClientException('ID must be an integer')
        url = self._add_page_to_url(url, page)
        return url

    def _get_creator_url(self, creator_type, creator_id, page):
        """Create URL for producer and magazine endpoints"""
        url = self.creator_base.format(creator_type=creator_type.lower(),
                                       creator_id=creator_id)
        # Check if type is valid
        if creator_type.lower() not in CREATOR_TYPES:
            raise ClientException('Type must be producer or magazine')
        if not isinstance(creator_id, int):
            raise ClientException('ID must be an integer')
        url = self._add_page_to_url(url, page)
        return url

    def _get_user_url(self, username, request, argument, page):
        """Create URL for user endpoint"""
        url = self.user_base.format(username=username.lower())
        if request is not None:
            if request not in USER_REQUESTS:
                raise ClientException('Invalid request for user endpoint')
            url += '/' + request
            if request.lower() == 'profile' and argument is not None:
                raise ClientException(
                    'No argument should be given for profile request')
            if request.lower() in ('animelist', 'mangalist') and argument is None and page is not None:
                raise ClientException(
                    'You must provide an argument if you provide a page for animelist or mangalist'
                )
            if argument is not None:
                if request.lower() == 'history' and argument.lower() not in USER_HISTORY_ARGUMENTS:
                    raise ClientException(
                        'Argument for history request should be anime or manga')
                if request.lower() == 'friends' and not isinstance(argument, int):
                    raise ClientException(
                        'Argument for friends request must be a page number integer')
                if request.lower() == 'animelist' and argument.lower() not in USER_ANIMELIST_ARGUMENTS:
                    raise ClientException(
                        'Argument for animelist request is not valid')
                if request.lower() == 'mangalist' and argument.lower() not in USER_MANGALIST_ARGUMENTS:
                    raise ClientException(
                        'Argument for mangalist request is not valid')
                url += '/' + str(argument)
                if request.lower() in ('animelist', 'mangalist'):
                    url = self._add_page_to_url(url, page)
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
            raise ClientException(
                'Period must be \'today\', \'weekly\', or \'monthly\'')
        return url

    def _add_page_to_url(self, url, page, delimiter='/'):
        """Add page to URL if it exists and is valid"""
        if page is not None:
            if not isinstance(page, int):
                raise ClientException(
                    'The parameter \'page\' must be an integer')
            url += delimiter + str(page)
        return url

    @abstractmethod
    def _get(self, endpoint, id, extension, page=None):
        """
        Gets the response from Jikan API given the endpoint

        Keyword Arguments:
        endpoint -- endpoint of API (anime, manga, character, person, club)
        id -- id of what to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        pass

    @abstractmethod
    def _get_creator(self, creator_type, creator_id, page=None):
        """Gets the response from Jikan API for producer and magazine"""
        pass

    def anime(self, id, extension=None, page=None):
        return self._get('anime', id, extension, page)

    def manga(self, id, extension=None):
        return self._get('manga', id, extension)

    def character(self, id, extension=None):
        return self._get('character', id, extension)

    def person(self, id, extension=None):
        return self._get('person', id, extension)

    def club(self, id, extension=None):
        return self._get('club', id, extension)

    def user_list(self, id, extension=None):
        """Gets user list information"""
        raise DeprecatedEndpoint('user_list is a deprecated endpoint')

    @abstractmethod
    def search(self, search_type, query, page=None, parameters=None):
        """
        Searches for a query on MyAnimeList

        Keyword Arguments:
        search_type -- where to search (anime, manga, person, character)
        query -- query to search for
        page -- page number of the results (default None)
        parameters - dictionary containing key,value pairs for ?key=value in url query
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
    def season_archive(self):
        """
        Gets all the years and their respective seasons from MyAnimeList
        """
        pass

    @abstractmethod
    def season_later(self):
        """
        Gets anime that have been announced for upcoming seasons
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

    def producer(self, producer_id, page=None):
        """
        Gets anime by the producer/studio/licensor

        Keyword Arguments:
        producer_id -- producer ID from MyAnimeList
        page -- page number of the results (default None)
        """
        return self._get_creator('producer', producer_id, page)

    def magazine(self, magazine_id, page=None):
        """
        Gets manga by the magazine/serializer/publisher

        Keyword Arguments:
        magazine_id -- magazine ID from MyAnimeList
        page -- page number of the results (default None)
        """
        return self._get_creator('magazine', magazine_id, page)

    @abstractmethod
    def user(self, username, request, argument=None, page=None):
        """
        Gets user data

        Keyword Arguments:
        username -- MyAnimeList username
        request -- type of data to get (profile, history, friends, animelist, mangalist)
        argument -- data for history (anime, manga), page number for friends, type of list
        page -- page number for animelist and mangalist
        """
        pass

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
