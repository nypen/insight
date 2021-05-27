import requests

class GCMDApi():
    instrumentsUrl = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/instruments/?format=json'
    platformsUrl = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/platforms/?format=json'

    def getInstrumentId(instrumentPrefLabel):
        url  = GCMDApi.instrumentsUrl

        session = requests.Session()
        resp = session.get(url)
        
        resp.raise_for_status()

        jsonResponse = resp.json()
        concepts = jsonResponse["concepts"]

        for concept in concepts:
            if(concept["prefLabel"] == instrumentPrefLabel):
                return concept["uuid"]
    
    def getPlatformId(platformPrefLabel):
        url  = GCMDApi.platformsUrl

        session = requests.Session()
        resp = session.get(url)

        jsonResponse = resp.json()
        concepts = jsonResponse["concepts"]

        for concept in concepts:
            if(concept["prefLabel"] == platformPrefLabel):
                return concept["uuid"]