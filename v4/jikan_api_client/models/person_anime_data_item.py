from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_meta import AnimeMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonAnimeDataItem")


@attr.s(auto_attribs=True)
class PersonAnimeDataItem:
    """
    Attributes:
        position (Union[Unset, str]): Person's position
        anime (Union[Unset, AnimeMeta]):
    """

    position: Union[Unset, str] = UNSET
    anime: Union[Unset, AnimeMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        anime: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.anime, Unset):
            anime = self.anime.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if anime is not UNSET:
            field_dict["anime"] = anime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position", UNSET)

        _anime = d.pop("anime", UNSET)
        anime: Union[Unset, AnimeMeta]
        if isinstance(_anime, Unset):
            anime = UNSET
        else:
            anime = AnimeMeta.from_dict(_anime)

        person_anime_data_item = cls(
            position=position,
            anime=anime,
        )

        person_anime_data_item.additional_properties = d
        return person_anime_data_item

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
