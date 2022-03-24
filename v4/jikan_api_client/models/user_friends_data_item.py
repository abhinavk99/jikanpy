from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_meta import UserMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFriendsDataItem")


@attr.s(auto_attribs=True)
class UserFriendsDataItem:
    """
    Attributes:
        user (Union[Unset, UserMeta]):
        last_online (Union[Unset, str]): Last Online Date ISO8601 format
        friends_since (Union[Unset, str]): Friends Since Date ISO8601 format
    """

    user: Union[Unset, UserMeta] = UNSET
    last_online: Union[Unset, str] = UNSET
    friends_since: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        last_online = self.last_online
        friends_since = self.friends_since

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if last_online is not UNSET:
            field_dict["last_online"] = last_online
        if friends_since is not UNSET:
            field_dict["friends_since"] = friends_since

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

        last_online = d.pop("last_online", UNSET)

        friends_since = d.pop("friends_since", UNSET)

        user_friends_data_item = cls(
            user=user,
            last_online=last_online,
            friends_since=friends_since,
        )

        user_friends_data_item.additional_properties = d
        return user_friends_data_item

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
