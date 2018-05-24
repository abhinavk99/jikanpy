# Possible extensions for endpoints
EXTENSIONS = {
    'anime': (
        'characters_staff',
        'episodes',
        'news',
        'pictures',
        'videos',
        'stats',
        'forum',
        'moreinfo'
    ),
    'manga': (
        'characters',
        'news',
        'pictures',
        'stats',
        'forum',
        'moreinfo'
    ),
    'character': (
        'pictures'
    ),
    'person': (
        'pictures'
    )
}

# Possible search parameters for ?key=value
SEARCH_PARAMS = {
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
    'genre' : range(1, 44),
    'score': '',
    'start_date': '',
    'end_date': '',
    'genre_exclude': (0, 1)
}

# Possible seasons
SEASONS = ('winter', 'spring', 'summer', 'fall')

# Possible days
DAYS = (
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
)

# Possible subtypes for top endpoint
SUBTYPES = {
    'anime': (
        'airing',
        'upcoming',
        'tv',
        'movie',
        'ova',
        'special'
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

# Possible parameters for meta
META = {
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
