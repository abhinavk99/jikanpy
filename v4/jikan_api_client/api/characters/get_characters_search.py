from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.characters_search import CharactersSearch
from ...models.characters_search_query_orderby import CharactersSearchQueryOrderby
from ...models.search_query_sort import SearchQuerySort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, CharactersSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/characters".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    json_order_by: Union[Unset, None, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value if order_by else None

    params["order_by"] = json_order_by

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["letter"] = letter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CharactersSearch]]:
    if response.status_code == 200:
        response_200 = CharactersSearch.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CharactersSearch]]:
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
    order_by: Union[Unset, None, CharactersSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, CharactersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        order_by (Union[Unset, None, CharactersSearchQueryOrderby]): Available Character order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, CharactersSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        order_by=order_by,
        sort=sort,
        letter=letter,
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
    order_by: Union[Unset, None, CharactersSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, CharactersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        order_by (Union[Unset, None, CharactersSearchQueryOrderby]): Available Character order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, CharactersSearch]]
    """

    return sync_detailed(
        client=client,
        q=q,
        order_by=order_by,
        sort=sort,
        letter=letter,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, CharactersSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, CharactersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        order_by (Union[Unset, None, CharactersSearchQueryOrderby]): Available Character order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, CharactersSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        order_by=order_by,
        sort=sort,
        letter=letter,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, CharactersSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, CharactersSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        order_by (Union[Unset, None, CharactersSearchQueryOrderby]): Available Character order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, CharactersSearch]]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            order_by=order_by,
            sort=sort,
            letter=letter,
        )
    ).parsed
