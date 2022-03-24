from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.forum import Forum
from ...models.get_anime_forum_filter import GetAnimeForumFilter
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    filter_: Union[Unset, None, GetAnimeForumFilter] = UNSET,
) -> Dict[str, Any]:
    url = "{}/anime/{id}/forum".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_filter_: Union[Unset, None, str] = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value if filter_ else None

    params["filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Forum]]:
    if response.status_code == 200:
        response_200 = Forum.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Forum]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    filter_: Union[Unset, None, GetAnimeForumFilter] = UNSET,
) -> Response[Union[Any, Forum]]:
    """
    Args:
        id (int):
        filter_ (Union[Unset, None, GetAnimeForumFilter]):

    Returns:
        Response[Union[Any, Forum]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        filter_=filter_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: Client,
    filter_: Union[Unset, None, GetAnimeForumFilter] = UNSET,
) -> Optional[Union[Any, Forum]]:
    """
    Args:
        id (int):
        filter_ (Union[Unset, None, GetAnimeForumFilter]):

    Returns:
        Response[Union[Any, Forum]]
    """

    return sync_detailed(
        id=id,
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    filter_: Union[Unset, None, GetAnimeForumFilter] = UNSET,
) -> Response[Union[Any, Forum]]:
    """
    Args:
        id (int):
        filter_ (Union[Unset, None, GetAnimeForumFilter]):

    Returns:
        Response[Union[Any, Forum]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        filter_=filter_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    filter_: Union[Unset, None, GetAnimeForumFilter] = UNSET,
) -> Optional[Union[Any, Forum]]:
    """
    Args:
        id (int):
        filter_ (Union[Unset, None, GetAnimeForumFilter]):

    Returns:
        Response[Union[Any, Forum]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            filter_=filter_,
        )
    ).parsed
