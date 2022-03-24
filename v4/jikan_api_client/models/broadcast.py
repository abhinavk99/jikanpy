from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Broadcast")


@attr.s(auto_attribs=True)
class Broadcast:
    """Broadcast Details

    Attributes:
        day (Union[Unset, None, str]): Day of the week
        time (Union[Unset, None, str]): Time in 24 hour format
        timezone (Union[Unset, None, str]): Timezone (Tz Database format
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
        string (Union[Unset, None, str]): Raw parsed broadcast string
    """

    day: Union[Unset, None, str] = UNSET
    time: Union[Unset, None, str] = UNSET
    timezone: Union[Unset, None, str] = UNSET
    string: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        day = self.day
        time = self.time
        timezone = self.timezone
        string = self.string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if time is not UNSET:
            field_dict["time"] = time
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if string is not UNSET:
            field_dict["string"] = string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        day = d.pop("day", UNSET)

        time = d.pop("time", UNSET)

        timezone = d.pop("timezone", UNSET)

        string = d.pop("string", UNSET)

        broadcast = cls(
            day=day,
            time=time,
            timezone=timezone,
            string=string,
        )

        broadcast.additional_properties = d
        return broadcast

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
