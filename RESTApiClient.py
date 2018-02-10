# *** IMPORTS *** #
import requests


# *** CLASS *** #
class RESTApiClient(object):

    # *** INIT *** #
    def __init__(self,
                 url,
                 params):

        self.url = url
        self.params = params

    # *** API *** #
    def get(self):

        return requests.get(url=self.url,
                            params=self.params)

    def post(self,
             headers,
             data):

        return requests.get(url=self.url,
                            params=self.params,
                            headers=headers,
                            data=data)
