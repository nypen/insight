import requests
import json

class OpenAccessHubService:
    url = 'https://apihub.copernicus.eu/apihub/odata/v1/Products(\'{}\')/Attributes?$format=json'

    def login(self, username, password):
        self.session = requests.Session()

        if username and password:
            self.session.auth = (username, password)

    def getProductData(self, productId):
        url = OpenAccessHubService.url.format(productId)
        resp = self.session.get(
            url,
            auth=self.session.auth
        )
        resp.raise_for_status()
        return resp.json()