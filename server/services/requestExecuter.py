import sys
import json
from services.oahService import OpenAccessHubService
from services.geoJsonProducer import GeoJsonProducer

class RequestExecuter:
    def executeRequest(self, id, username, password):
        oah = OpenAccessHubService()
        oah.login(username, password)

        data = oah.getProductData(id)

        frame_file = open("./inputs/frame.json", "r")
        frame = json.load(frame_file)

        structure1_file = open("./inputs/structure1.json", "r")
        structure = json.load(structure1_file)

        result = GeoJsonProducer.produceGeoJsonLd(data, structure, frame)

        return result