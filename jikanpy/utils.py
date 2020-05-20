from typing import Optional, Dict, Mapping, Union

import aiohttp
import requests

from jikanpy.exceptions import APIException

BASE_URL = "https://api.jikan.moe/v3"
SEASON_ARCHIVE_URL = f"{BASE_URL}/season/archive"
SEASON_LATER_URL = f"{BASE_URL}/season/later"


def check_response(
    response_dict: Dict, response_status_code: int, **kwargs: Union[int, Optional[str]],
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


def add_jikan_metadata(
    response: Union[requests.Response, aiohttp.ClientResponse],
    response_dict: Dict,
    url: str,
) -> Dict:
    """Adds the response headers and jikan endpoint url to response dictionary"""
    response_dict["jikan_url"] = url
    # dict() is to convert from CIMultiDictProxy for aiohttp.ClientResponse
    response_dict["headers"] = dict(response.headers)
    return response_dict


def get_url_with_page(url: str, page: Optional[int], delimiter: str = "/") -> str:
    """Add page to URL if it exists"""
    return url if page is None else f"{url}{delimiter}{page}"


def get_main_url(
    endpoint: str, id: int, extension: Optional[str], page: Optional[int]
) -> str:
    """Create URL for anime, manga, character, person, and club endpoints"""
    url = f"{BASE_URL}/{endpoint}/{id}"
    if extension is not None:
        url += f"/{extension}"
        url = get_url_with_page(url, page)
    return url


def get_creator_url(creator_type: str, creator_id: int, page: Optional[int]) -> str:
    """Create URL for producer and magazine endpoints"""
    url = f"{BASE_URL}/{creator_type}/{creator_id}"
    return get_url_with_page(url, page)


def get_search_url(
    search_type: str,
    query: str,
    page: Optional[int],
    parameters: Optional[Mapping[str, Optional[Union[int, str, float]]]],
) -> str:
    """Create URL for search endpoint"""
    url = f"{BASE_URL}/search/{search_type}?q={query}"
    url = get_url_with_page(url, page, delimiter="&page=")
    if parameters is not None:
        url += "".join(f"&{k}={v}" for k, v in parameters.items())
    return url


def get_season_url(year: int, season: str) -> str:
    """Create URL for season endpoint"""
    return f"{BASE_URL}/season/{year}/{season.lower()}"


def get_schedule_url(day: Optional[str]) -> str:
    """Create URL for schedule endpoint"""
    base_schedule_url = f"{BASE_URL}/schedule"
    return base_schedule_url if day is None else f"{base_schedule_url}/{day.lower()}"


def get_top_url(type: str, page: Optional[int], subtype: Optional[str]) -> str:
    """Create URL for top endpoint"""
    url = f"{BASE_URL}/top/{type.lower()}"
    url = get_url_with_page(url, page)
    return url if subtype is None else f"{url}/{subtype.lower()}"


def get_genre_url(type: str, genre_id: int, page: Optional[int]) -> str:
    """Create URL for genre endpoint"""
    url = f"{BASE_URL}/genre/{type.lower()}/{genre_id}"
    return get_url_with_page(url, page)


def get_user_url(
    username: str,
    request: Optional[str],
    argument: Optional[Union[int, str]],
    page: Optional[int],
    parameters: Optional[Mapping],
) -> str:
    """Create URL for user endpoint"""
    url = f"{BASE_URL}/user/{username.lower()}"
    if request is not None:
        url += f"/{request}"
        if argument is not None:
            url += f"/{argument}"
        url = get_url_with_page(url, page)
    if parameters is not None:
        param_str = "&".join(f"{k}={v}" for k, v in parameters.items())
        url += f"?{param_str}"
    return url


def get_meta_url(
    request: str, type: Optional[str], period: Optional[str], offset: Optional[int],
) -> str:
    """Create URL for meta endpoint"""
    url = f"{BASE_URL}/meta/{request}"
    if type is not None and period is not None:
        url += f"/{type}/{period}"
    return get_url_with_page(url, offset)
