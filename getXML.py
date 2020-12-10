import requests

# r = requests.get('https://xkcd.com/1906/')

# ploads = {'things':2,'total':25}
# r = requests.get('https://httpbin.org/get',params=ploads)

#You can also view the URL using the command 'r.url' as follows:

#Converting JSON to Python Dictionary
#You can see below 'r.json()' creates a Python dictionary from the JSON response given by the 'httpbin' website.


#https://requests.readthedocs.io/en/master/

# url = 'https://api.github.com/some/endpoint'
# >>> headers = {'user-agent': 'my-app/0.0.1'}

# >>> r = requests.get(url, headers=headers)


# api_url : string, optional
#     URL of the DataHub
#     defaults to 'https://scihub.copernicus.eu/apihub'

class eoAquisitionInformation
": {
"@type" : "AcquisitionInformation",
"eoInstrument": {
"@type" :"Instrument",
"id" : "http://gcmdservices.gsfc.nasa.gov/kms/concept/ed400e7c-229e-48be9a93-84f2fc864448",
"name" : "Synthetic Aperture Radar (C-band)",
"instrumentShortName" : "SAR-C SAR",
"description" : " https://sentinel.esa.int/web/sentinel/missions/
sentinel-1",
"polarisationChannels" : "VV VH",
"operationalMode" : "IW",
"swathIdentifier" : "IW"},
"eoPlatform": {
"@type":"Platform",
"id": "http://gcmdservices.gsfc.nasa.gov/kms/concept/c7279e54-f7c1-4ee7-
a957-719d6021a3f",
"description": "https://sentinel.esa.int/web/sentinel/missions/
sentinel-1",
"platformSerialIdentifier":"A",
"platformShortName":"Sentinel-1"},
"eoAcquisitionParameters": {
"@type" : "AcquisitionParameters",
"acquisitionType" : "NOMINAL",
"cycleNumber" : 154,
"ascendingNodeDate" : "2018-11-07T21:29:09.657Z",
"acquisitionSubType" : "175948",
"orbitNumber" : "24485",
"orbitDirection" : "ASCENDING",
"beginningDateTime" : "2018-11-07T17:25:04.147Z",
"endingDateTime" : "2018-11-07T17:25:29.145Z"}}

api_url = 'https://scihub.copernicus.eu/apihub/'
user = "pennypapadimas"
password = "pennypapadimas88"
id1 = "2b17b57d-fff4-4645-b539-91f305c27c69"
id2 = "c444677e-3484-49a7-b3fc-7e6282a044f9"

session = requests.Session()

if user and password:
    session.auth = (user, password)

api_url1 = api_url + "odata/v1/Products('{}')/Attributes?$format=json".format(id1)
api_url2 = api_url + "odata/v1/Products('{}')/Attributes?$format=json".format(id2)

resp = session.get(
    api_url1,
    auth = session.auth
    )
resp.raise_for_status()

print(resp.json())


