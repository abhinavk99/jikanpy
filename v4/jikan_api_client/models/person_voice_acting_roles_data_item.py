from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_meta import AnimeMeta
from ..models.character_meta import CharacterMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonVoiceActingRolesDataItem")


@attr.s(auto_attribs=True)
class PersonVoiceActingRolesDataItem:
    """
    Attributes:
        role (Union[Unset, str]): Person's Character's role in the anime
        anime (Union[Unset, AnimeMeta]):
        character (Union[Unset, CharacterMeta]):
    """

    role: Union[Unset, str] = UNSET
    anime: Union[Unset, AnimeMeta] = UNSET
    character: Union[Unset, CharacterMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role
        anime: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.anime, Unset):
            anime = self.anime.to_dict()

        character: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.character, Unset):
            character = self.character.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if anime is not UNSET:
            field_dict["anime"] = anime
        if character is not UNSET:
            field_dict["character"] = character

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = d.pop("role", UNSET)

        _anime = d.pop("anime", UNSET)
        anime: Union[Unset, AnimeMeta]
        if isinstance(_anime, Unset):
            anime = UNSET
        else:
            anime = AnimeMeta.from_dict(_anime)

        _character = d.pop("character", UNSET)
        character: Union[Unset, CharacterMeta]
        if isinstance(_character, Unset):
            character = UNSET
        else:
            character = CharacterMeta.from_dict(_character)

        person_voice_acting_roles_data_item = cls(
            role=role,
            anime=anime,
            character=character,
        )

        person_voice_acting_roles_data_item.additional_properties = d
        return person_voice_acting_roles_data_item

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
