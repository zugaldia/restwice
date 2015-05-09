import webapp2
from restwice import RestClient

SAMPLE_GET_ENDPOINT = 'http://httpbin.org/get'


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # The client
        rest_client = RestClient()
        rest_client.set_endpoint(endpoint=SAMPLE_GET_ENDPOINT)
        raw_result, cached_result = rest_client.do_get()

        # Done
        self.response.write('Hello from: ' + raw_result.get('url'))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
