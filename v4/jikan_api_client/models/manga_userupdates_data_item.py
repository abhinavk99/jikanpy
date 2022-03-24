from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_meta import UserMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="MangaUserupdatesDataItem")


@attr.s(auto_attribs=True)
class MangaUserupdatesDataItem:
    """
    Attributes:
        user (Union[Unset, UserMeta]):
        score (Union[Unset, int]): User Score
        status (Union[Unset, str]): User list status
        volumes_read (Union[Unset, int]): Number of volumes read
        volumes_total (Union[Unset, int]): Total number of volumes
        chapters_read (Union[Unset, int]): Number of chapters read
        chapters_total (Union[Unset, int]): Total number of chapters
        date (Union[Unset, str]): Last updated date ISO8601
    """

    user: Union[Unset, UserMeta] = UNSET
    score: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    volumes_read: Union[Unset, int] = UNSET
    volumes_total: Union[Unset, int] = UNSET
    chapters_read: Union[Unset, int] = UNSET
    chapters_total: Union[Unset, int] = UNSET
    date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        score = self.score
        status = self.status
        volumes_read = self.volumes_read
        volumes_total = self.volumes_total
        chapters_read = self.chapters_read
        chapters_total = self.chapters_total
        date = self.date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if score is not UNSET:
            field_dict["score"] = score
        if status is not UNSET:
            field_dict["status"] = status
        if volumes_read is not UNSET:
            field_dict["volumes_read"] = volumes_read
        if volumes_total is not UNSET:
            field_dict["volumes_total"] = volumes_total
        if chapters_read is not UNSET:
            field_dict["chapters_read"] = chapters_read
        if chapters_total is not UNSET:
            field_dict["chapters_total"] = chapters_total
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, UserMeta]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserMeta.from_dict(_user)

        score = d.pop("score", UNSET)

        status = d.pop("status", UNSET)

        volumes_read = d.pop("volumes_read", UNSET)

        volumes_total = d.pop("volumes_total", UNSET)

        chapters_read = d.pop("chapters_read", UNSET)

        chapters_total = d.pop("chapters_total", UNSET)

        date = d.pop("date", UNSET)

        manga_userupdates_data_item = cls(
            user=user,
            score=score,
            status=status,
            volumes_read=volumes_read,
            volumes_total=volumes_total,
            chapters_read=chapters_read,
            chapters_total=chapters_total,
            date=date,
        )

        manga_userupdates_data_item.additional_properties = d
        return manga_userupdates_data_item

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
