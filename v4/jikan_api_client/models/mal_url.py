from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MalUrl")


@attr.s(auto_attribs=True)
class MalUrl:
    """Parsed URL Data

    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        type (Union[Unset, str]): Type of resource
        name (Union[Unset, str]): Resource Name/Title
        url (Union[Unset, str]): MyAnimeList URL
    """

    mal_id: Union[Unset, int] = UNSET
    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        type = self.type
        name = self.name
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        mal_url = cls(
            mal_id=mal_id,
            type=type,
            name=name,
            url=url,
        )

        mal_url.additional_properties = d
        return mal_url

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
