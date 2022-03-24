from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_meta import AnimeMeta
from ..models.manga_meta import MangaMeta
from ..models.user_by_id import UserById
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendationsDataItem")


@attr.s(auto_attribs=True)
class RecommendationsDataItem:
    """
    Attributes:
        mal_id (Union[Unset, str]): MAL IDs of recommendations is both of the MAL ID's with a `-` delimiter
        entry (Union[Unset, List[Union[AnimeMeta, MangaMeta]]]): Array of 2 entries that are being recommended to each
            other
        content (Union[Unset, str]): Recommendation context provided by the user
        user (Union[Unset, UserById]): User Meta By ID
    """

    mal_id: Union[Unset, str] = UNSET
    entry: Union[Unset, List[Union[AnimeMeta, MangaMeta]]] = UNSET
    content: Union[Unset, str] = UNSET
    user: Union[Unset, UserById] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        entry: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = []
            for entry_item_data in self.entry:

                if isinstance(entry_item_data, AnimeMeta):
                    entry_item = entry_item_data.to_dict()

                else:
                    entry_item = entry_item_data.to_dict()

                entry.append(entry_item)

        content = self.content
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if entry is not UNSET:
            field_dict["entry"] = entry
        if content is not UNSET:
            field_dict["content"] = content
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

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

        content = d.pop("content", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserById]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserById.from_dict(_user)

        recommendations_data_item = cls(
            mal_id=mal_id,
            entry=entry,
            content=content,
            user=user,
        )

        recommendations_data_item.additional_properties = d
        return recommendations_data_item

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
