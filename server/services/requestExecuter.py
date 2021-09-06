import sys
import json
from services.oahService import OpenAccessHubService
from services.geoJsonProducer import GeoJsonProducer
from services.eoCollector import EOCollector

class RequestExecuter:
    def executeRequest(self, id, isSentinel5P, username, password, allAttributes=False):
        oah = OpenAccessHubService()
        result = oah.getProductData(username, password, id, isSentinel5P)

        if(allAttributes):
            result =  EOCollector.collect(result)
        else:
            frame_file = open("./inputs/frame.json", "r")
            frame = json.load(frame_file)

            structure1_file = open("./inputs/structure1.json", "r")
            structure = json.load(structure1_file)

            types_file = open("./inputs/types.json", "r")
            types = json.load(types_file)

            result = GeoJsonProducer.produceGeoJsonLd(result, structure, types, frame)

        return result
