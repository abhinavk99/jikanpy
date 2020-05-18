class JikanException(Exception):
    """Base exception class for Jikan.py"""


class APIException(JikanException):
    """Exception due to an error response from Jikan API"""


class DeprecatedEndpoint(JikanException):
    """Exception raised when attempting to use deprecated API endpoints"""
