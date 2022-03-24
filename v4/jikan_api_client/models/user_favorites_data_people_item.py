from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.character_meta import CharacterMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFavoritesDataPeopleItem")


@attr.s(auto_attribs=True)
class UserFavoritesDataPeopleItem:
    """
    Attributes:
        field_ (Union[Unset, CharacterMeta]):
    """

    field_: Union[Unset, CharacterMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_, Unset):
            field_ = self.field_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_ is not UNSET:
            field_dict[""] = field_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _field_ = d.pop("", UNSET)
        field_: Union[Unset, CharacterMeta]
        if isinstance(_field_, Unset):
            field_ = UNSET
        else:
            field_ = CharacterMeta.from_dict(_field_)

        user_favorites_data_people_item = cls(
            field_=field_,
        )

        user_favorites_data_people_item.additional_properties = d
        return user_favorites_data_people_item

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
