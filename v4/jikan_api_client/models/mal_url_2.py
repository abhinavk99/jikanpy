from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MalUrl2")


@attr.s(auto_attribs=True)
class MalUrl2:
    """Parsed URL Data

    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        type (Union[Unset, str]): Type of resource
        title (Union[Unset, str]): Resource Name/Title
        url (Union[Unset, str]): MyAnimeList URL
    """

    mal_id: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        type = self.type
        title = self.title
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        type = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        url = d.pop("url", UNSET)

        mal_url_2 = cls(
            mal_id=mal_id,
            type=type,
            title=title,
            url=url,
        )

        mal_url_2.additional_properties = d
        return mal_url_2

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
