from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_user_history_type import GetUserHistoryType
from ...models.user_history import UserHistory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    client: Client,
    type: Union[Unset, None, GetUserHistoryType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/{username}/history".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UserHistory]]:
    if response.status_code == 200:
        response_200 = UserHistory.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UserHistory]]:
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
    type: Union[Unset, None, GetUserHistoryType] = UNSET,
) -> Response[Union[Any, UserHistory]]:
    """
    Args:
        username (str):
        type (Union[Unset, None, GetUserHistoryType]):

    Returns:
        Response[Union[Any, UserHistory]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        type=type,
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
    type: Union[Unset, None, GetUserHistoryType] = UNSET,
) -> Optional[Union[Any, UserHistory]]:
    """
    Args:
        username (str):
        type (Union[Unset, None, GetUserHistoryType]):

    Returns:
        Response[Union[Any, UserHistory]]
    """

    return sync_detailed(
        username=username,
        client=client,
        type=type,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    type: Union[Unset, None, GetUserHistoryType] = UNSET,
) -> Response[Union[Any, UserHistory]]:
    """
    Args:
        username (str):
        type (Union[Unset, None, GetUserHistoryType]):

    Returns:
        Response[Union[Any, UserHistory]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
    type: Union[Unset, None, GetUserHistoryType] = UNSET,
) -> Optional[Union[Any, UserHistory]]:
    """
    Args:
        username (str):
        type (Union[Unset, None, GetUserHistoryType]):

    Returns:
        Response[Union[Any, UserHistory]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            type=type,
        )
    ).parsed
