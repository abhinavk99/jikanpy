import json

from jikanpy import session
from jikanpy.exceptions import APIException, ClientException, DeprecatedEndpoint
from jikanpy.extensions import EXTENSIONS, SEARCH_PARAMS, SEASONS, DAYS

BASE_URL = 'http://api.jikan.moe/'
BASE_URL_SSL = 'https://api.jikan.moe/'

class Jikan(object):
    """
    Wrapper for calls to the jikan.me unofficial MyAnimeList API.

    Note that the API has a daily limit of 5000 calls; this module does not
    make any effort to prevent abuse of that limit, so use it responsibly.
    """
    def __init__(self, use_ssl=True):
        selected_base = BASE_URL_SSL if use_ssl else BASE_URL
        self.base = selected_base + '{endpoint}/{id}'
        self.search_base = selected_base + 'search/{search_type}/{query}'
        self.season_base = selected_base + 'season/{year}/{season}'
        self.schedule_base = selected_base + 'schedule'
        self.top_base = selected_base + 'top/{type}/{page}/{subtype}'
        self.meta_base = selected_base + 'meta/{request}/{type}/{period}'

    def _get(self, endpoint, id, extension, page=None):
        """
        Gets the response from Jikan API given the endpoint

        Keyword Arguments:
        endpoint -- endpoint of API (anime, manga, character, person)
        id -- id of what to get the information of
        extension -- special information to get, possible values in the docs
        page -- page number of the results (default None)
        """
        url = self.base.format(endpoint=endpoint, id=id)
        # Check if extension is valid
        if extension is not None:
            if extension not in EXTENSIONS[endpoint]:
                raise ClientException('The extension is not valid')
            url += '/' + extension
            if extension == 'episodes' and isinstance(page, int):
                url += '/' + page
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, id=id, endpoint=endpoint)
        return response.json()

    def _check_response(self, response, **kwargs):
        """
        Check if the response is an error

        Keyword Arguments:
        response -- response from the API call
        kwargs -- keyword arguments
        """
        if response.status_code >= 400:
            err_str = '{}: error for '.format(
                response.status_code
            )
            err_str += ', '.join('='.join((str(k), str(v))) for k,v in kwargs.items())
            raise APIException(err_str)

    def anime(self, id, extension=None, page=None):
        """Gets anime information"""
        return self._get('anime', id, extension, page)

    def manga(self, id, extension=None):
        """Gets manga information"""
        return self._get('manga', id, extension)

    def character(self, id, extension=None):
        """Gets character information"""
        return self._get('character', id, extension)

    def person(self, id, extension=None):
        """Gets person information"""
        return self._get('person', id, extension)

    def user_list(self, id, extension=None):
        """Gets user list information"""
        raise DeprecatedEndpoint('user_list is a deprecated endpoint')

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
        url = self.search_base.format(search_type=search_type, query=query)
        # Check if page and query are valid
        if page is not None:
            if not isinstance(page, int):
                raise ClientException('The parameter \'page\' must be an integer')
            url += '/' + page
        if key is not None:
            if value is None:
                raise ClientException('You need to pass a value with the key')
            values = SEARCH_PARAMS.get(key, d=None)
            if values is None:
                raise ClientException('The key is not valid')
            elif isinstance(values, list) and value not in values:
                raise ClientException('The value is not valid')
            url += '?' + key + '=' + value
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        kwargs = {'search type': search_type, 'query': query}
        self._check_response(response, **kwargs)
        return response.json()

    def season(self, year, season):
        """
        Gets information on anime of the specific season

        Keyword Arguments:
        year -- year to get anime of
        season -- season to get anime of (winter, spring, summer, fall)
        """
        url = self.season_base.format(year=year, season=season.lower())
        # Check if year and season are valid
        if not (isinstance(year, int) and season.lower() in SEASONS):
            raise ClientException('Season or year is not valid')
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, year=year, season=season)
        return response.json()

    def schedule(self, day=None):
        """
        Gets anime scheduled for the specific day

        Keyword Arguments:
        day -- day to get anime of (default None)
        """
        url = self.schedule_base
        # Check if day is valid
        if day is not None:
            if day.lower() not in DAYS:
                raise ClientException('Day is not valid')
            else:
                url += '/' + day.lower()
        # Get information from the API
        response = session.get(url)
        # Check if there's an error with the response
        self._check_response(response, day=day)
        return response.json()
