from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrailerBase")


@attr.s(auto_attribs=True)
class TrailerBase:
    """Youtube Details

    Attributes:
        youtube_id (Union[Unset, None, str]): YouTube ID
        url (Union[Unset, None, str]): YouTube URL
        embed_url (Union[Unset, None, str]): Parsed Embed URL
    """

    youtube_id: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    embed_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        youtube_id = self.youtube_id
        url = self.url
        embed_url = self.embed_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if youtube_id is not UNSET:
            field_dict["youtube_id"] = youtube_id
        if url is not UNSET:
            field_dict["url"] = url
        if embed_url is not UNSET:
            field_dict["embed_url"] = embed_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        youtube_id = d.pop("youtube_id", UNSET)

        url = d.pop("url", UNSET)

        embed_url = d.pop("embed_url", UNSET)

        trailer_base = cls(
            youtube_id=youtube_id,
            url=url,
            embed_url=embed_url,
        )

        trailer_base.additional_properties = d
        return trailer_base

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
