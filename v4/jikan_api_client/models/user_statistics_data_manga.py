from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserStatisticsDataManga")


@attr.s(auto_attribs=True)
class UserStatisticsDataManga:
    """Manga Statistics

    Attributes:
        days_read (Union[Unset, float]): Number of days spent reading Manga
        mean_score (Union[Unset, float]): Mean Score
        reading (Union[Unset, int]): Manga Reading
        completed (Union[Unset, int]): Manga Completed
        on_hold (Union[Unset, int]): Manga On-Hold
        dropped (Union[Unset, int]): Manga Dropped
        plan_to_read (Union[Unset, int]): Manga Planned to Read
        total_entries (Union[Unset, int]): Total Manga entries on User list
        reread (Union[Unset, int]): Manga re-read
        chapters_read (Union[Unset, int]): Number of Manga Chapters Read
        volumes_read (Union[Unset, int]): Number of Manga Volumes Read
    """

    days_read: Union[Unset, float] = UNSET
    mean_score: Union[Unset, float] = UNSET
    reading: Union[Unset, int] = UNSET
    completed: Union[Unset, int] = UNSET
    on_hold: Union[Unset, int] = UNSET
    dropped: Union[Unset, int] = UNSET
    plan_to_read: Union[Unset, int] = UNSET
    total_entries: Union[Unset, int] = UNSET
    reread: Union[Unset, int] = UNSET
    chapters_read: Union[Unset, int] = UNSET
    volumes_read: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days_read = self.days_read
        mean_score = self.mean_score
        reading = self.reading
        completed = self.completed
        on_hold = self.on_hold
        dropped = self.dropped
        plan_to_read = self.plan_to_read
        total_entries = self.total_entries
        reread = self.reread
        chapters_read = self.chapters_read
        volumes_read = self.volumes_read

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days_read is not UNSET:
            field_dict["days_read"] = days_read
        if mean_score is not UNSET:
            field_dict["mean_score"] = mean_score
        if reading is not UNSET:
            field_dict["reading"] = reading
        if completed is not UNSET:
            field_dict["completed"] = completed
        if on_hold is not UNSET:
            field_dict["on_hold"] = on_hold
        if dropped is not UNSET:
            field_dict["dropped"] = dropped
        if plan_to_read is not UNSET:
            field_dict["plan_to_read"] = plan_to_read
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if reread is not UNSET:
            field_dict["reread"] = reread
        if chapters_read is not UNSET:
            field_dict["chapters_read"] = chapters_read
        if volumes_read is not UNSET:
            field_dict["volumes_read"] = volumes_read

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days_read = d.pop("days_read", UNSET)

        mean_score = d.pop("mean_score", UNSET)

        reading = d.pop("reading", UNSET)

        completed = d.pop("completed", UNSET)

        on_hold = d.pop("on_hold", UNSET)

        dropped = d.pop("dropped", UNSET)

        plan_to_read = d.pop("plan_to_read", UNSET)

        total_entries = d.pop("total_entries", UNSET)

        reread = d.pop("reread", UNSET)

        chapters_read = d.pop("chapters_read", UNSET)

        volumes_read = d.pop("volumes_read", UNSET)

        user_statistics_data_manga = cls(
            days_read=days_read,
            mean_score=mean_score,
            reading=reading,
            completed=completed,
            on_hold=on_hold,
            dropped=dropped,
            plan_to_read=plan_to_read,
            total_entries=total_entries,
            reread=reread,
            chapters_read=chapters_read,
            volumes_read=volumes_read,
        )

        user_statistics_data_manga.additional_properties = d
        return user_statistics_data_manga

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
