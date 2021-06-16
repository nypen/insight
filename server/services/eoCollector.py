import json
class EOCollector:

    # returns a dictionary containing all the data we can get
    # from Copernicus
    def collect_all(data):
        d = data['d']
        results = d['results']
        eoDictionary = {}

        for info in results:
            metadata = info['__metadata']
            eoDictionary[info['Id']] = info['Value']

        return eoDictionary

    # returns a dictionary containing only the data 
    # given in sentinelProperties

    def collect(data, sentinelProperties=None):
        d = data['d']
        results = d['results']

        eoDictionary = EOCollector.collect_all(data)

        if(sentinelProperties is not None):
            updatedEoDictionary = eoDictionary.copy()
            for prop in eoDictionary:
                if(prop not in sentinelProperties):
                    updatedEoDictionary.pop(prop)
            eoDictionary = updatedEoDictionary

        return eoDictionary