from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.daterange_prop import DaterangeProp
from ..types import UNSET, Unset

T = TypeVar("T", bound="Daterange")


@attr.s(auto_attribs=True)
class Daterange:
    """Date range

    Attributes:
        from_ (Union[Unset, None, str]): Date ISO8601
        to (Union[Unset, None, str]): Date ISO8601
        prop (Union[Unset, DaterangeProp]): Date Prop
    """

    from_: Union[Unset, None, str] = UNSET
    to: Union[Unset, None, str] = UNSET
    prop: Union[Unset, DaterangeProp] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        to = self.to
        prop: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prop, Unset):
            prop = self.prop.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if prop is not UNSET:
            field_dict["prop"] = prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        _prop = d.pop("prop", UNSET)
        prop: Union[Unset, DaterangeProp]
        if isinstance(_prop, Unset):
            prop = UNSET
        else:
            prop = DaterangeProp.from_dict(_prop)

        daterange = cls(
            from_=from_,
            to=to,
            prop=prop,
        )

        daterange.additional_properties = d
        return daterange

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
