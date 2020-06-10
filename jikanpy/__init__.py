"""JikanPy
====================================
__init__.py contains the Jikan class, a synchronous Jikan wrapper.
"""

from jikanpy.jikan import Jikan
from jikanpy.aiojikan import AioJikan
from jikanpy.exceptions import JikanException, APIException, DeprecatedEndpoint

__all__ = ["Jikan", "AioJikan", "JikanException", "APIException", "DeprecatedEndpoint"]
