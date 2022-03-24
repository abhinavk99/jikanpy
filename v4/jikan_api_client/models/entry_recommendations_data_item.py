from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_meta import AnimeMeta
from ..models.manga_meta import MangaMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntryRecommendationsDataItem")


@attr.s(auto_attribs=True)
class EntryRecommendationsDataItem:
    """
    Attributes:
        entry (Union[Unset, List[Union[AnimeMeta, MangaMeta]]]): Array of 2 entries that are being recommended to each
            other
        url (Union[Unset, str]): Recommendation MyAnimeList URL
        votes (Union[Unset, int]): Number of users who have recommended this entry
    """

    entry: Union[Unset, List[Union[AnimeMeta, MangaMeta]]] = UNSET
    url: Union[Unset, str] = UNSET
    votes: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = []
            for entry_item_data in self.entry:

                if isinstance(entry_item_data, AnimeMeta):
                    entry_item = entry_item_data.to_dict()

                else:
                    entry_item = entry_item_data.to_dict()

                entry.append(entry_item)

        url = self.url
        votes = self.votes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry
        if url is not UNSET:
            field_dict["url"] = url
        if votes is not UNSET:
            field_dict["votes"] = votes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry = []
        _entry = d.pop("entry", UNSET)
        for entry_item_data in _entry or []:

            def _parse_entry_item(data: object) -> Union[AnimeMeta, MangaMeta]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entry_item_type_0 = AnimeMeta.from_dict(data)

                    return entry_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                entry_item_type_1 = MangaMeta.from_dict(data)

                return entry_item_type_1

            entry_item = _parse_entry_item(entry_item_data)

            entry.append(entry_item)

        url = d.pop("url", UNSET)

        votes = d.pop("votes", UNSET)

        entry_recommendations_data_item = cls(
            entry=entry,
            url=url,
            votes=votes,
        )

        entry_recommendations_data_item.additional_properties = d
        return entry_recommendations_data_item

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
