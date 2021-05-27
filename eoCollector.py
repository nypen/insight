import json
class EOCollector:

    def collect(data, sentinelProperties):
        d = data['d']
        results = d['results']
        eoDictionary = {}
     
        mapping_file = open("./inputs/mapping.json", "r")
        mapping_data = json.load(mapping_file)

        for info in results:
            metadata = info['__metadata']
            if(info['Id'] in sentinelProperties):
                eoDictionary[mapping_data[info['Id']]] = info['Value']

        return eoDictionary