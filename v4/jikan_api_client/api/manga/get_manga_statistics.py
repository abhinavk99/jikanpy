from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.manga_statistics import MangaStatistics
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/manga/{id}/statistics".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, MangaStatistics]]:
    if response.status_code == 200:
        response_200 = MangaStatistics.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, MangaStatistics]]:
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
) -> Response[Union[Any, MangaStatistics]]:
    """
    Args:
        id (int):

    Returns:
        Response[Union[Any, MangaStatistics]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
) -> Optional[Union[Any, MangaStatistics]]:
    """
    Args:
        id (int):

    Returns:
        Response[Union[Any, MangaStatistics]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
) -> Response[Union[Any, MangaStatistics]]:
    """
    Args:
        id (int):

    Returns:
        Response[Union[Any, MangaStatistics]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
) -> Optional[Union[Any, MangaStatistics]]:
    """
    Args:
        id (int):

    Returns:
        Response[Union[Any, MangaStatistics]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
