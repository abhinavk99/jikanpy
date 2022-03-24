from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationPagination")


@attr.s(auto_attribs=True)
class PaginationPagination:
    """
    Attributes:
        last_visible_page (Union[Unset, int]):
        has_next_page (Union[Unset, bool]):
    """

    last_visible_page: Union[Unset, int] = UNSET
    has_next_page: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_visible_page = self.last_visible_page
        has_next_page = self.has_next_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_visible_page is not UNSET:
            field_dict["last_visible_page"] = last_visible_page
        if has_next_page is not UNSET:
            field_dict["has_next_page"] = has_next_page

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last_visible_page = d.pop("last_visible_page", UNSET)

        has_next_page = d.pop("has_next_page", UNSET)

        pagination_pagination = cls(
            last_visible_page=last_visible_page,
            has_next_page=has_next_page,
        )

        pagination_pagination.additional_properties = d
        return pagination_pagination

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
