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
        url = self.base.format(endpoint=endpoint, id=id)
        if extension is not None:
            if extension not in EXTENSIONS[endpoint]:
                raise ClientException('The extension is not valid')
            url += '/' + extension
            if extension == 'episodes' and isinstance(page, int):
                url += '/' + page

        response = session.get(url)
        self._check_response(response)

        return response.json()

    def _check_response(self, response):
        if response.status_code >= 400:
            err_str = '{}: error for id {} on endpoint {}'.format(
                response.status_code,
                id,
                endpoint
            )
            raise APIException(err_str)

    def anime(self, id, extension=None, page=None):
        return self._get('anime', id, extension, parameter)

    def manga(self, id, extension=None):
        return self._get('manga', id, extension, None)

    def character(self, id, extension=None):
        return self._get('character', id, extension, None)

    def person(self, id, extension=None):
        return self._get('person', id, extension, None)

    def user_list(self, id, extension):
        raise DeprecatedEndpoint('user_list is a deprecated endpoint')

    def search(self, search_type, query, page=None, key=None, value=None):
        url = self.search_base.format(search_type=search_type, query=query)
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
            else if isinstance(values, list) and value not in values:
                raise ClientException('The value is not valid')
            url += '?' + key + '=' + value

        response = session.get(url)
        self._check_response(response)

        return response.json()
