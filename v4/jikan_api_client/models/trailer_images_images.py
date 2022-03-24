from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrailerImagesImages")


@attr.s(auto_attribs=True)
class TrailerImagesImages:
    """
    Attributes:
        default_image_url (Union[Unset, None, str]): Default Image Size URL (120x90)
        small_image_url (Union[Unset, None, str]): Small Image Size URL (640x480)
        medium_image_url (Union[Unset, None, str]): Medium Image Size URL (320x180)
        large_image_url (Union[Unset, None, str]): Large Image Size URL (480x360)
        maximum_image_url (Union[Unset, None, str]): Maximum Image Size URL (1280x720)
    """

    default_image_url: Union[Unset, None, str] = UNSET
    small_image_url: Union[Unset, None, str] = UNSET
    medium_image_url: Union[Unset, None, str] = UNSET
    large_image_url: Union[Unset, None, str] = UNSET
    maximum_image_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_image_url = self.default_image_url
        small_image_url = self.small_image_url
        medium_image_url = self.medium_image_url
        large_image_url = self.large_image_url
        maximum_image_url = self.maximum_image_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_image_url is not UNSET:
            field_dict["default_image_url"] = default_image_url
        if small_image_url is not UNSET:
            field_dict["small_image_url"] = small_image_url
        if medium_image_url is not UNSET:
            field_dict["medium_image_url"] = medium_image_url
        if large_image_url is not UNSET:
            field_dict["large_image_url"] = large_image_url
        if maximum_image_url is not UNSET:
            field_dict["maximum_image_url"] = maximum_image_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        default_image_url = d.pop("default_image_url", UNSET)

        small_image_url = d.pop("small_image_url", UNSET)

        medium_image_url = d.pop("medium_image_url", UNSET)

        large_image_url = d.pop("large_image_url", UNSET)

        maximum_image_url = d.pop("maximum_image_url", UNSET)

        trailer_images_images = cls(
            default_image_url=default_image_url,
            small_image_url=small_image_url,
            medium_image_url=medium_image_url,
            large_image_url=large_image_url,
            maximum_image_url=maximum_image_url,
        )

        trailer_images_images.additional_properties = d
        return trailer_images_images

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
