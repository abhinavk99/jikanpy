from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.anime_images import AnimeImages
from ..models.anime_rating import AnimeRating
from ..models.anime_season import AnimeSeason
from ..models.anime_status import AnimeStatus
from ..models.anime_type import AnimeType
from ..models.broadcast import Broadcast
from ..models.daterange import Daterange
from ..models.mal_url import MalUrl
from ..models.trailer_base import TrailerBase
from ..types import UNSET, Unset

T = TypeVar("T", bound="Anime")


@attr.s(auto_attribs=True)
class Anime:
    """Anime Resource

    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        images (Union[Unset, AnimeImages]):
        trailer (Union[Unset, TrailerBase]): Youtube Details
        title (Union[Unset, str]): Title
        title_english (Union[Unset, None, str]): English Title
        title_japanese (Union[Unset, None, str]): Japanese Title
        title_synonyms (Union[Unset, List[str]]): Other Titles
        type (Union[Unset, None, AnimeType]): Anime Type
        source (Union[Unset, None, str]): Original Material/Source adapted from
        episodes (Union[Unset, None, int]): Episode count
        status (Union[Unset, None, AnimeStatus]): Airing status
        airing (Union[Unset, bool]): Airing boolean
        aired (Union[Unset, Daterange]): Date range
        duration (Union[Unset, None, str]): Parsed raw duration
        rating (Union[Unset, None, AnimeRating]): Anime audience rating
        score (Union[Unset, None, float]): Score
        scored_by (Union[Unset, None, int]): Number of users
        rank (Union[Unset, None, int]): Ranking
        popularity (Union[Unset, None, int]): Popularity
        members (Union[Unset, None, int]): Number of users who have added this entry to their list
        favorites (Union[Unset, None, int]): Number of users who have favorited this entry
        synopsis (Union[Unset, None, str]): Synopsis
        background (Union[Unset, None, str]): Background
        season (Union[Unset, None, AnimeSeason]): Season
        year (Union[Unset, None, int]): Year
        broadcast (Union[Unset, Broadcast]): Broadcast Details
        producers (Union[Unset, List[MalUrl]]):
        licensors (Union[Unset, List[MalUrl]]):
        studios (Union[Unset, List[MalUrl]]):
        genres (Union[Unset, List[MalUrl]]):
        explicit_genres (Union[Unset, List[MalUrl]]):
        themes (Union[Unset, List[MalUrl]]):
        demographics (Union[Unset, List[MalUrl]]):
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, AnimeImages] = UNSET
    trailer: Union[Unset, TrailerBase] = UNSET
    title: Union[Unset, str] = UNSET
    title_english: Union[Unset, None, str] = UNSET
    title_japanese: Union[Unset, None, str] = UNSET
    title_synonyms: Union[Unset, List[str]] = UNSET
    type: Union[Unset, None, AnimeType] = UNSET
    source: Union[Unset, None, str] = UNSET
    episodes: Union[Unset, None, int] = UNSET
    status: Union[Unset, None, AnimeStatus] = UNSET
    airing: Union[Unset, bool] = UNSET
    aired: Union[Unset, Daterange] = UNSET
    duration: Union[Unset, None, str] = UNSET
    rating: Union[Unset, None, AnimeRating] = UNSET
    score: Union[Unset, None, float] = UNSET
    scored_by: Union[Unset, None, int] = UNSET
    rank: Union[Unset, None, int] = UNSET
    popularity: Union[Unset, None, int] = UNSET
    members: Union[Unset, None, int] = UNSET
    favorites: Union[Unset, None, int] = UNSET
    synopsis: Union[Unset, None, str] = UNSET
    background: Union[Unset, None, str] = UNSET
    season: Union[Unset, None, AnimeSeason] = UNSET
    year: Union[Unset, None, int] = UNSET
    broadcast: Union[Unset, Broadcast] = UNSET
    producers: Union[Unset, List[MalUrl]] = UNSET
    licensors: Union[Unset, List[MalUrl]] = UNSET
    studios: Union[Unset, List[MalUrl]] = UNSET
    genres: Union[Unset, List[MalUrl]] = UNSET
    explicit_genres: Union[Unset, List[MalUrl]] = UNSET
    themes: Union[Unset, List[MalUrl]] = UNSET
    demographics: Union[Unset, List[MalUrl]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        trailer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trailer, Unset):
            trailer = self.trailer.to_dict()

        title = self.title
        title_english = self.title_english
        title_japanese = self.title_japanese
        title_synonyms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.title_synonyms, Unset):
            title_synonyms = self.title_synonyms

        type: Union[Unset, None, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        source = self.source
        episodes = self.episodes
        status: Union[Unset, None, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value if self.status else None

        airing = self.airing
        aired: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aired, Unset):
            aired = self.aired.to_dict()

        duration = self.duration
        rating: Union[Unset, None, str] = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating.value if self.rating else None

        score = self.score
        scored_by = self.scored_by
        rank = self.rank
        popularity = self.popularity
        members = self.members
        favorites = self.favorites
        synopsis = self.synopsis
        background = self.background
        season: Union[Unset, None, str] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.value if self.season else None

        year = self.year
        broadcast: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.broadcast, Unset):
            broadcast = self.broadcast.to_dict()

        producers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.producers, Unset):
            producers = []
            for producers_item_data in self.producers:
                producers_item = producers_item_data.to_dict()

                producers.append(producers_item)

        licensors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licensors, Unset):
            licensors = []
            for licensors_item_data in self.licensors:
                licensors_item = licensors_item_data.to_dict()

                licensors.append(licensors_item)

        studios: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.studios, Unset):
            studios = []
            for studios_item_data in self.studios:
                studios_item = studios_item_data.to_dict()

                studios.append(studios_item)

        genres: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.genres, Unset):
            genres = []
            for genres_item_data in self.genres:
                genres_item = genres_item_data.to_dict()

                genres.append(genres_item)

        explicit_genres: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.explicit_genres, Unset):
            explicit_genres = []
            for explicit_genres_item_data in self.explicit_genres:
                explicit_genres_item = explicit_genres_item_data.to_dict()

                explicit_genres.append(explicit_genres_item)

        themes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.themes, Unset):
            themes = []
            for themes_item_data in self.themes:
                themes_item = themes_item_data.to_dict()

                themes.append(themes_item)

        demographics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.demographics, Unset):
            demographics = []
            for demographics_item_data in self.demographics:
                demographics_item = demographics_item_data.to_dict()

                demographics.append(demographics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if images is not UNSET:
            field_dict["images"] = images
        if trailer is not UNSET:
            field_dict["trailer"] = trailer
        if title is not UNSET:
            field_dict["title"] = title
        if title_english is not UNSET:
            field_dict["title_english"] = title_english
        if title_japanese is not UNSET:
            field_dict["title_japanese"] = title_japanese
        if title_synonyms is not UNSET:
            field_dict["title_synonyms"] = title_synonyms
        if type is not UNSET:
            field_dict["type"] = type
        if source is not UNSET:
            field_dict["source"] = source
        if episodes is not UNSET:
            field_dict["episodes"] = episodes
        if status is not UNSET:
            field_dict["status"] = status
        if airing is not UNSET:
            field_dict["airing"] = airing
        if aired is not UNSET:
            field_dict["aired"] = aired
        if duration is not UNSET:
            field_dict["duration"] = duration
        if rating is not UNSET:
            field_dict["rating"] = rating
        if score is not UNSET:
            field_dict["score"] = score
        if scored_by is not UNSET:
            field_dict["scored_by"] = scored_by
        if rank is not UNSET:
            field_dict["rank"] = rank
        if popularity is not UNSET:
            field_dict["popularity"] = popularity
        if members is not UNSET:
            field_dict["members"] = members
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis
        if background is not UNSET:
            field_dict["background"] = background
        if season is not UNSET:
            field_dict["season"] = season
        if year is not UNSET:
            field_dict["year"] = year
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if producers is not UNSET:
            field_dict["producers"] = producers
        if licensors is not UNSET:
            field_dict["licensors"] = licensors
        if studios is not UNSET:
            field_dict["studios"] = studios
        if genres is not UNSET:
            field_dict["genres"] = genres
        if explicit_genres is not UNSET:
            field_dict["explicit_genres"] = explicit_genres
        if themes is not UNSET:
            field_dict["themes"] = themes
        if demographics is not UNSET:
            field_dict["demographics"] = demographics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, AnimeImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = AnimeImages.from_dict(_images)

        _trailer = d.pop("trailer", UNSET)
        trailer: Union[Unset, TrailerBase]
        if isinstance(_trailer, Unset):
            trailer = UNSET
        else:
            trailer = TrailerBase.from_dict(_trailer)

        title = d.pop("title", UNSET)

        title_english = d.pop("title_english", UNSET)

        title_japanese = d.pop("title_japanese", UNSET)

        title_synonyms = cast(List[str], d.pop("title_synonyms", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, None, AnimeType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = AnimeType(_type)

        source = d.pop("source", UNSET)

        episodes = d.pop("episodes", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, None, AnimeStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = AnimeStatus(_status)

        airing = d.pop("airing", UNSET)

        _aired = d.pop("aired", UNSET)
        aired: Union[Unset, Daterange]
        if isinstance(_aired, Unset):
            aired = UNSET
        else:
            aired = Daterange.from_dict(_aired)

        duration = d.pop("duration", UNSET)

        _rating = d.pop("rating", UNSET)
        rating: Union[Unset, None, AnimeRating]
        if _rating is None:
            rating = None
        elif isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = AnimeRating(_rating)

        score = d.pop("score", UNSET)

        scored_by = d.pop("scored_by", UNSET)

        rank = d.pop("rank", UNSET)

        popularity = d.pop("popularity", UNSET)

        members = d.pop("members", UNSET)

        favorites = d.pop("favorites", UNSET)

        synopsis = d.pop("synopsis", UNSET)

        background = d.pop("background", UNSET)

        _season = d.pop("season", UNSET)
        season: Union[Unset, None, AnimeSeason]
        if _season is None:
            season = None
        elif isinstance(_season, Unset):
            season = UNSET
        else:
            season = AnimeSeason(_season)

        year = d.pop("year", UNSET)

        _broadcast = d.pop("broadcast", UNSET)
        broadcast: Union[Unset, Broadcast]
        if isinstance(_broadcast, Unset):
            broadcast = UNSET
        else:
            broadcast = Broadcast.from_dict(_broadcast)

        producers = []
        _producers = d.pop("producers", UNSET)
        for producers_item_data in _producers or []:
            producers_item = MalUrl.from_dict(producers_item_data)

            producers.append(producers_item)

        licensors = []
        _licensors = d.pop("licensors", UNSET)
        for licensors_item_data in _licensors or []:
            licensors_item = MalUrl.from_dict(licensors_item_data)

            licensors.append(licensors_item)

        studios = []
        _studios = d.pop("studios", UNSET)
        for studios_item_data in _studios or []:
            studios_item = MalUrl.from_dict(studios_item_data)

            studios.append(studios_item)

        genres = []
        _genres = d.pop("genres", UNSET)
        for genres_item_data in _genres or []:
            genres_item = MalUrl.from_dict(genres_item_data)

            genres.append(genres_item)

        explicit_genres = []
        _explicit_genres = d.pop("explicit_genres", UNSET)
        for explicit_genres_item_data in _explicit_genres or []:
            explicit_genres_item = MalUrl.from_dict(explicit_genres_item_data)

            explicit_genres.append(explicit_genres_item)

        themes = []
        _themes = d.pop("themes", UNSET)
        for themes_item_data in _themes or []:
            themes_item = MalUrl.from_dict(themes_item_data)

            themes.append(themes_item)

        demographics = []
        _demographics = d.pop("demographics", UNSET)
        for demographics_item_data in _demographics or []:
            demographics_item = MalUrl.from_dict(demographics_item_data)

            demographics.append(demographics_item)

        anime = cls(
            mal_id=mal_id,
            url=url,
            images=images,
            trailer=trailer,
            title=title,
            title_english=title_english,
            title_japanese=title_japanese,
            title_synonyms=title_synonyms,
            type=type,
            source=source,
            episodes=episodes,
            status=status,
            airing=airing,
            aired=aired,
            duration=duration,
            rating=rating,
            score=score,
            scored_by=scored_by,
            rank=rank,
            popularity=popularity,
            members=members,
            favorites=favorites,
            synopsis=synopsis,
            background=background,
            season=season,
            year=year,
            broadcast=broadcast,
            producers=producers,
            licensors=licensors,
            studios=studios,
            genres=genres,
            explicit_genres=explicit_genres,
            themes=themes,
            demographics=demographics,
        )

        anime.additional_properties = d
        return anime

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
