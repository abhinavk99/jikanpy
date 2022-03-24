from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_images import CommonImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsDataItem")


@attr.s(auto_attribs=True)
class NewsDataItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        title (Union[Unset, str]): Title
        date (Union[Unset, str]): Post Date ISO8601
        author_username (Union[Unset, str]): Author MyAnimeList Username
        author_url (Union[Unset, str]): Author Profile URL
        forum_url (Union[Unset, str]): Forum topic URL
        images (Union[Unset, CommonImages]):
        comments (Union[Unset, int]): Comment count
        excerpt (Union[Unset, str]): Excerpt
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    author_username: Union[Unset, str] = UNSET
    author_url: Union[Unset, str] = UNSET
    forum_url: Union[Unset, str] = UNSET
    images: Union[Unset, CommonImages] = UNSET
    comments: Union[Unset, int] = UNSET
    excerpt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        title = self.title
        date = self.date
        author_username = self.author_username
        author_url = self.author_url
        forum_url = self.forum_url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        comments = self.comments
        excerpt = self.excerpt

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
        if forum_url is not UNSET:
            field_dict["forum_url"] = forum_url
        if images is not UNSET:
            field_dict["images"] = images
        if comments is not UNSET:
            field_dict["comments"] = comments
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt

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

        forum_url = d.pop("forum_url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, CommonImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = CommonImages.from_dict(_images)

        comments = d.pop("comments", UNSET)

        excerpt = d.pop("excerpt", UNSET)

        news_data_item = cls(
            mal_id=mal_id,
            url=url,
            title=title,
            date=date,
            author_username=author_username,
            author_url=author_url,
            forum_url=forum_url,
            images=images,
            comments=comments,
            excerpt=excerpt,
        )

        news_data_item.additional_properties = d
        return news_data_item

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
