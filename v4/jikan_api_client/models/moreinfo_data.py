from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoreinfoData")


@attr.s(auto_attribs=True)
class MoreinfoData:
    """
    Attributes:
        moreinfo (Union[Unset, None, str]): Additional information on the entry
    """

    moreinfo: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        moreinfo = self.moreinfo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if moreinfo is not UNSET:
            field_dict["moreinfo"] = moreinfo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        moreinfo = d.pop("moreinfo", UNSET)

        moreinfo_data = cls(
            moreinfo=moreinfo,
        )

        moreinfo_data.additional_properties = d
        return moreinfo_data

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
