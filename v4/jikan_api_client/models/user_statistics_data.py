from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_statistics_data_anime import UserStatisticsDataAnime
from ..models.user_statistics_data_manga import UserStatisticsDataManga
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserStatisticsData")


@attr.s(auto_attribs=True)
class UserStatisticsData:
    """
    Attributes:
        anime (Union[Unset, UserStatisticsDataAnime]): Anime Statistics
        manga (Union[Unset, UserStatisticsDataManga]): Manga Statistics
    """

    anime: Union[Unset, UserStatisticsDataAnime] = UNSET
    manga: Union[Unset, UserStatisticsDataManga] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        anime: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.anime, Unset):
            anime = self.anime.to_dict()

        manga: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manga, Unset):
            manga = self.manga.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anime is not UNSET:
            field_dict["anime"] = anime
        if manga is not UNSET:
            field_dict["manga"] = manga

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _anime = d.pop("anime", UNSET)
        anime: Union[Unset, UserStatisticsDataAnime]
        if isinstance(_anime, Unset):
            anime = UNSET
        else:
            anime = UserStatisticsDataAnime.from_dict(_anime)

        _manga = d.pop("manga", UNSET)
        manga: Union[Unset, UserStatisticsDataManga]
        if isinstance(_manga, Unset):
            manga = UNSET
        else:
            manga = UserStatisticsDataManga.from_dict(_manga)

        user_statistics_data = cls(
            anime=anime,
            manga=manga,
        )

        user_statistics_data.additional_properties = d
        return user_statistics_data

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
