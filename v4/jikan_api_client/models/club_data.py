from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.club_data_access import ClubDataAccess
from ..models.club_data_category import ClubDataCategory
from ..models.common_images import CommonImages
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClubData")


@attr.s(auto_attribs=True)
class ClubData:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        name (Union[Unset, str]): Club name
        url (Union[Unset, str]): Club URL
        images (Union[Unset, CommonImages]):
        members (Union[Unset, int]): Number of club members
        category (Union[Unset, ClubDataCategory]): Club Category
        created (Union[Unset, str]): Date Created ISO8601
        access (Union[Unset, ClubDataAccess]): Club access
    """

    mal_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, CommonImages] = UNSET
    members: Union[Unset, int] = UNSET
    category: Union[Unset, ClubDataCategory] = UNSET
    created: Union[Unset, str] = UNSET
    access: Union[Unset, ClubDataAccess] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        name = self.name
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        members = self.members
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        created = self.created
        access: Union[Unset, str] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if images is not UNSET:
            field_dict["images"] = images
        if members is not UNSET:
            field_dict["members"] = members
        if category is not UNSET:
            field_dict["category"] = category
        if created is not UNSET:
            field_dict["created"] = created
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, CommonImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = CommonImages.from_dict(_images)

        members = d.pop("members", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, ClubDataCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = ClubDataCategory(_category)

        created = d.pop("created", UNSET)

        _access = d.pop("access", UNSET)
        access: Union[Unset, ClubDataAccess]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = ClubDataAccess(_access)

        club_data = cls(
            mal_id=mal_id,
            name=name,
            url=url,
            images=images,
            members=members,
            category=category,
            created=created,
            access=access,
        )

        club_data.additional_properties = d
        return club_data

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
