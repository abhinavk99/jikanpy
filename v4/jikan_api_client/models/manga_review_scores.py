from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="MangaReviewScores")


@attr.s(auto_attribs=True)
class MangaReviewScores:
    """Review Scores breakdown

    Attributes:
        overall (Union[Unset, int]): Overall Score
        story (Union[Unset, int]): Story Score
        art (Union[Unset, int]): Art Score
        character (Union[Unset, int]): Character Score
        enjoyment (Union[Unset, int]): Enjoyment Score
    """

    overall: Union[Unset, int] = UNSET
    story: Union[Unset, int] = UNSET
    art: Union[Unset, int] = UNSET
    character: Union[Unset, int] = UNSET
    enjoyment: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        overall = self.overall
        story = self.story
        art = self.art
        character = self.character
        enjoyment = self.enjoyment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overall is not UNSET:
            field_dict["overall"] = overall
        if story is not UNSET:
            field_dict["story"] = story
        if art is not UNSET:
            field_dict["art"] = art
        if character is not UNSET:
            field_dict["character"] = character
        if enjoyment is not UNSET:
            field_dict["enjoyment"] = enjoyment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        overall = d.pop("overall", UNSET)

        story = d.pop("story", UNSET)

        art = d.pop("art", UNSET)

        character = d.pop("character", UNSET)

        enjoyment = d.pop("enjoyment", UNSET)

        manga_review_scores = cls(
            overall=overall,
            story=story,
            art=art,
            character=character,
            enjoyment=enjoyment,
        )

        manga_review_scores.additional_properties = d
        return manga_review_scores

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
