from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.club_relations_data import ClubRelationsData
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClubRelations")


@attr.s(auto_attribs=True)
class ClubRelations:
    """Club Relations

    Attributes:
        data (Union[Unset, ClubRelationsData]):
    """

    data: Union[Unset, ClubRelationsData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, ClubRelationsData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ClubRelationsData.from_dict(_data)

        club_relations = cls(
            data=data,
        )

        club_relations.additional_properties = d
        return club_relations

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
