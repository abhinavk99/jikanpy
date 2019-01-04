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
    'genre': range(1, 44),
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
GENRE_TYPES = ('anime', 'manga')

# Possible creator types/endpoints
CREATOR_TYPES = ('producer', 'magazine')

# Possible requests for user endpoint
USER_REQUESTS = ('profile', 'history', 'friends', 'animelist', 'mangalist')

# Possible arguments for history request in user endpoint
USER_HISTORY_ARGUMENTS = ('anime', 'manga')

# Possible arguments for animelist request in user endpoint
USER_ANIMELIST_ARGUMENTS = (
    'all', 'watching', 'completed', 'onhold', 'dropped', 'plantowatch', 'ptw')

# Possible arguments for mangalist request in user endpoint
USER_MANGALIST_ARGUMENTS = (
    'all', 'reading', 'completed', 'onhold', 'dropped', 'plantoread', 'ptr')

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
