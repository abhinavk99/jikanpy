# Changelog for Jikanpy

## [4.2.1] - 2020-06-11

### Fixed

- Bug where simplejson wasn't being installed as a dependency

## [4.2.0] - 2020-06-10

### Added

- Revamped how APIException works so it displays more information whether or not the HTTP response is JSON

### Changed

- Some refactoring to fix typing and linting errors from mypy, flake8, and pylint
- Updated some unit tests and commented out ones that don't work because of Jikan 503 errors

### Fixed

- Bug where jikanpy would crash when the JSON response can't be decoded with the simplejson JSON parser
- Bug where jikanpy would crash when the JSON response is a list instead of a dict

## [4.1.0] - 2020-05-23

### Fixed

- Bug where selected_base wasn't being used
- Bug where trailing slash or whitespace in selected_base argument wouldn't work

## [4.0.0] - 2020-05-20

### Added

- Documentation at https://jikanpy.readthedocs.io
- AioJikan can be constructed using 'async with' technique
- Optional page argument to club method

### Changed

- AbstractJikan rewritten as utility methods
- Docstrings rewritten to follow Google style guide
- Updated all requirements to current versions

### Removed

- Removed checking arguments and throwing ClientException from invalid arguments
- Removed ClientException because it isn't being raised anymore
- Removed use_ssl argument so only HTTPS Jikan URL is available
- Removed loop argument for AioJikan
- Unnecessary type hints for variable instantiations

### Fixed

- Lazy construct aiohttp session in AioJikan to stop DeprecationWarning
- Issue where page couldn't be added to user method URL when argument not passed in

## [3.4.2] - 2019-11-29

### Added

- Added extension forum/episodes for anime endpoint

## [3.4.1] - 2019-10-02

### Added

- Added MIT license to Jikanpy

## [3.4.0] - 2019-09-15

### Added

- Added Jikanpy to PyPI

## [3.3.0] - 2019-09-07

### Added

- Ability to pass in own Requests session to Jikan in constructor

### Fixed

- Made type hints for session and loop in constructors more accurate

## [3.2.0] - 2019-09-07

### Added

- Jikan URL and response headers to Jikanpy response

### Fixed

- Error handling when type or period argument is None for meta method
- Bug in which letter argument for search method didn't allow the character .

## [3.1.2] - 2019-07-23

### Added

- This changelog

## [3.1.1] - 2019-07-22

### Fixed

- Bug when passing in genre_exclude as boolean

## [3.1.0] - 2019-05-18

### Added

- selected_base constructor arg to aio_jikan

### Changed

- search and user methods to adhere with REST 3.3

## [3.0.2] - 2019-05-07

### Fixed

- Bug where search method didn't check genre parameter correctly

## [3.0.1] - 2019-04-28

### Fixed

- Bug where check_response didn't handle when there was no error in the response json

## [3.0.0] - 2019-03-30

### Added

- Type hints (only works in Python 3.6+)
- Options `other` and `unknown` for the parameter `day` in schedule method
- Errors thrown when `status` request is called with arguments in meta method
- `page` parameter to manga endpoint

### Removed

- No more support for Python versions before 3.6

### Fixed

- Bug where parameters weren't being added to search url correctly
- Argument checks for user method
- meta not implemented test

## [2.4.1] - 2019-03-12

### Added

- Tests to reach 100% coverage

### Changed

- Abstract methods raise `NotImplementedError`

## [2.4.0] - 2019-03-05

### Added

- Option to provide base url to Jikanpy to use for endpoint

### Changed

- README examples for user method

## [2.3.2] - 2019-01-19

### Added

- Codecov integration
- Error if top method if subtype is provided without page
- async/await examples in examples.py

## [2.3.1] - 2019-01-05

### Added

- Tests and examples for person method

## [2.3.0] - 2019-01-04

### Added

- club and season later methods (for REST v3.2)
- reviews, recommendations, and user updates extensions (for REST v3.2)

### Fixed

- Bug where page wasn't added to url correctly for extension `episodes`

## [2.2.0] - 2018-12-05

### Added

- Travis integration
- Support for multiple query parameters in search method

### Removed

- No more support for Python versions before 3.5

## [2.1.3] - 2018-11-28

### Fixed

- Subtypes checking for top endpoint

## [2.1.2] - 2018-11-20

### Fixed

- Bug when adding query parameter to url before converting it to a string in search method

## [2.1.1] - 2018-11-18

### Fixed

- Checking key and value in search method

## [2.1.0] - 2018-10-18

### Added

- animelist and mangalist support in user endpoint (REST v3.1)
- search archive method (REST v3.1)

## [2.0.0] - 2018-09-05

### Added

- genre, producer, magazine, and user methods (REST v3)

### Changed

- Base endpoint url to `api.jikan.moe/v3`

## [1.0.1] - 2018-09-03

### Fixed

- Bug where page was added to url before converting it to a string

## [1.0.0] - 2018-06-17

### Added

- semver for versioning
- setup.py

## 2018-06-07

### Added

- AioJikan async wrapper for Jikan

## 2018-05-25

### Added

- season, schedule, top, and meta methods (REST v2.2)

### Changed

- Generalized error checking

## 2018-05-18

### Added

- page support to anime, manga, character, and person methods (REST v2.2)
- query parameter to search method (REST v2.2)

## 2018-04-12

### Added

- search method (REST v2.1)
- examples.py for example usage

### Changed

- Base endpoint url to `api.jikan.moe`
- Extensions for anime, manga, character, and person methods (REST v2.1)
- Limit warning in docstring to the new limit, 5000
- Link to Jikan docs in README

### Deprecated

- user list method

## 2017-10-20

### Changed

- DeprecationWarning to DeprecatedEndpoint

### Fixed

- ID typos in README usage

## 2017-10-19

### Added

- character, person, and user list methods
- Tests for anime and manga methods
- DeprecationWarning exception
- Usage info in README

## 2017-10-18

### Added

- Initial version with anime and manga methods and exceptions
