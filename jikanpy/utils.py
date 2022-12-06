"""Jikan/AioJikan Utilities
====================================
utils.py contains utility methods used in Jikan and AioJikan.
"""

from typing import Optional, Dict, Mapping, Union, Any

import aiohttp
import requests


BASE_URL = "https://api.jikan.moe/v4"


def add_jikan_metadata(
    response: Union[requests.Response, aiohttp.ClientResponse],
    response_dict: Dict[str, Any],
    url: str,
) -> Dict[str, Any]:
    """Adds the response headers and jikan endpoint url to response dictionary."""
    response_dict["jikan_url"] = url

    # We need this if statement so that static type checking can determine what the type
    # of response is
    if isinstance(response, aiohttp.ClientResponse):
        # Convert from CIMultiDictProxy[str] for aiohttp.ClientResponse
        response_dict["headers"] = dict(response.headers)
    else:
        # Convert from CaseInsensitiveDict[str] for requests.Response
        response_dict["headers"] = dict(response.headers)

    return response_dict


def get_url_with_page(url: str, page: Optional[int], delimiter: str = "/") -> str:
    """Adds the page to the URL if it exists."""
    # return url if page is None else f"{url}{delimiter}{page}"
    raise DeprecatedEndpoint('Pages are no longer indexed with /page')


def get_main_url(
    base_url: str, endpoint: str, id: int, extension: Optional[str], page: Optional[int]
) -> str:
    """Creates the URL for the anime, manga, character, person, and club endpoints."""
    url = f"{base_url}/{endpoint}/{id}"
    if extension is not None:
        url += f"/{extension}"
    if page is not None:
        url += f'&page={page}'
    return url


def get_creator_url(
    base_url: str, creator_type: str, creator_id: int, page: Optional[int] = None,
) -> str:
    """Creates the URL for the producer and magazine endpoints."""
    url = f"{base_url}/{creator_type}/{creator_id}"
    if page is not None:
        url += f'&page={page}'
    return url


def get_search_url(
    base_url: str,
    search_type: str,
    query: str,
    page: Optional[int] = None,
    parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]] = None,
) -> str:
    """Creates the URL for the search endpoint."""
    url = f"{base_url}/{search_type}?q={query}"
    if page is not None:
        url += f'&page={page}'
    if parameters is not None:
        url += "".join(f"&{k}={v}" for k, v in parameters.items())
    return url


def get_season_url(
    base_url: str, year: Optional[int] = None, season: Optional[str] = None
) -> str:
    """Creates the URL for the season endpoint."""
    if year is None or season is None:
        return f"{base_url}/seasons/now"
    return f"{base_url}/seasons/{year}/{season.lower()}"


def get_season_upcoming_url(base_url: str) -> str:
    """Creates the URL for the season archive endpoint."""
    return f"{base_url}/seasons/upcoming"


def get_season_now_url(base_url: str) -> str:
    """Creates the URL for the season later endpoint."""
    return f"{base_url}/seasons/now"

def get_season_history(base_url: str) -> str:
    """Creats the URL for the getSeasonList endpoint."""
    return f"{base_url}/seasons"


def get_schedule_url(base_url: str, day: Optional[str] = None, parameters: Optional[Mapping[str, Any]] = None)  -> str:
    """Creates the URL for the schedule endpoint."""
    url = f"{base_url}/schedules"

    if day is not None:
        url += f"?filter={day}"

    if day is None and parameters is not None:
        k, v = parameters.popitem()
        url += f"?{k}={v}"
        url += "".join(f"&{k}={v}" for k, v in parameters.items())
    elif day is not None and parameters is not None:
        url += "".join(f"&{k}={v}" for k, v in parameters.items())

    return url


def get_top_url(
    base_url: str, type: str, page: Optional[int] = None, parameters: Optional[Mapping[str, Any]] = None
) -> str:
    """Creates the URL for the top endpoint."""
    url = f"{base_url}/top/{type.lower()}"
    if page is not None:
        url += f'?page={page}'

    if page is None and parameters is not None:
        k, v = parameters.popitem()
        url += f"?{k}={v}"
        url += "".join(f"&{k}={v}" for k, v in parameters.items())
    elif page is not None and parameters is not None:
        url += "".join(f"&{k}={v}" for k, v in parameters.items())

    return url


def get_genre_url(base_url: str, type: str, genre_id: int, page: Optional[int]) -> str:
    """Creates the URL for the genre endpoint."""
    url = f"{base_url}/genre/{type.lower()}/{genre_id}"
    if page is not None:
        url += f'&page={page}'
    return url


def get_user_url(
    base_url: str,
    username: str,
    request: Optional[str],
    argument: Optional[Union[int, str]],
    page: Optional[int],
    parameters: Optional[Mapping[str, Any]],
) -> str:
    """Creates the URL for the user endpoint."""
    url = f"{base_url}/user/{username.lower()}"
    if request is not None:
        url += f"/{request}"
        if argument is not None:
            url += f"/{argument}"
        if page is not None:
            url += f'&page={page}'
    if parameters is not None:
        param_str = "&".join(f"{k}={v}" for k, v in parameters.items())
        url += f"?{param_str}"
    return url


def get_meta_url(
    base_url: str,
    request: str,
    type: Optional[str],
    period: Optional[str],
    offset: Optional[int],
) -> str:
    """Creates the URL for the meta endpoint."""
    url = f"{base_url}/meta/{request}"
    if type is not None and period is not None:
        url += f"/{type}/{period}"
    if page is not None:
        url += f'&page={page}'
    return url
