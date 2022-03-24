from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeReviewScores")


@attr.s(auto_attribs=True)
class AnimeReviewScores:
    """Review Scores breakdown

    Attributes:
        overall (Union[Unset, int]): Overall Score
        story (Union[Unset, int]): Story Score
        animation (Union[Unset, int]): Animation Score
        sound (Union[Unset, int]): Sound Score
        character (Union[Unset, int]): Character Score
        enjoyment (Union[Unset, int]): Enjoyment Score
    """

    overall: Union[Unset, int] = UNSET
    story: Union[Unset, int] = UNSET
    animation: Union[Unset, int] = UNSET
    sound: Union[Unset, int] = UNSET
    character: Union[Unset, int] = UNSET
    enjoyment: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        overall = self.overall
        story = self.story
        animation = self.animation
        sound = self.sound
        character = self.character
        enjoyment = self.enjoyment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overall is not UNSET:
            field_dict["overall"] = overall
        if story is not UNSET:
            field_dict["story"] = story
        if animation is not UNSET:
            field_dict["animation"] = animation
        if sound is not UNSET:
            field_dict["sound"] = sound
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

        animation = d.pop("animation", UNSET)

        sound = d.pop("sound", UNSET)

        character = d.pop("character", UNSET)

        enjoyment = d.pop("enjoyment", UNSET)

        anime_review_scores = cls(
            overall=overall,
            story=story,
            animation=animation,
            sound=sound,
            character=character,
            enjoyment=enjoyment,
        )

        anime_review_scores.additional_properties = d
        return anime_review_scores

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
