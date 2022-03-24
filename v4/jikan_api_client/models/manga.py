from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.daterange import Daterange
from ..models.mal_url import MalUrl
from ..models.manga_images import MangaImages
from ..models.manga_status import MangaStatus
from ..models.manga_type import MangaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Manga")


@attr.s(auto_attribs=True)
class Manga:
    """Manga Resource

    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        images (Union[Unset, MangaImages]):
        title (Union[Unset, str]): Title
        title_english (Union[Unset, None, str]): English Title
        title_japanese (Union[Unset, None, str]): Japanese Title
        title_synonyms (Union[Unset, List[str]]): Other Titles
        type (Union[Unset, None, MangaType]): Manga Type
        chapters (Union[Unset, None, int]): Chapter count
        volumes (Union[Unset, None, int]): Volume count
        status (Union[Unset, MangaStatus]): Publishing status
        publishing (Union[Unset, bool]): Publishing boolean
        published (Union[Unset, Daterange]): Date range
        score (Union[Unset, float]): Score
        scored_by (Union[Unset, int]): Number of users
        rank (Union[Unset, None, int]): Ranking
        popularity (Union[Unset, None, int]): Popularity
        members (Union[Unset, None, int]): Number of users who have added this entry to their list
        favorites (Union[Unset, None, int]): Number of users who have favorited this entry
        synopsis (Union[Unset, None, str]): Synopsis
        background (Union[Unset, None, str]): Background
        authors (Union[Unset, List[MalUrl]]):
        serializations (Union[Unset, List[MalUrl]]):
        genres (Union[Unset, List[MalUrl]]):
        explicit_genres (Union[Unset, List[MalUrl]]):
        themes (Union[Unset, List[MalUrl]]):
        demographics (Union[Unset, List[MalUrl]]):
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, MangaImages] = UNSET
    title: Union[Unset, str] = UNSET
    title_english: Union[Unset, None, str] = UNSET
    title_japanese: Union[Unset, None, str] = UNSET
    title_synonyms: Union[Unset, List[str]] = UNSET
    type: Union[Unset, None, MangaType] = UNSET
    chapters: Union[Unset, None, int] = UNSET
    volumes: Union[Unset, None, int] = UNSET
    status: Union[Unset, MangaStatus] = UNSET
    publishing: Union[Unset, bool] = UNSET
    published: Union[Unset, Daterange] = UNSET
    score: Union[Unset, float] = UNSET
    scored_by: Union[Unset, int] = UNSET
    rank: Union[Unset, None, int] = UNSET
    popularity: Union[Unset, None, int] = UNSET
    members: Union[Unset, None, int] = UNSET
    favorites: Union[Unset, None, int] = UNSET
    synopsis: Union[Unset, None, str] = UNSET
    background: Union[Unset, None, str] = UNSET
    authors: Union[Unset, List[MalUrl]] = UNSET
    serializations: Union[Unset, List[MalUrl]] = UNSET
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

        title = self.title
        title_english = self.title_english
        title_japanese = self.title_japanese
        title_synonyms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.title_synonyms, Unset):
            title_synonyms = self.title_synonyms

        type: Union[Unset, None, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        chapters = self.chapters
        volumes = self.volumes
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        publishing = self.publishing
        published: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.published, Unset):
            published = self.published.to_dict()

        score = self.score
        scored_by = self.scored_by
        rank = self.rank
        popularity = self.popularity
        members = self.members
        favorites = self.favorites
        synopsis = self.synopsis
        background = self.background
        authors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()

                authors.append(authors_item)

        serializations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.serializations, Unset):
            serializations = []
            for serializations_item_data in self.serializations:
                serializations_item = serializations_item_data.to_dict()

                serializations.append(serializations_item)

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
        if chapters is not UNSET:
            field_dict["chapters"] = chapters
        if volumes is not UNSET:
            field_dict["volumes"] = volumes
        if status is not UNSET:
            field_dict["status"] = status
        if publishing is not UNSET:
            field_dict["publishing"] = publishing
        if published is not UNSET:
            field_dict["published"] = published
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
        if authors is not UNSET:
            field_dict["authors"] = authors
        if serializations is not UNSET:
            field_dict["serializations"] = serializations
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
        images: Union[Unset, MangaImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = MangaImages.from_dict(_images)

        title = d.pop("title", UNSET)

        title_english = d.pop("title_english", UNSET)

        title_japanese = d.pop("title_japanese", UNSET)

        title_synonyms = cast(List[str], d.pop("title_synonyms", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, None, MangaType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = MangaType(_type)

        chapters = d.pop("chapters", UNSET)

        volumes = d.pop("volumes", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MangaStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MangaStatus(_status)

        publishing = d.pop("publishing", UNSET)

        _published = d.pop("published", UNSET)
        published: Union[Unset, Daterange]
        if isinstance(_published, Unset):
            published = UNSET
        else:
            published = Daterange.from_dict(_published)

        score = d.pop("score", UNSET)

        scored_by = d.pop("scored_by", UNSET)

        rank = d.pop("rank", UNSET)

        popularity = d.pop("popularity", UNSET)

        members = d.pop("members", UNSET)

        favorites = d.pop("favorites", UNSET)

        synopsis = d.pop("synopsis", UNSET)

        background = d.pop("background", UNSET)

        authors = []
        _authors = d.pop("authors", UNSET)
        for authors_item_data in _authors or []:
            authors_item = MalUrl.from_dict(authors_item_data)

            authors.append(authors_item)

        serializations = []
        _serializations = d.pop("serializations", UNSET)
        for serializations_item_data in _serializations or []:
            serializations_item = MalUrl.from_dict(serializations_item_data)

            serializations.append(serializations_item)

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

        manga = cls(
            mal_id=mal_id,
            url=url,
            images=images,
            title=title,
            title_english=title_english,
            title_japanese=title_japanese,
            title_synonyms=title_synonyms,
            type=type,
            chapters=chapters,
            volumes=volumes,
            status=status,
            publishing=publishing,
            published=published,
            score=score,
            scored_by=scored_by,
            rank=rank,
            popularity=popularity,
            members=members,
            favorites=favorites,
            synopsis=synopsis,
            background=background,
            authors=authors,
            serializations=serializations,
            genres=genres,
            explicit_genres=explicit_genres,
            themes=themes,
            demographics=demographics,
        )

        manga.additional_properties = d
        return manga

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
