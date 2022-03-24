from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.users_temp_data_item_images_jpg import UsersTempDataItemImagesJpg
from ..models.users_temp_data_item_images_webp import UsersTempDataItemImagesWebp
from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersTempDataItemImages")


@attr.s(auto_attribs=True)
class UsersTempDataItemImages:
    """Images

    Attributes:
        jpg (Union[Unset, UsersTempDataItemImagesJpg]): Available images in JPG
        webp (Union[Unset, UsersTempDataItemImagesWebp]): Available images in WEBP
    """

    jpg: Union[Unset, UsersTempDataItemImagesJpg] = UNSET
    webp: Union[Unset, UsersTempDataItemImagesWebp] = UNSET
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
        jpg: Union[Unset, UsersTempDataItemImagesJpg]
        if isinstance(_jpg, Unset):
            jpg = UNSET
        else:
            jpg = UsersTempDataItemImagesJpg.from_dict(_jpg)

        _webp = d.pop("webp", UNSET)
        webp: Union[Unset, UsersTempDataItemImagesWebp]
        if isinstance(_webp, Unset):
            webp = UNSET
        else:
            webp = UsersTempDataItemImagesWebp.from_dict(_webp)

        users_temp_data_item_images = cls(
            jpg=jpg,
            webp=webp,
        )

        users_temp_data_item_images.additional_properties = d
        return users_temp_data_item_images

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
