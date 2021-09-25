from pyld import jsonld
from services.eoCollector import EOCollector
from models.eoGraph import EOGraph
from services.gcmdService import GcmdService
from services.helpers import getValueBetweenTag


class GeoJsonProducer:
    IRI = "https://scihub.copernicus.eu/dhus/search?q=identifier:{}"

    def produceGeoJsonLd(data, structure, types, frame):

        result = EOCollector.collect(data)
        for i in result:
            print(i + ": " + result[i])
        print("--------------")
        print("-----------")

        result = GeoJsonProducer.annotate(result, structure)
        for i in result:
            print(i + ": " + result[i])
        print("--------------")
        print("-----------")

        result = GeoJsonProducer.formatValues(result)

        for i in result:
            print(i + ": " + result[i])
        print("--------------")
        print("-----------")

        graph = EOGraph()

        graph.addEoTriples(structure, result, types)

        g = jsonld.from_rdf(graph.serialize())

        framed = jsonld.frame(g, frame)

        return framed

    def annotate(data, annotations):
        annotatedData = {}
        for key in annotations.keys():
            if(type(annotations[key]) == type("")):
                value = ""
                if(annotations[key] in data.keys()):
                    value = data[annotations[key]]
                annotatedData[key] = value
            elif(type(annotations[key]) == type([])):
                for annotation in annotations[key]:
                    if(annotation in data.keys()):
                        annotatedData[key] = data[annotation]
            else:
                nested = GeoJsonProducer.annotate(data, annotations[key])
                annotatedData.update(nested)

        annotatedData['eoPlatform'] = GcmdService.getPlatformUrl(
            data['Satellite'])
        annotatedData['eoInstrument'] = GcmdService.getInstrumentUrl(
            data['Instrument'])
        annotatedData['eoEarthObservation'] = GeoJsonProducer.IRI.format(
            data['Identifier'])

        return annotatedData

    def formatValues(diction):
        for key in diction.keys():
            if(key == "type"):
                diction[key] = "POLYGON" if "Polygon" in diction[key] else ""
            elif(key == "coordinates"):
                value = getValueBetweenTag("gml:coordinates", diction[key])
                diction[key] = value

        return diction
