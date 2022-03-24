from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WatchEpisodesDataItemEpisodesItem")


@attr.s(auto_attribs=True)
class WatchEpisodesDataItemEpisodesItem:
    """
    Attributes:
        mal_id (Union[Unset, str]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        title (Union[Unset, str]): Episode Title
        premium (Union[Unset, bool]): For MyAnimeList Premium Users
    """

    mal_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    premium: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        title = self.title
        premium = self.premium

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if premium is not UNSET:
            field_dict["premium"] = premium

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        premium = d.pop("premium", UNSET)

        watch_episodes_data_item_episodes_item = cls(
            mal_id=mal_id,
            url=url,
            title=title,
            premium=premium,
        )

        watch_episodes_data_item_episodes_item.additional_properties = d
        return watch_episodes_data_item_episodes_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
