
class EOCollector:

    def collect(data, sentinelProperties):
        d = data['d']
        results = d['results']
        eoDictionary = {}

        for info in results:
            metadata = info['__metadata']
            if(info['Id'] in sentinelProperties):
                eoDictionary[info['Id']] = info['Value']

        return eoDictionary