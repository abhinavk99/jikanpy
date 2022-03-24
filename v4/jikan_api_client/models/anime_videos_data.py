from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_videos_data_episodes_item import AnimeVideosDataEpisodesItem
from ..models.anime_videos_data_promos_item import AnimeVideosDataPromosItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeVideosData")


@attr.s(auto_attribs=True)
class AnimeVideosData:
    """
    Attributes:
        promos (Union[Unset, List[AnimeVideosDataPromosItem]]):
        episodes (Union[Unset, List[AnimeVideosDataEpisodesItem]]):
    """

    promos: Union[Unset, List[AnimeVideosDataPromosItem]] = UNSET
    episodes: Union[Unset, List[AnimeVideosDataEpisodesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        promos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.promos, Unset):
            promos = []
            for promos_item_data in self.promos:
                promos_item = promos_item_data.to_dict()

                promos.append(promos_item)

        episodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.episodes, Unset):
            episodes = []
            for episodes_item_data in self.episodes:
                episodes_item = episodes_item_data.to_dict()

                episodes.append(episodes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if promos is not UNSET:
            field_dict["promos"] = promos
        if episodes is not UNSET:
            field_dict["episodes"] = episodes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        promos = []
        _promos = d.pop("promos", UNSET)
        for promos_item_data in _promos or []:
            promos_item = AnimeVideosDataPromosItem.from_dict(promos_item_data)

            promos.append(promos_item)

        episodes = []
        _episodes = d.pop("episodes", UNSET)
        for episodes_item_data in _episodes or []:
            episodes_item = AnimeVideosDataEpisodesItem.from_dict(episodes_item_data)

            episodes.append(episodes_item)

        anime_videos_data = cls(
            promos=promos,
            episodes=episodes,
        )

        anime_videos_data.additional_properties = d
        return anime_videos_data

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
