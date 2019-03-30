from __future__ import annotations

from typing import Dict, Union, Tuple, Iterable

# Possible extensions for endpoints
EXTENSIONS: Dict[str, Union[str, Tuple[str, ...]]] = {
    'anime': (
        'characters_staff',
        'episodes',
        'news',
        'pictures',
        'videos',
        'stats',
        'forum',
        'moreinfo',
        'reviews',
        'recommendations',
        'userupdates'
    ),
    'manga': (
        'characters',
        'news',
        'pictures',
        'stats',
        'forum',
        'moreinfo',
        'reviews',
        'recommendations',
        'userupdates'
    ),
    'character': (
        'pictures'
    ),
    'person': (
        'pictures'
    ),
    'club': (
        'members'
    )
}

# Possible search parameters for ?key=value
SEARCH_PARAMS: Dict[str, Union[str, Tuple[Union[int, str], ...], Iterable[int]]] = {
    'type': (
        'tv',
        'ova',
        'movie',
        'special',
        'ona',
        'music',
        'manga',
        'novel',
        'oneshot',
        'doujin',
        'manhwa',
        'manhua'
    ),
    'status': (
        'airing',
        'completed',
        'complete',
        'tba',
        'upcoming'
    ),
    'rated': (
        'g',
        'pg',
        'pg13',
        'r17',
        'r',
        'rx'
    ),
    'genre': range(1, 44),
    'score': '',
    'start_date': '',
    'end_date': '',
    'genre_exclude': (0, 1)
}

# Possible seasons
SEASONS: Tuple[str, ...] = ('winter', 'spring', 'summer', 'fall')

# Possible days
DAYS: Tuple[str, ...] = (
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
    'other',
    'unknown'
)

# Possible subtypes for top endpoint
SUBTYPES: Dict[str, Tuple[str, ...]] = {
    'anime': (
        'airing',
        'upcoming',
        'tv',
        'movie',
        'ova',
        'special',
        'bypopularity',
        'favorite'
    ),
    'manga': (
        'manga',
        'novels',
        'oneshots',
        'doujin',
        'manhwa',
        'manhua',
        'bypopularity',
        'favorite'
    )
}

# Possible types for genre
GENRE_TYPES: Tuple[str, ...] = ('anime', 'manga')

# Possible creator types/endpoints
CREATOR_TYPES: Tuple[str, ...] = ('producer', 'magazine')

# Possible requests for user endpoint
USER_REQUESTS: Tuple[str, ...] = (
    'profile', 'history', 'friends', 'animelist', 'mangalist')

# Possible arguments for history request in user endpoint
USER_HISTORY_ARGUMENTS: Tuple[str, ...] = ('anime', 'manga')

# Possible arguments for animelist request in user endpoint
USER_ANIMELIST_ARGUMENTS: Tuple[str, ...] = (
    'all', 'watching', 'completed', 'onhold', 'dropped', 'plantowatch', 'ptw')

# Possible arguments for mangalist request in user endpoint
USER_MANGALIST_ARGUMENTS: Tuple[str, ...] = (
    'all', 'reading', 'completed', 'onhold', 'dropped', 'plantoread', 'ptr')

# Possible parameters for meta
META: Dict[str, Tuple[str, ...]] = {
    'request': (
        'requests',
        'status'
    ),
    'type': (
        'anime',
        'manga',
        'character',
        'person',
        'search',
        'top',
        'schedule',
        'season'
    ),
    'period': (
        'today',
        'weekly',
        'monthly'
    )
}
