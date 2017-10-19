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
}

class Jikan(object):
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
            err_str = '{}: error for url {}'.format(response.status_code, url)
            raise APIException(err_str)
        return response.json()

    def anime(self, id, extension=None):
        return self._get('anime', id, extension)
    
    def manga(self, id, extension=None):
        return self._get('manga', id, extension)
