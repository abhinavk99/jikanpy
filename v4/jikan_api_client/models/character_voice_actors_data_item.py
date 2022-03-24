from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.person_meta import PersonMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="CharacterVoiceActorsDataItem")


@attr.s(auto_attribs=True)
class CharacterVoiceActorsDataItem:
    """
    Attributes:
        language (Union[Unset, str]): Character's Role
        person (Union[Unset, PersonMeta]):
    """

    language: Union[Unset, str] = UNSET
    person: Union[Unset, PersonMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language = self.language
        person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if person is not UNSET:
            field_dict["person"] = person

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language = d.pop("language", UNSET)

        _person = d.pop("person", UNSET)
        person: Union[Unset, PersonMeta]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = PersonMeta.from_dict(_person)

        character_voice_actors_data_item = cls(
            language=language,
            person=person,
        )

        character_voice_actors_data_item.additional_properties = d
        return character_voice_actors_data_item

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
