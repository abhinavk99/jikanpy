from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DaterangePropTo")


@attr.s(auto_attribs=True)
class DaterangePropTo:
    """Date Prop To

    Attributes:
        day (Union[Unset, None, int]): Day
        month (Union[Unset, None, int]): Month
        year (Union[Unset, None, int]): Year
    """

    day: Union[Unset, None, int] = UNSET
    month: Union[Unset, None, int] = UNSET
    year: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day = self.day
        month = self.month
        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if month is not UNSET:
            field_dict["month"] = month
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        day = d.pop("day", UNSET)

        month = d.pop("month", UNSET)

        year = d.pop("year", UNSET)

        daterange_prop_to = cls(
            day=day,
            month=month,
            year=year,
        )

        daterange_prop_to.additional_properties = d
        return daterange_prop_to

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
