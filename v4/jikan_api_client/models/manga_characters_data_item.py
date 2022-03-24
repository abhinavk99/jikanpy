from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.character_meta import CharacterMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="MangaCharactersDataItem")


@attr.s(auto_attribs=True)
class MangaCharactersDataItem:
    """
    Attributes:
        character (Union[Unset, CharacterMeta]):
        role (Union[Unset, str]): Character's Role
    """

    character: Union[Unset, CharacterMeta] = UNSET
    role: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        character: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.character, Unset):
            character = self.character.to_dict()

        role = self.role

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if character is not UNSET:
            field_dict["character"] = character
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _character = d.pop("character", UNSET)
        character: Union[Unset, CharacterMeta]
        if isinstance(_character, Unset):
            character = UNSET
        else:
            character = CharacterMeta.from_dict(_character)

        role = d.pop("role", UNSET)

        manga_characters_data_item = cls(
            character=character,
            role=role,
        )

        manga_characters_data_item.additional_properties = d
        return manga_characters_data_item

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
