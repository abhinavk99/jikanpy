from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.daterange_prop_from import DaterangePropFrom
from ..models.daterange_prop_to import DaterangePropTo
from ..types import UNSET, Unset

T = TypeVar("T", bound="DaterangeProp")


@attr.s(auto_attribs=True)
class DaterangeProp:
    """Date Prop

    Attributes:
        from_ (Union[Unset, DaterangePropFrom]): Date Prop From
        to (Union[Unset, DaterangePropTo]): Date Prop To
        string (Union[Unset, None, str]): Raw parsed string
    """

    from_: Union[Unset, DaterangePropFrom] = UNSET
    to: Union[Unset, DaterangePropTo] = UNSET
    string: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        string = self.string

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if string is not UNSET:
            field_dict["string"] = string

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, DaterangePropFrom]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = DaterangePropFrom.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, DaterangePropTo]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = DaterangePropTo.from_dict(_to)

        string = d.pop("string", UNSET)

        daterange_prop = cls(
            from_=from_,
            to=to,
            string=string,
        )

        daterange_prop.additional_properties = d
        return daterange_prop

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
