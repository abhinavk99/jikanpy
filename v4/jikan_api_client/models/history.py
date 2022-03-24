from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.mal_url import MalUrl
from ..types import UNSET, Unset

T = TypeVar("T", bound="History")


@attr.s(auto_attribs=True)
class History:
    """Transform the resource into an array.

    Attributes:
        entry (Union[Unset, MalUrl]): Parsed URL Data
        increment (Union[Unset, int]): Number of episodes/chapters watched/read
        date (Union[Unset, str]): Date ISO8601
    """

    entry: Union[Unset, MalUrl] = UNSET
    increment: Union[Unset, int] = UNSET
    date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        increment = self.increment
        date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry
        if increment is not UNSET:
            field_dict["increment"] = increment
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, MalUrl]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = MalUrl.from_dict(_entry)

        increment = d.pop("increment", UNSET)

        date = d.pop("date", UNSET)

        history = cls(
            entry=entry,
            increment=increment,
            date=date,
        )

        history.additional_properties = d
        return history

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
