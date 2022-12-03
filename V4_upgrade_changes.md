# Helper file to keep track of things changed in the jikan rest api

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



## Things new in v4

- Rate limit is now:
	- 3 requests per second (originally 2)
	- 60 requests per minute (originally 30)

	Not really important for the upgrade, but I might have an idea
	for a method of optional forced rate limting

- Cache Validation - the new `ETag` header in all request responses gives the MD5 hash of the response. Can be used
	to verify content by using `If-None-Match` in request header
		- waiting to find out if this is implemented yet



# Todo
- [X] Remove meta endpoint calls and tests
- [X] Update response header information
- [ ] Implement cache validation
	- May not be possible, ETag doesn't appear to be implemented yet
- [ ] Update return structure parsing
