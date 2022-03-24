from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserClubsDataItem")


@attr.s(auto_attribs=True)
class UserClubsDataItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        name (Union[Unset, str]): Club Name
        url (Union[Unset, str]): Club URL
    """

    mal_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        name = self.name
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        user_clubs_data_item = cls(
            mal_id=mal_id,
            name=name,
            url=url,
        )

        user_clubs_data_item.additional_properties = d
        return user_clubs_data_item

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
