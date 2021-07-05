import requests
import json

class OpenAccessHubService:
    url = 'https://apihub.copernicus.eu/apihub/odata/v1/Products(\'{}\')/Attributes?$format=json'
    sentinel5PUrl = 'https://s5phub.copernicus.eu/dhus/odata/v1/Products(\'{}\')/Attributes?$format=json'
    def login(self, username, password):
        self.session = requests.Session()

        if username and password:
            self.session.auth = (username, password)

    def getProductData(self, productId, isSentinel5P):
        if(isSentinel5P):
            self.session.auth = ("s5pguest", "s5pguest")

        url = OpenAccessHubService.url.format(productId) if not isSentinel5P else OpenAccessHubService.sentinel5PUrl.format(productId)

        resp = self.session.get(
            url,
            auth=self.session.auth
        )
        resp.raise_for_status()
        return resp.json()