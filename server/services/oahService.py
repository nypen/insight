import requests
import json

class OpenAccessHubService:
    apihubUrl = 'https://apihub.copernicus.eu/apihub/odata/v1/Products(\'{}\')/Attributes?$format=json'
    s5phubPUrl = 'https://s5phub.copernicus.eu/dhus/odata/v1/Products(\'{}\')/Attributes?$format=json'

    def getProductData(self, username, password, productId, isSentinel5P):
        self.session = requests.Session()
        self.url = ""

        if(isSentinel5P):
            self.session.auth = ("s5pguest", "s5pguest")
            self.url = OpenAccessHubService.s5phubPUrl.format(productId)
        else:
            self.session.auth = (username, password)
            self.url = OpenAccessHubService.apihubUrl.format(productId)

        resp = self.session.get(
            self.url,
            auth=self.session.auth
        )
        resp.raise_for_status()
        return resp.json()