from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_images import UserImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserMeta")


@attr.s(auto_attribs=True)
class UserMeta:
    """
    Attributes:
        username (Union[Unset, str]): MyAnimeList Username
        url (Union[Unset, str]): MyAnimeList Profile URL
        images (Union[Unset, UserImages]):
    """

    username: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, UserImages] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if url is not UNSET:
            field_dict["url"] = url
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, UserImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = UserImages.from_dict(_images)

        user_meta = cls(
            username=username,
            url=url,
            images=images,
        )

        user_meta.additional_properties = d
        return user_meta

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
