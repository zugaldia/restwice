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
