from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_schedules_filter import GetSchedulesFilter
from ...models.schedules import Schedules
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filter_: Union[Unset, None, GetSchedulesFilter] = UNSET,
) -> Dict[str, Any]:
    url = "{}/schedules".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Schedules]]:
    if response.status_code == 200:
        response_200 = Schedules.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Schedules]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filter_: Union[Unset, None, GetSchedulesFilter] = UNSET,
) -> Response[Union[Any, Schedules]]:
    """
    Args:
        filter_ (Union[Unset, None, GetSchedulesFilter]):

    Returns:
        Response[Union[Any, Schedules]]
    """

    kwargs = _get_kwargs(
        client=client,
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
    filter_: Union[Unset, None, GetSchedulesFilter] = UNSET,
) -> Optional[Union[Any, Schedules]]:
    """
    Args:
        filter_ (Union[Unset, None, GetSchedulesFilter]):

    Returns:
        Response[Union[Any, Schedules]]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filter_: Union[Unset, None, GetSchedulesFilter] = UNSET,
) -> Response[Union[Any, Schedules]]:
    """
    Args:
        filter_ (Union[Unset, None, GetSchedulesFilter]):

    Returns:
        Response[Union[Any, Schedules]]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    filter_: Union[Unset, None, GetSchedulesFilter] = UNSET,
) -> Optional[Union[Any, Schedules]]:
    """
    Args:
        filter_ (Union[Unset, None, GetSchedulesFilter]):

    Returns:
        Response[Union[Any, Schedules]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
        )
    ).parsed
