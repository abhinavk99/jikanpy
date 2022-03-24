from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.mal_url import MalUrl
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClubRelationsData")


@attr.s(auto_attribs=True)
class ClubRelationsData:
    """
    Attributes:
        anime (Union[Unset, List[MalUrl]]):
        manga (Union[Unset, List[MalUrl]]):
        characters (Union[Unset, List[MalUrl]]):
    """

    anime: Union[Unset, List[MalUrl]] = UNSET
    manga: Union[Unset, List[MalUrl]] = UNSET
    characters: Union[Unset, List[MalUrl]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        anime: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.anime, Unset):
            anime = []
            for anime_item_data in self.anime:
                anime_item = anime_item_data.to_dict()

                anime.append(anime_item)

        manga: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.manga, Unset):
            manga = []
            for manga_item_data in self.manga:
                manga_item = manga_item_data.to_dict()

                manga.append(manga_item)

        characters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.characters, Unset):
            characters = []
            for characters_item_data in self.characters:
                characters_item = characters_item_data.to_dict()

                characters.append(characters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anime is not UNSET:
            field_dict["anime"] = anime
        if manga is not UNSET:
            field_dict["manga"] = manga
        if characters is not UNSET:
            field_dict["characters"] = characters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        anime = []
        _anime = d.pop("anime", UNSET)
        for anime_item_data in _anime or []:
            anime_item = MalUrl.from_dict(anime_item_data)

            anime.append(anime_item)

        manga = []
        _manga = d.pop("manga", UNSET)
        for manga_item_data in _manga or []:
            manga_item = MalUrl.from_dict(manga_item_data)

            manga.append(manga_item)

        characters = []
        _characters = d.pop("characters", UNSET)
        for characters_item_data in _characters or []:
            characters_item = MalUrl.from_dict(characters_item_data)

            characters.append(characters_item)

        club_relations_data = cls(
            anime=anime,
            manga=manga,
            characters=characters,
        )

        club_relations_data.additional_properties = d
        return club_relations_data

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
