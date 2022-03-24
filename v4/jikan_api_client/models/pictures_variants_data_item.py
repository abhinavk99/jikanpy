from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_images import CommonImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="PicturesVariantsDataItem")


@attr.s(auto_attribs=True)
class PicturesVariantsDataItem:
    """
    Attributes:
        images (Union[Unset, CommonImages]):
    """

    images: Union[Unset, CommonImages] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _images = d.pop("images", UNSET)
        images: Union[Unset, CommonImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = CommonImages.from_dict(_images)

        pictures_variants_data_item = cls(
            images=images,
        )

        pictures_variants_data_item.additional_properties = d
        return pictures_variants_data_item

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
