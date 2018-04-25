Jikanpy
=======

Jikanpy is a Python wrapper for [Jikan](https://github.com/jikan-me/jikan),
providing bindings for all API functionality. Because it is intended to be
pretty much identical, please consult [Jikan's
documentation](https://jikan.docs.apiary.io/#) for thornier details on how it is meant to
be used. Perhaps most importantly, Jikanpy does not make any attempts to rate
limit itself, so use it as responsibly as you would use the API primitively.

```python
from jikanpy import Jikan
jikan = Jikan()

# json of all anime info specified by Jikan docs
mushishi = jikan.anime(457)

# same as above, but with extra info
# (see Jikan docs for information about which endpoints have which extensions)
mushishi_with_eps = jikan.anime(457, extension='episodes')
mushishi_with_eps_2 = jikan.anime(457, extension='episodes', page=2)
mushishi_with_characters_and_staff = jikan.anime(457, extension='characters_staff')

# you can also query characters
ginko = jikan.character(425)

# and manga
mushishi_manga = jikan.manga(418)
```