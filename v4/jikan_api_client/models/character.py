from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.character_images import CharacterImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="Character")


@attr.s(auto_attribs=True)
class Character:
    """Character Resource

    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        images (Union[Unset, CharacterImages]):
        name (Union[Unset, str]): Name
        name_kanji (Union[Unset, None, str]): Name
        nicknames (Union[Unset, List[str]]): Other Names
        favorites (Union[Unset, int]): Number of users who have favorited this entry
        about (Union[Unset, None, str]): Biography
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, CharacterImages] = UNSET
    name: Union[Unset, str] = UNSET
    name_kanji: Union[Unset, None, str] = UNSET
    nicknames: Union[Unset, List[str]] = UNSET
    favorites: Union[Unset, int] = UNSET
    about: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        name = self.name
        name_kanji = self.name_kanji
        nicknames: Union[Unset, List[str]] = UNSET
        if not isinstance(self.nicknames, Unset):
            nicknames = self.nicknames

        favorites = self.favorites
        about = self.about

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
        if name_kanji is not UNSET:
            field_dict["name_kanji"] = name_kanji
        if nicknames is not UNSET:
            field_dict["nicknames"] = nicknames
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if about is not UNSET:
            field_dict["about"] = about

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

        name_kanji = d.pop("name_kanji", UNSET)

        nicknames = cast(List[str], d.pop("nicknames", UNSET))

        favorites = d.pop("favorites", UNSET)

        about = d.pop("about", UNSET)

        character = cls(
            mal_id=mal_id,
            url=url,
            images=images,
            name=name,
            name_kanji=name_kanji,
            nicknames=nicknames,
            favorites=favorites,
            about=about,
        )

        character.additional_properties = d
        return character

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
