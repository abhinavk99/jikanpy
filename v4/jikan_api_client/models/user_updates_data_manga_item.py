from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.manga_meta import MangaMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdatesDataMangaItem")


@attr.s(auto_attribs=True)
class UserUpdatesDataMangaItem:
    """
    Attributes:
        entry (Union[Unset, MangaMeta]):
        score (Union[Unset, None, int]):
        status (Union[Unset, str]):
        chapters_read (Union[Unset, None, int]):
        chapters_total (Union[Unset, None, int]):
        volumes_read (Union[Unset, None, int]):
        volumes_total (Union[Unset, None, int]):
        date (Union[Unset, str]): ISO8601 format
    """

    entry: Union[Unset, MangaMeta] = UNSET
    score: Union[Unset, None, int] = UNSET
    status: Union[Unset, str] = UNSET
    chapters_read: Union[Unset, None, int] = UNSET
    chapters_total: Union[Unset, None, int] = UNSET
    volumes_read: Union[Unset, None, int] = UNSET
    volumes_total: Union[Unset, None, int] = UNSET
    date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        score = self.score
        status = self.status
        chapters_read = self.chapters_read
        chapters_total = self.chapters_total
        volumes_read = self.volumes_read
        volumes_total = self.volumes_total
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
        if chapters_read is not UNSET:
            field_dict["chapters_read"] = chapters_read
        if chapters_total is not UNSET:
            field_dict["chapters_total"] = chapters_total
        if volumes_read is not UNSET:
            field_dict["volumes_read"] = volumes_read
        if volumes_total is not UNSET:
            field_dict["volumes_total"] = volumes_total
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, MangaMeta]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = MangaMeta.from_dict(_entry)

        score = d.pop("score", UNSET)

        status = d.pop("status", UNSET)

        chapters_read = d.pop("chapters_read", UNSET)

        chapters_total = d.pop("chapters_total", UNSET)

        volumes_read = d.pop("volumes_read", UNSET)

        volumes_total = d.pop("volumes_total", UNSET)

        date = d.pop("date", UNSET)

        user_updates_data_manga_item = cls(
            entry=entry,
            score=score,
            status=status,
            chapters_read=chapters_read,
            chapters_total=chapters_total,
            volumes_read=volumes_read,
            volumes_total=volumes_total,
            date=date,
        )

        user_updates_data_manga_item.additional_properties = d
        return user_updates_data_manga_item

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
