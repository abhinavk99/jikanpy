from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.user_friends import UserFriends
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{username}/friends".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UserFriends]]:
    if response.status_code == 200:
        response_200 = UserFriends.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UserFriends]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Client,
) -> Response[Union[Any, UserFriends]]:
    """
    Args:
        username (str):

    Returns:
        Response[Union[Any, UserFriends]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    username: str,
    *,
    client: Client,
) -> Optional[Union[Any, UserFriends]]:
    """
    Args:
        username (str):

    Returns:
        Response[Union[Any, UserFriends]]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
) -> Response[Union[Any, UserFriends]]:
    """
    Args:
        username (str):

    Returns:
        Response[Union[Any, UserFriends]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
) -> Optional[Union[Any, UserFriends]]:
    """
    Args:
        username (str):

    Returns:
        Response[Union[Any, UserFriends]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
