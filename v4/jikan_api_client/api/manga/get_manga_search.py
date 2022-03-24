from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.manga_search import MangaSearch
from ...models.manga_search_query_orderby import MangaSearchQueryOrderby
from ...models.manga_search_query_status import MangaSearchQueryStatus
from ...models.manga_search_query_type import MangaSearchQueryType
from ...models.search_query_sort import SearchQuerySort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    min_score: Union[Unset, None, float] = UNSET,
    max_score: Union[Unset, None, float] = UNSET,
    status: Union[Unset, None, MangaSearchQueryStatus] = UNSET,
    sfw: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, str] = UNSET,
    genres_exclude: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, MangaSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
    magazines: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/manga".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["q"] = q

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params["score"] = score

    params["min_score"] = min_score

    params["max_score"] = max_score

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

    params["sfw"] = sfw

    params["genres"] = genres

    params["genres_exclude"] = genres_exclude

    json_order_by: Union[Unset, None, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value if order_by else None

    params["order_by"] = json_order_by

    json_sort: Union[Unset, None, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value if sort else None

    params["sort"] = json_sort

    params["letter"] = letter

    params["magazines"] = magazines

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
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    min_score: Union[Unset, None, float] = UNSET,
    max_score: Union[Unset, None, float] = UNSET,
    status: Union[Unset, None, MangaSearchQueryStatus] = UNSET,
    sfw: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, str] = UNSET,
    genres_exclude: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, MangaSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
    magazines: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, MangaSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        score (Union[Unset, None, float]):
        min_score (Union[Unset, None, float]):
        max_score (Union[Unset, None, float]):
        status (Union[Unset, None, MangaSearchQueryStatus]): Available Manga statuses
        sfw (Union[Unset, None, bool]):
        genres (Union[Unset, None, str]):
        genres_exclude (Union[Unset, None, str]):
        order_by (Union[Unset, None, MangaSearchQueryOrderby]): Available Manga order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):
        magazines (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        type=type,
        score=score,
        min_score=min_score,
        max_score=max_score,
        status=status,
        sfw=sfw,
        genres=genres,
        genres_exclude=genres_exclude,
        order_by=order_by,
        sort=sort,
        letter=letter,
        magazines=magazines,
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
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    min_score: Union[Unset, None, float] = UNSET,
    max_score: Union[Unset, None, float] = UNSET,
    status: Union[Unset, None, MangaSearchQueryStatus] = UNSET,
    sfw: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, str] = UNSET,
    genres_exclude: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, MangaSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
    magazines: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, MangaSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        score (Union[Unset, None, float]):
        min_score (Union[Unset, None, float]):
        max_score (Union[Unset, None, float]):
        status (Union[Unset, None, MangaSearchQueryStatus]): Available Manga statuses
        sfw (Union[Unset, None, bool]):
        genres (Union[Unset, None, str]):
        genres_exclude (Union[Unset, None, str]):
        order_by (Union[Unset, None, MangaSearchQueryOrderby]): Available Manga order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):
        magazines (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    return sync_detailed(
        client=client,
        q=q,
        type=type,
        score=score,
        min_score=min_score,
        max_score=max_score,
        status=status,
        sfw=sfw,
        genres=genres,
        genres_exclude=genres_exclude,
        order_by=order_by,
        sort=sort,
        letter=letter,
        magazines=magazines,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    min_score: Union[Unset, None, float] = UNSET,
    max_score: Union[Unset, None, float] = UNSET,
    status: Union[Unset, None, MangaSearchQueryStatus] = UNSET,
    sfw: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, str] = UNSET,
    genres_exclude: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, MangaSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
    magazines: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, MangaSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        score (Union[Unset, None, float]):
        min_score (Union[Unset, None, float]):
        max_score (Union[Unset, None, float]):
        status (Union[Unset, None, MangaSearchQueryStatus]): Available Manga statuses
        sfw (Union[Unset, None, bool]):
        genres (Union[Unset, None, str]):
        genres_exclude (Union[Unset, None, str]):
        order_by (Union[Unset, None, MangaSearchQueryOrderby]): Available Manga order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):
        magazines (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    kwargs = _get_kwargs(
        client=client,
        q=q,
        type=type,
        score=score,
        min_score=min_score,
        max_score=max_score,
        status=status,
        sfw=sfw,
        genres=genres,
        genres_exclude=genres_exclude,
        order_by=order_by,
        sort=sort,
        letter=letter,
        magazines=magazines,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, MangaSearchQueryType] = UNSET,
    score: Union[Unset, None, float] = UNSET,
    min_score: Union[Unset, None, float] = UNSET,
    max_score: Union[Unset, None, float] = UNSET,
    status: Union[Unset, None, MangaSearchQueryStatus] = UNSET,
    sfw: Union[Unset, None, bool] = UNSET,
    genres: Union[Unset, None, str] = UNSET,
    genres_exclude: Union[Unset, None, str] = UNSET,
    order_by: Union[Unset, None, MangaSearchQueryOrderby] = UNSET,
    sort: Union[Unset, None, SearchQuerySort] = UNSET,
    letter: Union[Unset, None, str] = UNSET,
    magazines: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, MangaSearch]]:
    """
    Args:
        q (Union[Unset, None, str]):
        type (Union[Unset, None, MangaSearchQueryType]): Available Manga types
        score (Union[Unset, None, float]):
        min_score (Union[Unset, None, float]):
        max_score (Union[Unset, None, float]):
        status (Union[Unset, None, MangaSearchQueryStatus]): Available Manga statuses
        sfw (Union[Unset, None, bool]):
        genres (Union[Unset, None, str]):
        genres_exclude (Union[Unset, None, str]):
        order_by (Union[Unset, None, MangaSearchQueryOrderby]): Available Manga order_by
            properties
        sort (Union[Unset, None, SearchQuerySort]): Characters Search Query Sort
        letter (Union[Unset, None, str]):
        magazines (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, MangaSearch]]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            type=type,
            score=score,
            min_score=min_score,
            max_score=max_score,
            status=status,
            sfw=sfw,
            genres=genres,
            genres_exclude=genres_exclude,
            order_by=order_by,
            sort=sort,
            letter=letter,
            magazines=magazines,
        )
    ).parsed
