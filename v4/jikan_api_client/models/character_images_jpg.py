from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CharacterImagesJpg")


@attr.s(auto_attribs=True)
class CharacterImagesJpg:
    """Available images in JPG

    Attributes:
        image_url (Union[Unset, None, str]): Image URL JPG
        small_image_url (Union[Unset, None, str]): Small Image URL JPG
    """

    image_url: Union[Unset, None, str] = UNSET
    small_image_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_url = self.image_url
        small_image_url = self.small_image_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if small_image_url is not UNSET:
            field_dict["small_image_url"] = small_image_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_url = d.pop("image_url", UNSET)

        small_image_url = d.pop("small_image_url", UNSET)

        character_images_jpg = cls(
            image_url=image_url,
            small_image_url=small_image_url,
        )

        character_images_jpg.additional_properties = d
        return character_images_jpg

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
