from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.people_images import PeopleImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeCharactersDataItemVoiceActorsItemPerson")


@attr.s(auto_attribs=True)
class AnimeCharactersDataItemVoiceActorsItemPerson:
    """
    Attributes:
        mal_id (Union[Unset, int]):
        url (Union[Unset, str]):
        images (Union[Unset, PeopleImages]):
        name (Union[Unset, str]):
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, PeopleImages] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        name = self.name

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, PeopleImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = PeopleImages.from_dict(_images)

        name = d.pop("name", UNSET)

        anime_characters_data_item_voice_actors_item_person = cls(
            mal_id=mal_id,
            url=url,
            images=images,
            name=name,
        )

        anime_characters_data_item_voice_actors_item_person.additional_properties = d
        return anime_characters_data_item_voice_actors_item_person

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
