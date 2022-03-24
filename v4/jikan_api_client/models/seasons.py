from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.seasons_data_item import SeasonsDataItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Seasons")


@attr.s(auto_attribs=True)
class Seasons:
    """List of available seasons

    Attributes:
        data (Union[Unset, List[SeasonsDataItem]]):
    """

    data: Union[Unset, List[SeasonsDataItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = SeasonsDataItem.from_dict(data_item_data)

            data.append(data_item)

        seasons = cls(
            data=data,
        )

        seasons.additional_properties = d
        return seasons

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
