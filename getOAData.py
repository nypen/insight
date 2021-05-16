import requests
import json

class OpenAccessHubAPI:
    url = 'https://apihub.copernicus.eu/apihub/odata/v1/Products(\'{}\')/Attributes?$format=json'

    def login(self, username, password):
        self.session = requests.Session()

        if username and password:
            self.session.auth = (username, password)
            print(self.session.auth)

    def getProductData(self, productId):
        url = OpenAccessHubAPI.url.format(productId)
        resp = self.session.get(
            url,
            auth=self.session.auth
        )
        resp.raise_for_status()
        return resp.json()