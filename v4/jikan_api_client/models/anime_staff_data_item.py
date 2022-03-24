from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.anime_staff_data_item_person import AnimeStaffDataItemPerson
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeStaffDataItem")


@attr.s(auto_attribs=True)
class AnimeStaffDataItem:
    """
    Attributes:
        person (Union[Unset, AnimeStaffDataItemPerson]): Person details
        positions (Union[Unset, List[str]]): Staff Positions
    """

    person: Union[Unset, AnimeStaffDataItemPerson] = UNSET
    positions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        positions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.positions, Unset):
            positions = self.positions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person is not UNSET:
            field_dict["person"] = person
        if positions is not UNSET:
            field_dict["positions"] = positions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _person = d.pop("person", UNSET)
        person: Union[Unset, AnimeStaffDataItemPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = AnimeStaffDataItemPerson.from_dict(_person)

        positions = cast(List[str], d.pop("positions", UNSET))

        anime_staff_data_item = cls(
            person=person,
            positions=positions,
        )

        anime_staff_data_item.additional_properties = d
        return anime_staff_data_item

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
