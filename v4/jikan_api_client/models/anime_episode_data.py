from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnimeEpisodeData")


@attr.s(auto_attribs=True)
class AnimeEpisodeData:
    """
    Attributes:
        mal_id (Union[Unset, int]): MyAnimeList ID
        url (Union[Unset, str]): MyAnimeList URL
        title (Union[Unset, str]): Title
        title_japanese (Union[Unset, None, str]): Title Japanese
        title_romanji (Union[Unset, None, str]): title_romanji
        duration (Union[Unset, None, int]): Episode duration in seconds
        aired (Union[Unset, None, str]): Aired Date ISO8601
        filler (Union[Unset, bool]): Filler episode
        recap (Union[Unset, bool]): Recap episode
        synopsis (Union[Unset, None, str]): Episode Synopsis
    """

    mal_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    title_japanese: Union[Unset, None, str] = UNSET
    title_romanji: Union[Unset, None, str] = UNSET
    duration: Union[Unset, None, int] = UNSET
    aired: Union[Unset, None, str] = UNSET
    filler: Union[Unset, bool] = UNSET
    recap: Union[Unset, bool] = UNSET
    synopsis: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mal_id = self.mal_id
        url = self.url
        title = self.title
        title_japanese = self.title_japanese
        title_romanji = self.title_romanji
        duration = self.duration
        aired = self.aired
        filler = self.filler
        recap = self.recap
        synopsis = self.synopsis

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mal_id is not UNSET:
            field_dict["mal_id"] = mal_id
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if title_japanese is not UNSET:
            field_dict["title_japanese"] = title_japanese
        if title_romanji is not UNSET:
            field_dict["title_romanji"] = title_romanji
        if duration is not UNSET:
            field_dict["duration"] = duration
        if aired is not UNSET:
            field_dict["aired"] = aired
        if filler is not UNSET:
            field_dict["filler"] = filler
        if recap is not UNSET:
            field_dict["recap"] = recap
        if synopsis is not UNSET:
            field_dict["synopsis"] = synopsis

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mal_id = d.pop("mal_id", UNSET)

        url = d.pop("url", UNSET)

        title = d.pop("title", UNSET)

        title_japanese = d.pop("title_japanese", UNSET)

        title_romanji = d.pop("title_romanji", UNSET)

        duration = d.pop("duration", UNSET)

        aired = d.pop("aired", UNSET)

        filler = d.pop("filler", UNSET)

        recap = d.pop("recap", UNSET)

        synopsis = d.pop("synopsis", UNSET)

        anime_episode_data = cls(
            mal_id=mal_id,
            url=url,
            title=title,
            title_japanese=title_japanese,
            title_romanji=title_romanji,
            duration=duration,
            aired=aired,
            filler=filler,
            recap=recap,
            synopsis=synopsis,
        )

        anime_episode_data.additional_properties = d
        return anime_episode_data

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
