from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonsDataItem")


@attr.s(auto_attribs=True)
class SeasonsDataItem:
    """
    Attributes:
        year (Union[Unset, int]): Year
        seasons (Union[Unset, List[str]]): List of available seasons
    """

    year: Union[Unset, int] = UNSET
    seasons: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        year = self.year
        seasons: Union[Unset, List[str]] = UNSET
        if not isinstance(self.seasons, Unset):
            seasons = self.seasons

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if year is not UNSET:
            field_dict["year"] = year
        if seasons is not UNSET:
            field_dict["seasons"] = seasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        year = d.pop("year", UNSET)

        seasons = cast(List[str], d.pop("seasons", UNSET))

        seasons_data_item = cls(
            year=year,
            seasons=seasons,
        )

        seasons_data_item.additional_properties = d
        return seasons_data_item

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
