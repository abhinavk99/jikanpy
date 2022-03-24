from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_characters_data_item_voice_actors_item_person import AnimeCharactersDataItemVoiceActorsItemPerson
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeCharactersDataItemVoiceActorsItem")


@attr.s(auto_attribs=True)
class AnimeCharactersDataItemVoiceActorsItem:
    """
    Attributes:
        person (Union[Unset, AnimeCharactersDataItemVoiceActorsItemPerson]):
        language (Union[Unset, str]):
    """

    person: Union[Unset, AnimeCharactersDataItemVoiceActorsItemPerson] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person is not UNSET:
            field_dict["person"] = person
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _person = d.pop("person", UNSET)
        person: Union[Unset, AnimeCharactersDataItemVoiceActorsItemPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = AnimeCharactersDataItemVoiceActorsItemPerson.from_dict(_person)

        language = d.pop("language", UNSET)

        anime_characters_data_item_voice_actors_item = cls(
            person=person,
            language=language,
        )

        anime_characters_data_item_voice_actors_item.additional_properties = d
        return anime_characters_data_item_voice_actors_item

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
