# Helper file to keep track of things changed in the jikan rest api

List of things to keep track of for updating jikanpy from jikanv3 to jikanv4. 
Updating this as I go and plan to use it to help me put PR together.

## Things in v3 removed in v4
- The entire meta endpoint has been removed

## Things in v3 modified in v4
- Cache TTL is now 24 hours for all requests
- Response headers are updated:
	- `Expires` is still the cache expiry date
	- `X-Request-Cached` has been removed
	- `X-Request-Cache-Ttl` has been removed
	- New: `Last-Modified` details the cache set date
	- New: `X-Request-Fingerprint` details the unique request fingerprint

- Responses are now wrapped in a single key dict: {'data' : usual_response}
- Search has more argument options
- `/character` endpoint is now `/characters`
- `/anime/{id}/episodes` now returns a `List[dict]` object for episodes
	- `page` parameter should probably be re-worked. Url it constructs now gets that number episode
- `person` endpoint is renamed to `people`
- search is now spread to a particular endpoint instead of just `/search`
- `/season` is now `/seasons` with different parameters
- `/schedule` is now `/schedules` with query parameters instead of url params
- `page` is now a query param instead of a url append
- `/top`'s `subtype` url params are now replaced with query params
- `/genre` is renamed to `/genres` and only returns a list of genres with MAL urls. Paging no longer supported

## Things new in v4

- Rate limit is now:
	- 3 requests per second (originally 2)
	- 60 requests per minute (originally 30)

	Not really important for the upgrade, but I might have an idea
	for a method of optional forced rate limting

- Cache Validation - the new `ETag` header in all request responses gives the MD5 hash of the response. Can be used
	to verify content by using `If-None-Match` in request header
		- waiting to find out if this is implemented yet

- Certain endpoints now support pagination (ex: [getAnimeEpisodes](https://docs.api.jikan.moe/#tag/anime/operation/getAnimeEpisodes))

- Some pre-existing endpoints have new child endpoints
	- ex: Some old endpoints (need to make a list of which) now support `/full` (e.g. `/manga/1/full`) to get all information about the series



# Todo
- [X] Update response header information
- [ ] Implement cache validation
	- May not be possible, ETag is currently broken. Opened an issue [here](https://github.com/jikan-me/jikan-rest/issues/322)
- [ ] Update parsing for new response structure
	- [ ] Update response dict keys in test fixtures
	- [ ] Support pagination for relevant endpionts
- [ ] Add support for new endpoints
- [ ] Deprecate unsupported endpoints
	- [X] Remove meta endpoint calls and tests
	- [X] Deprecated `get_url_with_page` method and replaced calls with query behavior
	- [ ] Updated search url construction
- [ ] Change behavior for modified endpoints
	- [X] Update `person` method to `people` to reflect endpoint change
	- [X] change season utils to reflect new endpoint behavior
		- [X] removed `get_season_archive_url` and `get_season_later_url` in utils
		- [X] added `get_season_upcoming_url` and `get_season_now_url` in utils
		- [X] repalced `get_season_later` with `get_season_upcoming` in jikan.py
	- [X] change `get_schedule_url` in utils to reflect changes to `/schedule` behvaior
	- [X] modify `get_top_url` in utils to reflect changes `/top` endpoint 
	- [X] modify `top` in jikan to reflect changes to `/top` endpoint
	