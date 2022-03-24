from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.people_images import PeopleImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="Person")


@attr.s(auto_attribs=True)
class Person:
    """Person Resource

    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        website_url (Union[Unset, None, str]): Person's website URL
        images (Union[Unset, PeopleImages]):
        name (Union[Unset, str]): Name
        given_name (Union[Unset, None, str]): Given Name
        family_name (Union[Unset, None, str]): Family Name
        alternate_names (Union[Unset, List[str]]): Other Names
        birthday (Union[Unset, None, str]): Birthday Date ISO8601
        favorites (Union[Unset, int]): Number of users who have favorited this entry
        about (Union[Unset, None, str]): Biography
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    website_url: Union[Unset, None, str] = UNSET
    images: Union[Unset, PeopleImages] = UNSET
    name: Union[Unset, str] = UNSET
    given_name: Union[Unset, None, str] = UNSET
    family_name: Union[Unset, None, str] = UNSET
    alternate_names: Union[Unset, List[str]] = UNSET
    birthday: Union[Unset, None, str] = UNSET
    favorites: Union[Unset, int] = UNSET
    about: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        website_url = self.website_url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        name = self.name
        given_name = self.given_name
        family_name = self.family_name
        alternate_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alternate_names, Unset):
            alternate_names = self.alternate_names

        birthday = self.birthday
        favorites = self.favorites
        about = self.about

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if images is not UNSET:
            field_dict["images"] = images
        if name is not UNSET:
            field_dict["name"] = name
        if given_name is not UNSET:
            field_dict["given_name"] = given_name
        if family_name is not UNSET:
            field_dict["family_name"] = family_name
        if alternate_names is not UNSET:
            field_dict["alternate_names"] = alternate_names
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if about is not UNSET:
            field_dict["about"] = about

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        website_url = d.pop("website_url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, PeopleImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = PeopleImages.from_dict(_images)

        name = d.pop("name", UNSET)

        given_name = d.pop("given_name", UNSET)

        family_name = d.pop("family_name", UNSET)

        alternate_names = cast(List[str], d.pop("alternate_names", UNSET))

        birthday = d.pop("birthday", UNSET)

        favorites = d.pop("favorites", UNSET)

        about = d.pop("about", UNSET)

        person = cls(
            mal_id=mal_id,
            url=url,
            website_url=website_url,
            images=images,
            name=name,
            given_name=given_name,
            family_name=family_name,
            alternate_names=alternate_names,
            birthday=birthday,
            favorites=favorites,
            about=about,
        )

        person.additional_properties = d
        return person

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
