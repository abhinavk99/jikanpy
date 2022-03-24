from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.character_images import CharacterImages
from ..models.mal_url_2 import MalUrl2
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFavoritesDataCharactersItem")


@attr.s(auto_attribs=True)
class UserFavoritesDataCharactersItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        images (Union[Unset, CharacterImages]):
        name (Union[Unset, str]): Entry name
        field_ (Union[Unset, MalUrl2]): Parsed URL Data
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, CharacterImages] = UNSET
    name: Union[Unset, str] = UNSET
    field_: Union[Unset, MalUrl2] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        name = self.name
        field_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_, Unset):
            field_ = self.field_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if images is not UNSET:
            field_dict["images"] = images
        if name is not UNSET:
            field_dict["name"] = name
        if field_ is not UNSET:
            field_dict[""] = field_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, CharacterImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = CharacterImages.from_dict(_images)

        name = d.pop("name", UNSET)

        _field_ = d.pop("", UNSET)
        field_: Union[Unset, MalUrl2]
        if isinstance(_field_, Unset):
            field_ = UNSET
        else:
            field_ = MalUrl2.from_dict(_field_)

        user_favorites_data_characters_item = cls(
            mal_id=mal_id,
            url=url,
            images=images,
            name=name,
            field_=field_,
        )

        user_favorites_data_characters_item.additional_properties = d
        return user_favorites_data_characters_item

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
