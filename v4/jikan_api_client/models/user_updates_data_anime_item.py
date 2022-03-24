from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_meta import AnimeMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdatesDataAnimeItem")


@attr.s(auto_attribs=True)
class UserUpdatesDataAnimeItem:
    """
    Attributes:
        entry (Union[Unset, AnimeMeta]):
        score (Union[Unset, None, int]):
        status (Union[Unset, str]):
        episodes_seen (Union[Unset, None, int]):
        episodes_total (Union[Unset, None, int]):
        date (Union[Unset, str]): ISO8601 format
    """

    entry: Union[Unset, AnimeMeta] = UNSET
    score: Union[Unset, None, int] = UNSET
    status: Union[Unset, str] = UNSET
    episodes_seen: Union[Unset, None, int] = UNSET
    episodes_total: Union[Unset, None, int] = UNSET
    date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        score = self.score
        status = self.status
        episodes_seen = self.episodes_seen
        episodes_total = self.episodes_total
        date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry
        if score is not UNSET:
            field_dict["score"] = score
        if status is not UNSET:
            field_dict["status"] = status
        if episodes_seen is not UNSET:
            field_dict["episodes_seen"] = episodes_seen
        if episodes_total is not UNSET:
            field_dict["episodes_total"] = episodes_total
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, AnimeMeta]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = AnimeMeta.from_dict(_entry)

        score = d.pop("score", UNSET)

        status = d.pop("status", UNSET)

        episodes_seen = d.pop("episodes_seen", UNSET)

        episodes_total = d.pop("episodes_total", UNSET)

        date = d.pop("date", UNSET)

        user_updates_data_anime_item = cls(
            entry=entry,
            score=score,
            status=status,
            episodes_seen=episodes_seen,
            episodes_total=episodes_total,
            date=date,
        )

        user_updates_data_anime_item.additional_properties = d
        return user_updates_data_anime_item

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
