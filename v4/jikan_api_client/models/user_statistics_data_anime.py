from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserStatisticsDataAnime")


@attr.s(auto_attribs=True)
class UserStatisticsDataAnime:
    """Anime Statistics

    Attributes:
        days_watched (Union[Unset, float]): Number of days spent watching Anime
        mean_score (Union[Unset, float]): Mean Score
        watching (Union[Unset, int]): Anime Watching
        completed (Union[Unset, int]): Anime Completed
        on_hold (Union[Unset, int]): Anime On-Hold
        dropped (Union[Unset, int]): Anime Dropped
        plan_to_watch (Union[Unset, int]): Anime Planned to Watch
        total_entries (Union[Unset, int]): Total Anime entries on User list
        rewatched (Union[Unset, int]): Anime re-watched
        episodes_watched (Union[Unset, int]): Number of Anime Episodes Watched
    """

    days_watched: Union[Unset, float] = UNSET
    mean_score: Union[Unset, float] = UNSET
    watching: Union[Unset, int] = UNSET
    completed: Union[Unset, int] = UNSET
    on_hold: Union[Unset, int] = UNSET
    dropped: Union[Unset, int] = UNSET
    plan_to_watch: Union[Unset, int] = UNSET
    total_entries: Union[Unset, int] = UNSET
    rewatched: Union[Unset, int] = UNSET
    episodes_watched: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days_watched = self.days_watched
        mean_score = self.mean_score
        watching = self.watching
        completed = self.completed
        on_hold = self.on_hold
        dropped = self.dropped
        plan_to_watch = self.plan_to_watch
        total_entries = self.total_entries
        rewatched = self.rewatched
        episodes_watched = self.episodes_watched

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days_watched is not UNSET:
            field_dict["days_watched"] = days_watched
        if mean_score is not UNSET:
            field_dict["mean_score"] = mean_score
        if watching is not UNSET:
            field_dict["watching"] = watching
        if completed is not UNSET:
            field_dict["completed"] = completed
        if on_hold is not UNSET:
            field_dict["on_hold"] = on_hold
        if dropped is not UNSET:
            field_dict["dropped"] = dropped
        if plan_to_watch is not UNSET:
            field_dict["plan_to_watch"] = plan_to_watch
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if rewatched is not UNSET:
            field_dict["rewatched"] = rewatched
        if episodes_watched is not UNSET:
            field_dict["episodes_watched"] = episodes_watched

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        days_watched = d.pop("days_watched", UNSET)

        mean_score = d.pop("mean_score", UNSET)

        watching = d.pop("watching", UNSET)

        completed = d.pop("completed", UNSET)

        on_hold = d.pop("on_hold", UNSET)

        dropped = d.pop("dropped", UNSET)

        plan_to_watch = d.pop("plan_to_watch", UNSET)

        total_entries = d.pop("total_entries", UNSET)

        rewatched = d.pop("rewatched", UNSET)

        episodes_watched = d.pop("episodes_watched", UNSET)

        user_statistics_data_anime = cls(
            days_watched=days_watched,
            mean_score=mean_score,
            watching=watching,
            completed=completed,
            on_hold=on_hold,
            dropped=dropped,
            plan_to_watch=plan_to_watch,
            total_entries=total_entries,
            rewatched=rewatched,
            episodes_watched=episodes_watched,
        )

        user_statistics_data_anime.additional_properties = d
        return user_statistics_data_anime

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
