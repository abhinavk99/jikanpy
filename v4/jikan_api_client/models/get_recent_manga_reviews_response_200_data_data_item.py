from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.manga_meta import MangaMeta
from ..models.manga_review_scores import MangaReviewScores
from ..models.user_meta import UserMeta
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRecentMangaReviewsResponse200DataDataItem")


@attr.s(auto_attribs=True)
class GetRecentMangaReviewsResponse200DataDataItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        type (Union[Unset, str]): Entry Type
        votes (Union[Unset, int]): Number of user votes on the Review
        date (Union[Unset, str]): Review created date ISO8601
        chapters_read (Union[Unset, int]): Number of chapters read by the reviewer
        review (Union[Unset, str]): Review content
        scores (Union[Unset, MangaReviewScores]): Review Scores breakdown
        user (Union[Unset, UserMeta]):
        manga (Union[Unset, MangaMeta]):
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    votes: Union[Unset, int] = UNSET
    date: Union[Unset, str] = UNSET
    chapters_read: Union[Unset, int] = UNSET
    review: Union[Unset, str] = UNSET
    scores: Union[Unset, MangaReviewScores] = UNSET
    user: Union[Unset, UserMeta] = UNSET
    manga: Union[Unset, MangaMeta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        type = self.type
        votes = self.votes
        date = self.date
        chapters_read = self.chapters_read
        review = self.review
        scores: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.scores, Unset):
            scores = self.scores.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        manga: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manga, Unset):
            manga = self.manga.to_dict()

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
        if chapters_read is not UNSET:
            field_dict["chapters_read"] = chapters_read
        if review is not UNSET:
            field_dict["review"] = review
        if scores is not UNSET:
            field_dict["scores"] = scores
        if user is not UNSET:
            field_dict["user"] = user
        if manga is not UNSET:
            field_dict["manga"] = manga

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        type = d.pop("type", UNSET)

        votes = d.pop("votes", UNSET)

        date = d.pop("date", UNSET)

        chapters_read = d.pop("chapters_read", UNSET)

        review = d.pop("review", UNSET)

        _scores = d.pop("scores", UNSET)
        scores: Union[Unset, MangaReviewScores]
        if isinstance(_scores, Unset):
            scores = UNSET
        else:
            scores = MangaReviewScores.from_dict(_scores)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserMeta]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserMeta.from_dict(_user)

        _manga = d.pop("manga", UNSET)
        manga: Union[Unset, MangaMeta]
        if isinstance(_manga, Unset):
            manga = UNSET
        else:
            manga = MangaMeta.from_dict(_manga)

        get_recent_manga_reviews_response_200_data_data_item = cls(
            mal_id=mal_id,
            url=url,
            type=type,
            votes=votes,
            date=date,
            chapters_read=chapters_read,
            review=review,
            scores=scores,
            user=user,
            manga=manga,
        )

        get_recent_manga_reviews_response_200_data_data_item.additional_properties = d
        return get_recent_manga_reviews_response_200_data_data_item

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
