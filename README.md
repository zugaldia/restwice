# Restwice

A Python REST client, with Memcache support, that defaults to URL Fetch on App Engine and Requests everywhere else.

Main features:

* Memcache support
* Defaults to URL Fetch on App Engine
* Supports Requests everywhere else
* Supports OAuth1 authentication (requires `oauthlib`)

## Usage

This is the simplest way of using the library:

```
import pprint
from restwice import RestClient

SAMPLE_GET_ENDPOINT = 'http://httpbin.org/get'

# The client
rest_client = RestClient()
rest_client.set_endpoint(endpoint=SAMPLE_GET_ENDPOINT)
raw_result, cached_result = rest_client.do_get()

# Done
pprint.pprint(raw_result)
pprint.pprint(raw_result.get('url'))
pprint.pprint(cached_result)
```

The same exact code will work both on CLI and App Engine.

See `sample-cli` for a Requests-based sample, and `sample-appengine` for the App Engine equivalent. You can run both samples with `make sample`.
