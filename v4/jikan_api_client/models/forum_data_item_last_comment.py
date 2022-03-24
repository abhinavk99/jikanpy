from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForumDataItemLastComment")


@attr.s(auto_attribs=True)
class ForumDataItemLastComment:
    """Last comment details

    Attributes:
        url (Union[Unset, str]): Last comment URL
        author_username (Union[Unset, str]): Author MyAnimeList Username
        author_url (Union[Unset, str]): Author Profile URL
        date (Union[Unset, None, str]): Last comment date posted ISO8601
    """

    url: Union[Unset, str] = UNSET
    author_username: Union[Unset, str] = UNSET
    author_url: Union[Unset, str] = UNSET
    date: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        author_username = self.author_username
        author_url = self.author_url
        date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if author_username is not UNSET:
            field_dict["author_username"] = author_username
        if author_url is not UNSET:
            field_dict["author_url"] = author_url
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        author_username = d.pop("author_username", UNSET)

        author_url = d.pop("author_url", UNSET)

        date = d.pop("date", UNSET)

        forum_data_item_last_comment = cls(
            url=url,
            author_username=author_username,
            author_url=author_url,
            date=date,
        )

        forum_data_item_last_comment.additional_properties = d
        return forum_data_item_last_comment

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
