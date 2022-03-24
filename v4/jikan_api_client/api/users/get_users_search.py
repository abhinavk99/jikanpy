from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.users_search import UsersSearch
from ...models.users_search_query_gender import UsersSearchQueryGender
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    gender: Union[Unset, None, UsersSearchQueryGender] = UNSET,
    location: Union[Unset, None, str] = UNSET,
    max_age: Union[Unset, None, int] = UNSET,
    min_age: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    json_gender: Union[Unset, None, str] = UNSET
    if not isinstance(gender, Unset):
        json_gender = gender.value if gender else None

    params["gender"] = json_gender

    params["location"] = location

    params["maxAge"] = max_age

    params["minAge"] = min_age

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UsersSearch]]:
    if response.status_code == 200:
        response_200 = UsersSearch.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UsersSearch]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    gender: Union[Unset, None, UsersSearchQueryGender] = UNSET,
    location: Union[Unset, None, str] = UNSET,
    max_age: Union[Unset, None, int] = UNSET,
    min_age: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, UsersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        gender (Union[Unset, None, UsersSearchQueryGender]): Users Search Query Gender
        location (Union[Unset, None, str]):
        max_age (Union[Unset, None, int]):
        min_age (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, UsersSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        gender=gender,
        location=location,
        max_age=max_age,
        min_age=min_age,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    gender: Union[Unset, None, UsersSearchQueryGender] = UNSET,
    location: Union[Unset, None, str] = UNSET,
    max_age: Union[Unset, None, int] = UNSET,
    min_age: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, UsersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        gender (Union[Unset, None, UsersSearchQueryGender]): Users Search Query Gender
        location (Union[Unset, None, str]):
        max_age (Union[Unset, None, int]):
        min_age (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, UsersSearch]]
    """

    return sync_detailed(
        client=client,
        q=q,
        gender=gender,
        location=location,
        max_age=max_age,
        min_age=min_age,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    gender: Union[Unset, None, UsersSearchQueryGender] = UNSET,
    location: Union[Unset, None, str] = UNSET,
    max_age: Union[Unset, None, int] = UNSET,
    min_age: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, UsersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        gender (Union[Unset, None, UsersSearchQueryGender]): Users Search Query Gender
        location (Union[Unset, None, str]):
        max_age (Union[Unset, None, int]):
        min_age (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, UsersSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        gender=gender,
        location=location,
        max_age=max_age,
        min_age=min_age,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    gender: Union[Unset, None, UsersSearchQueryGender] = UNSET,
    location: Union[Unset, None, str] = UNSET,
    max_age: Union[Unset, None, int] = UNSET,
    min_age: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, UsersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        gender (Union[Unset, None, UsersSearchQueryGender]): Users Search Query Gender
        location (Union[Unset, None, str]):
        max_age (Union[Unset, None, int]):
        min_age (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, UsersSearch]]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            gender=gender,
            location=location,
            max_age=max_age,
            min_age=min_age,
        )
    ).parsed
