from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.manga_meta import MangaMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonMangaDataItem")


@attr.s(auto_attribs=True)
class PersonMangaDataItem:
    """
    Attributes:
        position (Union[Unset, str]): Person's position
        manga (Union[Unset, MangaMeta]):
    """

    position: Union[Unset, str] = UNSET
    manga: Union[Unset, MangaMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position = self.position
        manga: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manga, Unset):
            manga = self.manga.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if manga is not UNSET:
            field_dict["manga"] = manga

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position", UNSET)

        _manga = d.pop("manga", UNSET)
        manga: Union[Unset, MangaMeta]
        if isinstance(_manga, Unset):
            manga = UNSET
        else:
            manga = MangaMeta.from_dict(_manga)

        person_manga_data_item = cls(
            position=position,
            manga=manga,
        )

        person_manga_data_item.additional_properties = d
        return person_manga_data_item

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
