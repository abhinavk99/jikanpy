from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.manga_statistics_data_scores_item import MangaStatisticsDataScoresItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="MangaStatisticsData")


@attr.s(auto_attribs=True)
class MangaStatisticsData:
    """
    Attributes:
        reading (Union[Unset, int]): Number of users reading the resource
        completed (Union[Unset, int]): Number of users who have completed the resource
        on_hold (Union[Unset, int]): Number of users who have put the resource on hold
        dropped (Union[Unset, int]): Number of users who have dropped the resource
        plan_to_read (Union[Unset, int]): Number of users who have planned to read the resource
        total (Union[Unset, int]): Total number of users who have the resource added to their lists
        scores (Union[Unset, List[MangaStatisticsDataScoresItem]]):
    """

    reading: Union[Unset, int] = UNSET
    completed: Union[Unset, int] = UNSET
    on_hold: Union[Unset, int] = UNSET
    dropped: Union[Unset, int] = UNSET
    plan_to_read: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    scores: Union[Unset, List[MangaStatisticsDataScoresItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reading = self.reading
        completed = self.completed
        on_hold = self.on_hold
        dropped = self.dropped
        plan_to_read = self.plan_to_read
        total = self.total
        scores: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scores, Unset):
            scores = []
            for scores_item_data in self.scores:
                scores_item = scores_item_data.to_dict()

                scores.append(scores_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if total is not UNSET:
            field_dict["total"] = total
        if scores is not UNSET:
            field_dict["scores"] = scores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reading = d.pop("reading", UNSET)

        completed = d.pop("completed", UNSET)

        on_hold = d.pop("on_hold", UNSET)

        dropped = d.pop("dropped", UNSET)

        plan_to_read = d.pop("plan_to_read", UNSET)

        total = d.pop("total", UNSET)

        scores = []
        _scores = d.pop("scores", UNSET)
        for scores_item_data in _scores or []:
            scores_item = MangaStatisticsDataScoresItem.from_dict(scores_item_data)

            scores.append(scores_item)

        manga_statistics_data = cls(
            reading=reading,
            completed=completed,
            on_hold=on_hold,
            dropped=dropped,
            plan_to_read=plan_to_read,
            total=total,
            scores=scores,
        )

        manga_statistics_data.additional_properties = d
        return manga_statistics_data

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
