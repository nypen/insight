import sys
import json
from services.oahService import OpenAccessHubService
from services.geoJsonProducer import GeoJsonProducer
from services.eoCollector import EOCollector

class RequestExecuter:
    def executeRequest(self, id, isSentinel5P, username, password, allAttributes=False):
        oah = OpenAccessHubService()
        data = oah.getProductData(username, password, id, isSentinel5P)

        result = None
        if(allAttributes):
            result =  EOCollector.collect(data)
        else:
            frame_file = open("./configurations/frame.json", "r")
            frame = json.load(frame_file)

            graphDefinition_file = open("./configurations/graphDefinition.json", "r")
            definition = json.load(graphDefinition_file)

            types_file = open("./configurations/types.json", "r")
            types = json.load(types_file)

            result = GeoJsonProducer.produceGeoJsonLd(data, definition, types, frame)

        return result

