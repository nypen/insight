import requests
import json

class OpenAccessHubAPI:
    url = 'https://scihub.copernicus.eu/apihub/odata/v1/Products(\'{}\')/Attributes?$format=json'

    def login(self, username, password):
        self.session = requests.Session()

        if user and password:
            self.session.auth = (user, password)

    def getProductData(self, productId):
        resp = self.session.get(
            OpenAccessHubAPI.url.format(productId),
            auth=self.session.auth
        )

        return resp.json()


user = "pennypapadimas"
password = "pennypapadimas88"
id1 = "2b17b57d-fff4-4645-b539-91f305c27c69"
id2 = "c444677e-3484-49a7-b3fc-7e6282a044f9"

oah = OpenAccessHubAPI()
oah.login(user, password)

result = oah.getProductData(id1)

print (result)

print(type(result))

# result = oah.getProductData(id2)

# print (result)
