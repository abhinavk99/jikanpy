from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAboutDataItem")


@attr.s(auto_attribs=True)
class UserAboutDataItem:
    """
    Attributes:
        about (Union[Unset, None, str]): User About. NOTE: About information is customizable by users through BBCode on
            MyAnimeList. This means users can add multimedia content, different text sizes, etc. Due to this freeform, Jikan
            returns parsed HTML. Validate on your end!
    """

    about: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        about = self.about

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if about is not UNSET:
            field_dict["about"] = about

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        about = d.pop("about", UNSET)

        user_about_data_item = cls(
            about=about,
        )

        user_about_data_item.additional_properties = d
        return user_about_data_item

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
