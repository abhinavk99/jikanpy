from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_characters_data_item_character import AnimeCharactersDataItemCharacter
from ..models.anime_characters_data_item_voice_actors_item import AnimeCharactersDataItemVoiceActorsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeCharactersDataItem")


@attr.s(auto_attribs=True)
class AnimeCharactersDataItem:
    """
    Attributes:
        character (Union[Unset, AnimeCharactersDataItemCharacter]): Character details
        role (Union[Unset, str]): Character's Role
        voice_actors (Union[Unset, List[AnimeCharactersDataItemVoiceActorsItem]]):
    """

    character: Union[Unset, AnimeCharactersDataItemCharacter] = UNSET
    role: Union[Unset, str] = UNSET
    voice_actors: Union[Unset, List[AnimeCharactersDataItemVoiceActorsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        character: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.character, Unset):
            character = self.character.to_dict()

        role = self.role
        voice_actors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.voice_actors, Unset):
            voice_actors = []
            for voice_actors_item_data in self.voice_actors:
                voice_actors_item = voice_actors_item_data.to_dict()

                voice_actors.append(voice_actors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if character is not UNSET:
            field_dict["character"] = character
        if role is not UNSET:
            field_dict["role"] = role
        if voice_actors is not UNSET:
            field_dict["voice_actors"] = voice_actors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _character = d.pop("character", UNSET)
        character: Union[Unset, AnimeCharactersDataItemCharacter]
        if isinstance(_character, Unset):
            character = UNSET
        else:
            character = AnimeCharactersDataItemCharacter.from_dict(_character)

        role = d.pop("role", UNSET)

        voice_actors = []
        _voice_actors = d.pop("voice_actors", UNSET)
        for voice_actors_item_data in _voice_actors or []:
            voice_actors_item = AnimeCharactersDataItemVoiceActorsItem.from_dict(voice_actors_item_data)

            voice_actors.append(voice_actors_item)

        anime_characters_data_item = cls(
            character=character,
            role=role,
            voice_actors=voice_actors,
        )

        anime_characters_data_item.additional_properties = d
        return anime_characters_data_item

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
