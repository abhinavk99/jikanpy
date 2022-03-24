from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.trailer_images_images import TrailerImagesImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="Trailer")


@attr.s(auto_attribs=True)
class Trailer:
    """Youtube Details

    Attributes:
        youtube_id (Union[Unset, None, str]): YouTube ID
        url (Union[Unset, None, str]): YouTube URL
        embed_url (Union[Unset, None, str]): Parsed Embed URL
        images (Union[Unset, TrailerImagesImages]):
    """

    youtube_id: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    embed_url: Union[Unset, None, str] = UNSET
    images: Union[Unset, TrailerImagesImages] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        youtube_id = self.youtube_id
        url = self.url
        embed_url = self.embed_url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if youtube_id is not UNSET:
            field_dict["youtube_id"] = youtube_id
        if url is not UNSET:
            field_dict["url"] = url
        if embed_url is not UNSET:
            field_dict["embed_url"] = embed_url
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        youtube_id = d.pop("youtube_id", UNSET)

        url = d.pop("url", UNSET)

        embed_url = d.pop("embed_url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, TrailerImagesImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = TrailerImagesImages.from_dict(_images)

        trailer = cls(
            youtube_id=youtube_id,
            url=url,
            embed_url=embed_url,
            images=images,
        )

        trailer.additional_properties = d
        return trailer

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
