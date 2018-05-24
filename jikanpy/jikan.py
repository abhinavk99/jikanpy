import json

from jikanpy import session
from jikanpy.exceptions import APIException, ClientException, DeprecatedEndpoint
from jikanpy.extensions import EXTENSIONS, SEARCH_PARAMS

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
        if response.status_code >= 400:
            err_str = '{}: error for id {} on endpoint {}'.format(
                response.status_code,
                id,
                endpoint
            )
            raise APIException(err_str)

        return response.json()

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
            if type(page) is not int:
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
        if response.status_code >= 400:
            err_str = '{}: error for search type {} on query {}'.format(
                response.status_code,
                search_type,
                query
            )
            raise APIException(err_str)

        return response.json()
