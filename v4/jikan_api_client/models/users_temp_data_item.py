from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.users_temp_data_item_anime_stats import UsersTempDataItemAnimeStats
from ..models.users_temp_data_item_favorites import UsersTempDataItemFavorites
from ..models.users_temp_data_item_images import UsersTempDataItemImages
from ..models.users_temp_data_item_manga_stats import UsersTempDataItemMangaStats
from ..types import UNSET, Unset

T = TypeVar("T", bound="UsersTempDataItem")


@attr.s(auto_attribs=True)
class UsersTempDataItem:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        username (Union[Unset, str]): MyAnimeList Username
        url (Union[Unset, str]): MyAnimeList URL
        images (Union[Unset, UsersTempDataItemImages]): Images
        last_online (Union[Unset, str]): Last Online Date ISO8601
        gender (Union[Unset, str]): User Gender
        birthday (Union[Unset, str]): Birthday Date ISO8601
        location (Union[Unset, str]): Location
        joined (Union[Unset, str]): Joined Date ISO8601
        anime_stats (Union[Unset, UsersTempDataItemAnimeStats]): Anime Stats
        manga_stats (Union[Unset, UsersTempDataItemMangaStats]): Manga Stats
        favorites (Union[Unset, UsersTempDataItemFavorites]): Favorite entries
        about (Union[Unset, str]): User About. NOTE: About information is customizable by users through BBCode on
            MyAnimeList. This means users can add multimedia content, different text sizes, etc. Due to this freeform, Jikan
            returns parsed HTML. Validate on your end!
    """

    mal_id: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    images: Union[Unset, UsersTempDataItemImages] = UNSET
    last_online: Union[Unset, str] = UNSET
    gender: Union[Unset, str] = UNSET
    birthday: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    joined: Union[Unset, str] = UNSET
    anime_stats: Union[Unset, UsersTempDataItemAnimeStats] = UNSET
    manga_stats: Union[Unset, UsersTempDataItemMangaStats] = UNSET
    favorites: Union[Unset, UsersTempDataItemFavorites] = UNSET
    about: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        username = self.username
        url = self.url
        images: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        last_online = self.last_online
        gender = self.gender
        birthday = self.birthday
        location = self.location
        joined = self.joined
        anime_stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.anime_stats, Unset):
            anime_stats = self.anime_stats.to_dict()

        manga_stats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.manga_stats, Unset):
            manga_stats = self.manga_stats.to_dict()

        favorites: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites.to_dict()

        about = self.about

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if username is not UNSET:
            field_dict["username"] = username
        if url is not UNSET:
            field_dict["url"] = url
        if images is not UNSET:
            field_dict["images"] = images
        if last_online is not UNSET:
            field_dict["last_online"] = last_online
        if gender is not UNSET:
            field_dict["gender"] = gender
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if location is not UNSET:
            field_dict["location"] = location
        if joined is not UNSET:
            field_dict["joined"] = joined
        if anime_stats is not UNSET:
            field_dict["anime_stats"] = anime_stats
        if manga_stats is not UNSET:
            field_dict["manga_stats"] = manga_stats
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if about is not UNSET:
            field_dict["about"] = about

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        username = d.pop("username", UNSET)

        url = d.pop("url", UNSET)

        _images = d.pop("images", UNSET)
        images: Union[Unset, UsersTempDataItemImages]
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = UsersTempDataItemImages.from_dict(_images)

        last_online = d.pop("last_online", UNSET)

        gender = d.pop("gender", UNSET)

        birthday = d.pop("birthday", UNSET)

        location = d.pop("location", UNSET)

        joined = d.pop("joined", UNSET)

        _anime_stats = d.pop("anime_stats", UNSET)
        anime_stats: Union[Unset, UsersTempDataItemAnimeStats]
        if isinstance(_anime_stats, Unset):
            anime_stats = UNSET
        else:
            anime_stats = UsersTempDataItemAnimeStats.from_dict(_anime_stats)

        _manga_stats = d.pop("manga_stats", UNSET)
        manga_stats: Union[Unset, UsersTempDataItemMangaStats]
        if isinstance(_manga_stats, Unset):
            manga_stats = UNSET
        else:
            manga_stats = UsersTempDataItemMangaStats.from_dict(_manga_stats)

        _favorites = d.pop("favorites", UNSET)
        favorites: Union[Unset, UsersTempDataItemFavorites]
        if isinstance(_favorites, Unset):
            favorites = UNSET
        else:
            favorites = UsersTempDataItemFavorites.from_dict(_favorites)

        about = d.pop("about", UNSET)

        users_temp_data_item = cls(
            mal_id=mal_id,
            username=username,
            url=url,
            images=images,
            last_online=last_online,
            gender=gender,
            birthday=birthday,
            location=location,
            joined=joined,
            anime_stats=anime_stats,
            manga_stats=manga_stats,
            favorites=favorites,
            about=about,
        )

        users_temp_data_item.additional_properties = d
        return users_temp_data_item

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
