import string
from typing import Dict, Union, Tuple

# Possible extensions for endpoints
EXTENSIONS: Dict[str, Union[str, Tuple[str, ...]]] = {
    "anime": (
        "characters_staff",
        "episodes",
        "news",
        "pictures",
        "videos",
        "stats",
        "forum",
        "moreinfo",
        "reviews",
        "recommendations",
        "userupdates",
        'forum/episodes'
    ),
    "manga": (
        "characters",
        "news",
        "pictures",
        "stats",
        "forum",
        "moreinfo",
        "reviews",
        "recommendations",
        "userupdates",
    ),
    "character": ("pictures"),
    "person": ("pictures"),
    "club": ("members"),
}

# Possible search parameters for ?key=value
SEARCH_PARAMS: Dict[
    str, Union[Dict[str, Tuple[Union[int, str], ...]], str, Tuple[Union[int, str], ...]]
] = {
    "anime": {
        "type": ("tv", "ova", "movie", "special", "ona", "music"),
        "status": ("airing", "completed", "complete", "to_be_aired", "tba", "upcoming"),
        "rated": ("g", "pg", "pg13", "r17", "r", "rx"),
        "genre": tuple(range(1, 44)),
        "order_by": (
            "title",
            "start_date",
            "end_date",
            "score",
            "type",
            "members",
            "id",
            "episodes",
            "rating",
        ),
    },
    "manga": {
        "type": ("manga", "novel", "oneshot", "doujin", "manhwa", "manhua"),
        "status": (
            "publishing",
            "completed",
            "complete",
            "to_be_published",
            "tbp",
            "upcoming",
        ),
        "genre": tuple(range(1, 46)),
        "order_by": (
            "title",
            "start_date",
            "end_date",
            "score",
            "type",
            "members",
            "id",
            "chapters",
            "volumes",
        ),
    },
    "score": "",
    "start_date": "",
    "end_date": "",
    "genre_exclude": (0, 1),
    "limit": "",
    "sort": ("ascending", "asc", "descending", "desc"),
    # tuple of lowercase letters and '.'
    "letter": tuple(string.ascii_lowercase + "."),
}

# Possible seasons
SEASONS: Tuple[str, ...] = ("winter", "spring", "summer", "fall")

# Possible days
DAYS: Tuple[str, ...] = (
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
    "other",
    "unknown",
)

# Possible subtypes for top endpoint
SUBTYPES: Dict[str, Tuple[str, ...]] = {
    "anime": (
        "airing",
        "upcoming",
        "tv",
        "movie",
        "ova",
        "special",
        "bypopularity",
        "favorite",
    ),
    "manga": (
        "manga",
        "novels",
        "oneshots",
        "doujin",
        "manhwa",
        "manhua",
        "bypopularity",
        "favorite",
    ),
}

# Possible types for genre
GENRE_TYPES: Tuple[str, ...] = ("anime", "manga")

# Possible creator types/endpoints
CREATOR_TYPES: Tuple[str, ...] = ("producer", "magazine")

# Possible requests for user endpoint
USER_REQUESTS: Tuple[str, ...] = (
    "profile",
    "history",
    "friends",
    "animelist",
    "mangalist",
)

# Possible arguments for history request in user endpoint
USER_HISTORY_ARGUMENTS: Tuple[str, ...] = ("anime", "manga")

# Possible arguments for animelist request in user endpoint
USER_ANIMELIST_ARGUMENTS: Tuple[str, ...] = (
    "all",
    "watching",
    "completed",
    "onhold",
    "dropped",
    "plantowatch",
    "ptw",
)

# Possible arguments for mangalist request in user endpoint
USER_MANGALIST_ARGUMENTS: Tuple[str, ...] = (
    "all",
    "reading",
    "completed",
    "onhold",
    "dropped",
    "plantoread",
    "ptr",
)

# Possible parameters for meta
META: Dict[str, Tuple[str, ...]] = {
    "request": ("requests", "status"),
    "type": (
        "anime",
        "manga",
        "character",
        "person",
        "search",
        "top",
        "schedule",
        "season",
    ),
    "period": ("today", "weekly", "monthly"),
}
