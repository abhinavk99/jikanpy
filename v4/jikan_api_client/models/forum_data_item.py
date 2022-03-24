from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.forum_data_item_last_comment import ForumDataItemLastComment
from ..types import UNSET, Unset

T = TypeVar("T", bound="ForumDataItem")


@attr.s(auto_attribs=True)
class ForumDataItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        title (Union[Unset, str]): Title
        date (Union[Unset, str]): Post Date ISO8601
        author_username (Union[Unset, str]): Author MyAnimeList Username
        author_url (Union[Unset, str]): Author Profile URL
        comments (Union[Unset, int]): Comment count
        last_comment (Union[Unset, ForumDataItemLastComment]): Last comment details
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    author_username: Union[Unset, str] = UNSET
    author_url: Union[Unset, str] = UNSET
    comments: Union[Unset, int] = UNSET
    last_comment: Union[Unset, ForumDataItemLastComment] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        title = self.title
        date = self.date
        author_username = self.author_username
        author_url = self.author_url
        comments = self.comments
        last_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_comment, Unset):
            last_comment = self.last_comment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if date is not UNSET:
            field_dict["date"] = date
        if author_username is not UNSET:
            field_dict["author_username"] = author_username
        if author_url is not UNSET:
            field_dict["author_url"] = author_url
        if comments is not UNSET:
            field_dict["comments"] = comments
        if last_comment is not UNSET:
            field_dict["last_comment"] = last_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        date = d.pop("date", UNSET)

        author_username = d.pop("author_username", UNSET)

        author_url = d.pop("author_url", UNSET)

        comments = d.pop("comments", UNSET)

        _last_comment = d.pop("last_comment", UNSET)
        last_comment: Union[Unset, ForumDataItemLastComment]
        if isinstance(_last_comment, Unset):
            last_comment = UNSET
        else:
            last_comment = ForumDataItemLastComment.from_dict(_last_comment)

        forum_data_item = cls(
            mal_id=mal_id,
            url=url,
            title=title,
            date=date,
            author_username=author_username,
            author_url=author_url,
            comments=comments,
            last_comment=last_comment,
        )

        forum_data_item.additional_properties = d
        return forum_data_item

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
