"""Jikan/AioJikan Exceptions
====================================
exceptions.py contains exceptions used in Jikan and AioJikan.
"""
from typing import Optional, Mapping, Any, Union


class JikanException(Exception):
    """Base exception class for JikanPy."""


class APIException(JikanException):
    """Exception due to an error response from Jikan API.

    Attributes:
        status_code: HTTP response status code.
        error_json: JSON error response from Jikan. Defaults to None.
        relevant_params: Relevant parameters passed into the method resulting in the
            exception.
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        status_code: int,
        error_json: Optional[Mapping[str, Any]] = None,
        **relevant_params: Union[int, Optional[str]],
    ):
        self.status_code = status_code
        self.error_json = error_json
        self.relevant_params = relevant_params
        super().__init__(self.status_code)

    def __str__(self) -> str:
        output = f"HTTP {self.status_code}"
        if self.error_json:
            error_str = ", ".join(f"{k}={v}" for k, v in self.error_json.items())
            output += f" - {error_str}"
        if self.relevant_params:
            param_str = ", ".join(f"{k}={v}" for k, v in self.relevant_params.items())
            output += f" for {param_str}"
        return output

    def __repr__(self) -> str:
        return (
            f"APIException(status_code={self.status_code}, "
            f"error_json={self.error_json}, relevant_params={self.relevant_params})"
        )


class DeprecatedEndpoint(JikanException):
    """Exception raised when attempting to use deprecated API endpoints."""
