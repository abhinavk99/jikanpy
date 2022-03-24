from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_images import CommonImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeVideosDataEpisodesItem")


@attr.s(auto_attribs=True)
class AnimeVideosDataEpisodesItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        title (Union[Unset, str]): Title
        episode (Union[Unset, str]): Episode
        images (Union[Unset, CommonImages]):
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    episode: Union[Unset, str] = UNSET
    images: Union[Unset, CommonImages] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        title = self.title
        episode = self.episode
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if episode is not UNSET:
            field_dict["episode"] = episode
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        episode = d.pop("episode", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, CommonImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = CommonImages.from_dict(_images)

        anime_videos_data_episodes_item = cls(
            mal_id=mal_id,
            url=url,
            title=title,
            episode=episode,
            images=images,
        )

        anime_videos_data_episodes_item.additional_properties = d
        return anime_videos_data_episodes_item

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
