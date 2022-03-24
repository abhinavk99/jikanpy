from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.mal_url import MalUrl
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeRelationsDataItem")


@attr.s(auto_attribs=True)
class AnimeRelationsDataItem:
    """
    Attributes:
        relation (Union[Unset, str]): Relation type
        entry (Union[Unset, List[MalUrl]]):
    """

    relation: Union[Unset, str] = UNSET
    entry: Union[Unset, List[MalUrl]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relation = self.relation
        entry: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = []
            for entry_item_data in self.entry:
                entry_item = entry_item_data.to_dict()

                entry.append(entry_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relation is not UNSET:
            field_dict["relation"] = relation
        if entry is not UNSET:
            field_dict["entry"] = entry

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        relation = d.pop("relation", UNSET)

        entry = []
        _entry = d.pop("entry", UNSET)
        for entry_item_data in _entry or []:
            entry_item = MalUrl.from_dict(entry_item_data)

            entry.append(entry_item)

        anime_relations_data_item = cls(
            relation=relation,
            entry=entry,
        )

        anime_relations_data_item.additional_properties = d
        return anime_relations_data_item

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
