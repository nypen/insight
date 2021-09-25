import sys
import json
from services.oahService import OpenAccessHubService
from services.geoJsonProducer import GeoJsonProducer
from services.eoCollector import EOCollector
from services.configuration import Configuration

class RequestExecuter:
    def executeRequest(self, id, isSentinel5P, username, password, allAttributes=False):
        oah = OpenAccessHubService()
        data = oah.getProductData(username, password, id, isSentinel5P)

        result = None
        if(allAttributes):
            result =  EOCollector.collect(data)
        else:
            configuration = Configuration()
            result = GeoJsonProducer.produceGeoJsonLd(data, configuration.graphDefinition, configuration.types, configuration.frame)

        return result

