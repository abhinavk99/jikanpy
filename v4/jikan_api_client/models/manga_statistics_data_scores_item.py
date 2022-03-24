from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MangaStatisticsDataScoresItem")


@attr.s(auto_attribs=True)
class MangaStatisticsDataScoresItem:
    """
    Attributes:
        score (Union[Unset, int]): Scoring value
        votes (Union[Unset, int]): Number of votes for this score
        percentage (Union[Unset, float]): Percentage of votes for this score
    """

    score: Union[Unset, int] = UNSET
    votes: Union[Unset, int] = UNSET
    percentage: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        score = self.score
        votes = self.votes
        percentage = self.percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if votes is not UNSET:
            field_dict["votes"] = votes
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        score = d.pop("score", UNSET)

        votes = d.pop("votes", UNSET)

        percentage = d.pop("percentage", UNSET)

        manga_statistics_data_scores_item = cls(
            score=score,
            votes=votes,
            percentage=percentage,
        )

        manga_statistics_data_scores_item.additional_properties = d
        return manga_statistics_data_scores_item

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
