from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_images_jpg import CommonImagesJpg
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommonImages")


@attr.s(auto_attribs=True)
class CommonImages:
    """
    Attributes:
        jpg (Union[Unset, CommonImagesJpg]): Available images in JPG
    """

    jpg: Union[Unset, CommonImagesJpg] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jpg, Unset):
            jpg = self.jpg.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jpg is not UNSET:
            field_dict["jpg"] = jpg

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _jpg = d.pop("jpg", UNSET)
        jpg: Union[Unset, CommonImagesJpg]
        if isinstance(_jpg, Unset):
            jpg = UNSET
        else:
            jpg = CommonImagesJpg.from_dict(_jpg)

        common_images = cls(
            jpg=jpg,
        )

        common_images.additional_properties = d
        return common_images

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
