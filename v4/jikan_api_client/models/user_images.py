from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_images_jpg import UserImagesJpg
from ..models.user_images_webp import UserImagesWebp
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserImages")


@attr.s(auto_attribs=True)
class UserImages:
    """
    Attributes:
        jpg (Union[Unset, UserImagesJpg]): Available images in JPG
        webp (Union[Unset, UserImagesWebp]): Available images in WEBP
    """

    jpg: Union[Unset, UserImagesJpg] = UNSET
    webp: Union[Unset, UserImagesWebp] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jpg, Unset):
            jpg = self.jpg.to_dict()

        webp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.webp, Unset):
            webp = self.webp.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jpg is not UNSET:
            field_dict["jpg"] = jpg
        if webp is not UNSET:
            field_dict["webp"] = webp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _jpg = d.pop("jpg", UNSET)
        jpg: Union[Unset, UserImagesJpg]
        if isinstance(_jpg, Unset):
            jpg = UNSET
        else:
            jpg = UserImagesJpg.from_dict(_jpg)

        _webp = d.pop("webp", UNSET)
        webp: Union[Unset, UserImagesWebp]
        if isinstance(_webp, Unset):
            webp = UNSET
        else:
            webp = UserImagesWebp.from_dict(_webp)

        user_images = cls(
            jpg=jpg,
            webp=webp,
        )

        user_images.additional_properties = d
        return user_images

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
