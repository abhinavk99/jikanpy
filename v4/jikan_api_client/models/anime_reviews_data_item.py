from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.anime_review_scores import AnimeReviewScores
from ..models.user_meta import UserMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeReviewsDataItem")


@attr.s(auto_attribs=True)
class AnimeReviewsDataItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        type (Union[Unset, str]): Entry Type
        votes (Union[Unset, int]): Number of user votes on the Review
        date (Union[Unset, str]): Review created date ISO8601
        review (Union[Unset, str]): Review content
        episodes_watched (Union[Unset, int]): Number of episodes watched
        scores (Union[Unset, AnimeReviewScores]): Review Scores breakdown
        user (Union[Unset, UserMeta]):
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    votes: Union[Unset, int] = UNSET
    date: Union[Unset, str] = UNSET
    review: Union[Unset, str] = UNSET
    episodes_watched: Union[Unset, int] = UNSET
    scores: Union[Unset, AnimeReviewScores] = UNSET
    user: Union[Unset, UserMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        type = self.type
        votes = self.votes
        date = self.date
        review = self.review
        episodes_watched = self.episodes_watched
        scores: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scores, Unset):
            scores = self.scores.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if type is not UNSET:
            field_dict["type"] = type
        if votes is not UNSET:
            field_dict["votes"] = votes
        if date is not UNSET:
            field_dict["date"] = date
        if review is not UNSET:
            field_dict["review"] = review
        if episodes_watched is not UNSET:
            field_dict["episodes_watched"] = episodes_watched
        if scores is not UNSET:
            field_dict["scores"] = scores
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        type = d.pop("type", UNSET)

        votes = d.pop("votes", UNSET)

        date = d.pop("date", UNSET)

        review = d.pop("review", UNSET)

        episodes_watched = d.pop("episodes_watched", UNSET)

        _scores = d.pop("scores", UNSET)
        scores: Union[Unset, AnimeReviewScores]
        if isinstance(_scores, Unset):
            scores = UNSET
        else:
            scores = AnimeReviewScores.from_dict(_scores)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserMeta]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserMeta.from_dict(_user)

        anime_reviews_data_item = cls(
            mal_id=mal_id,
            url=url,
            type=type,
            votes=votes,
            date=date,
            review=review,
            episodes_watched=episodes_watched,
            scores=scores,
            user=user,
        )

        anime_reviews_data_item.additional_properties = d
        return anime_reviews_data_item

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
