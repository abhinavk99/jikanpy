import json
import os
import requests

from jikanpy import session
from jikanpy.exceptions import APIException, ClientException

BASE_URL = 'http://jikan.me/api/'
BASE_URL_SSL = 'https://jikan.me/api/'

EXTENSIONS = {
    'anime': ['episodes', 'characters_staff', 'all'],
    'manga': ['characters_staff'],
    'character': [],
    'person': [],
    'user_list': ['anime', 'manga'],
}

class Jikan(object):
    """
    Wrapper for calls to the jikan.me unofficial MyAnimeList API.

    Note that the API has a daily limit of 2000 calls; this module does not
    make any effort to prevent abuse of that limit, so use it responsibly.
    """
    def __init__(self, use_ssl=True):
        selected_base = BASE_URL_SSL if use_ssl else BASE_URL
        self.base = selected_base + '{endpoint}/{id}'

    def _get(self, endpoint, id, extension):
        url = self.base.format(endpoint=endpoint, id=id)
        if extension is not None:
            if extension not in EXTENSIONS[endpoint]:
                raise ClientException
            url += '/' + extension

        response = session.get(url)
        if response.status_code >= 400:
            err_str = '{}: error for id {} on endpoint {}'.format(
                response.status_code,
                id,
                endpoint
            )
            raise APIException(err_str)

        return response.json()

    def anime(self, id, extension=None):
        return self._get('anime', id, extension)

    def manga(self, id, extension=None):
        return self._get('manga', id, extension)

    def character(self, id, extension=None):
        return self._get('character', id, extension)

    def person(self, id, extension=None):
        return self._get('person', id, extension)

    def user_list(self, id, extension):
        return self._get('user_list', id, extension)
