import requests

class GcmdService():
    instrumentsUrl = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/instruments/?format=json'
    platformsUrl = 'https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/platforms/?format=json'
    conceptUrl = 'https://gcmd.earthdata.nasa.gov/kms/concept/{}'

    def getInstrumentUrl(instrumentPrefLabel):
        url  = GcmdService.instrumentsUrl

        session = requests.Session()
        resp = session.get(url)
        
        resp.raise_for_status()

        jsonResponse = resp.json()
        concepts = jsonResponse["concepts"]

        for concept in concepts:
            if(concept["prefLabel"] == instrumentPrefLabel):
                return GcmdService.conceptUrl.format(concept["uuid"])
    
    def getPlatformUrl(platformPrefLabel):
        url  = GcmdService.platformsUrl

        session = requests.Session()
        resp = session.get(url)

        jsonResponse = resp.json()
        concepts = jsonResponse["concepts"]

        for concept in concepts:
            if(concept["prefLabel"] == platformPrefLabel):
                return GcmdService.conceptUrl.format(concept["uuid"])