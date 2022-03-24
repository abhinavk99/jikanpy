from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_meta import AnimeMeta
from ..models.watch_episodes_data_item_episodes_item import WatchEpisodesDataItemEpisodesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="WatchEpisodesDataItem")


@attr.s(auto_attribs=True)
class WatchEpisodesDataItem:
    """
    Attributes:
        entry (Union[Unset, AnimeMeta]):
        episodes (Union[Unset, List[WatchEpisodesDataItemEpisodesItem]]): Recent Episodes (max 2 listed)
        region_locked (Union[Unset, bool]): Region Locked Episode
    """

    entry: Union[Unset, AnimeMeta] = UNSET
    episodes: Union[Unset, List[WatchEpisodesDataItemEpisodesItem]] = UNSET
    region_locked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        episodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.episodes, Unset):
            episodes = []
            for episodes_item_data in self.episodes:
                episodes_item = episodes_item_data.to_dict()

                episodes.append(episodes_item)

        region_locked = self.region_locked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry
        if episodes is not UNSET:
            field_dict["episodes"] = episodes
        if region_locked is not UNSET:
            field_dict["region_locked"] = region_locked

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

        episodes = []
        _episodes = d.pop("episodes", UNSET)
        for episodes_item_data in _episodes or []:
            episodes_item = WatchEpisodesDataItemEpisodesItem.from_dict(episodes_item_data)

            episodes.append(episodes_item)

        region_locked = d.pop("region_locked", UNSET)

        watch_episodes_data_item = cls(
            entry=entry,
            episodes=episodes,
            region_locked=region_locked,
        )

        watch_episodes_data_item.additional_properties = d
        return watch_episodes_data_item

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
