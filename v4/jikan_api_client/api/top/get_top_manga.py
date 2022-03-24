from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_top_manga_filter import GetTopMangaFilter
from ...models.manga_search import MangaSearch
from ...models.manga_search_query_type import MangaSearchQueryType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    filter_: Union[Unset, None, GetTopMangaFilter] = UNSET,
) -> Dict[str, Any]:
    url = "{}/top/manga".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, MangaSearch]]:
    if response.status_code == 200:
        response_200 = MangaSearch.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, MangaSearch]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    filter_: Union[Unset, None, GetTopMangaFilter] = UNSET,
) -> Response[Union[Any, MangaSearch]]:
    """
    Args:
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        filter_ (Union[Unset, None, GetTopMangaFilter]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
        filter_=filter_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    filter_: Union[Unset, None, GetTopMangaFilter] = UNSET,
) -> Optional[Union[Any, MangaSearch]]:
    """
    Args:
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        filter_ (Union[Unset, None, GetTopMangaFilter]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    return sync_detailed(
        client=client,
        type=type,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    filter_: Union[Unset, None, GetTopMangaFilter] = UNSET,
) -> Response[Union[Any, MangaSearch]]:
    """
    Args:
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        filter_ (Union[Unset, None, GetTopMangaFilter]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        type=type,
        filter_=filter_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    filter_: Union[Unset, None, GetTopMangaFilter] = UNSET,
) -> Optional[Union[Any, MangaSearch]]:
    """
    Args:
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        filter_ (Union[Unset, None, GetTopMangaFilter]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
            filter_=filter_,
        )
    ).parsed
