from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_images import UserImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfile")


@attr.s(auto_attribs=True)
class UserProfile:
    """
    Attributes:
        mal_id (Union[Unset, None, int]): MyAnimeList ID
        username (Union[Unset, str]): MyAnimeList Username
        url (Union[Unset, str]): MyAnimeList URL
        images (Union[Unset, UserImages]):
        last_online (Union[Unset, None, str]): Last Online Date ISO8601
        gender (Union[Unset, None, str]): User Gender
        birthday (Union[Unset, None, str]): Birthday Date ISO8601
        location (Union[Unset, None, str]): Location
        joined (Union[Unset, None, str]): Joined Date ISO8601
    """

    mal_id: Union[Unset, None, int] = UNSET
    username: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, UserImages] = UNSET
    last_online: Union[Unset, None, str] = UNSET
    gender: Union[Unset, None, str] = UNSET
    birthday: Union[Unset, None, str] = UNSET
    location: Union[Unset, None, str] = UNSET
    joined: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        username = self.username
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        last_online = self.last_online
        gender = self.gender
        birthday = self.birthday
        location = self.location
        joined = self.joined

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if username is not UNSET:
            field_dict["username"] = username
        if url is not UNSET:
            field_dict["url"] = url
        if images is not UNSET:
            field_dict["images"] = images
        if last_online is not UNSET:
            field_dict["last_online"] = last_online
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if location is not UNSET:
            field_dict["location"] = location
        if joined is not UNSET:
            field_dict["joined"] = joined

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        username = d.pop("username", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, UserImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = UserImages.from_dict(_images)

        last_online = d.pop("last_online", UNSET)

        gender = d.pop("gender", UNSET)

        birthday = d.pop("birthday", UNSET)

        location = d.pop("location", UNSET)

        joined = d.pop("joined", UNSET)

        user_profile = cls(
            mal_id=mal_id,
            username=username,
            url=url,
            images=images,
            last_online=last_online,
            gender=gender,
            birthday=birthday,
            location=location,
            joined=joined,
        )

        user_profile.additional_properties = d
        return user_profile

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
