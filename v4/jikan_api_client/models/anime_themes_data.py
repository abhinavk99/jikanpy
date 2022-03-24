from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeThemesData")


@attr.s(auto_attribs=True)
class AnimeThemesData:
    """
    Attributes:
        openings (Union[Unset, List[str]]):
        endings (Union[Unset, List[str]]):
    """

    openings: Union[Unset, List[str]] = UNSET
    endings: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        openings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.openings, Unset):
            openings = self.openings

        endings: Union[Unset, List[str]] = UNSET
        if not isinstance(self.endings, Unset):
            endings = self.endings

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if openings is not UNSET:
            field_dict["openings"] = openings
        if endings is not UNSET:
            field_dict["endings"] = endings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        openings = cast(List[str], d.pop("openings", UNSET))

        endings = cast(List[str], d.pop("endings", UNSET))

        anime_themes_data = cls(
            openings=openings,
            endings=endings,
        )

        anime_themes_data.additional_properties = d
        return anime_themes_data

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
