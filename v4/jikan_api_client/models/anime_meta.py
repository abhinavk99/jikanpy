from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_images import AnimeImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeMeta")


@attr.s(auto_attribs=True)
class AnimeMeta:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        images (Union[Unset, AnimeImages]):
        title (Union[Unset, str]): Entry title
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, AnimeImages] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if images is not UNSET:
            field_dict["images"] = images
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, AnimeImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = AnimeImages.from_dict(_images)

        title = d.pop("title", UNSET)

        anime_meta = cls(
            mal_id=mal_id,
            url=url,
            images=images,
            title=title,
        )

        anime_meta.additional_properties = d
        return anime_meta

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
