from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_recent_manga_reviews_response_200_data_data_item import GetRecentMangaReviewsResponse200DataDataItem
from ..models.pagination_pagination import PaginationPagination
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRecentMangaReviewsResponse200Data")


@attr.s(auto_attribs=True)
class GetRecentMangaReviewsResponse200Data:
    """
    Attributes:
        pagination (Union[Unset, PaginationPagination]):
        data (Union[Unset, List[GetRecentMangaReviewsResponse200DataDataItem]]):
    """

    pagination: Union[Unset, PaginationPagination] = UNSET
    data: Union[Unset, List[GetRecentMangaReviewsResponse200DataDataItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, PaginationPagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = PaginationPagination.from_dict(_pagination)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetRecentMangaReviewsResponse200DataDataItem.from_dict(data_item_data)

            data.append(data_item)

        get_recent_manga_reviews_response_200_data = cls(
            pagination=pagination,
            data=data,
        )

        get_recent_manga_reviews_response_200_data.additional_properties = d
        return get_recent_manga_reviews_response_200_data

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
