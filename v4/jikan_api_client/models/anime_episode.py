from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_episode_data import AnimeEpisodeData
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeEpisode")


@attr.s(auto_attribs=True)
class AnimeEpisode:
    """Anime Episode Resource

    Attributes:
        data (Union[Unset, AnimeEpisodeData]):
    """

    data: Union[Unset, AnimeEpisodeData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, AnimeEpisodeData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AnimeEpisodeData.from_dict(_data)

        anime_episode = cls(
            data=data,
        )

        anime_episode.additional_properties = d
        return anime_episode

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
