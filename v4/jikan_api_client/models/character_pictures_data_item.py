from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CharacterPicturesDataItem")


@attr.s(auto_attribs=True)
class CharacterPicturesDataItem:
    """
    Attributes:
        image_url (Union[Unset, None, str]): Default JPG Image Size URL
        large_image_url (Union[Unset, None, str]): Large JPG Image Size URL
    """

    image_url: Union[Unset, None, str] = UNSET
    large_image_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_url = self.image_url
        large_image_url = self.large_image_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if large_image_url is not UNSET:
            field_dict["large_image_url"] = large_image_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_url = d.pop("image_url", UNSET)

        large_image_url = d.pop("large_image_url", UNSET)

        character_pictures_data_item = cls(
            image_url=image_url,
            large_image_url=large_image_url,
        )

        character_pictures_data_item.additional_properties = d
        return character_pictures_data_item

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
