from pyld import jsonld
from services.eoCollector import EOCollector
from models.eoGraph import EOGraph
from services.gcmdService import GcmdService
from services.helpers import getValueBetweenTag, getValueBetween


class GeoJsonProducer:
    IRI = "https://scihub.copernicus.eu/dhus/search?q=identifier:{}"

    def produceGeoJsonLd(data, structure, types, frame):

        result = EOCollector.collect(data)

        result = GeoJsonProducer.annotate(result, structure)

        result = GeoJsonProducer.formatValues(result)

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

    def formatValues(values):
        for key in values.keys():
            if(key == "type"):
                values[key] = "POLYGON" if "Polygon" in values[key] else ""
            elif(key == "coordinates"):
                value = getValueBetweenTag("gml:coordinates", values[key])
                # values[key] = [value]
                coordinates = value.split(" ")
                coordinatesArray = []
                for coordinate in coordinates:
                    points = coordinate.split(",")
                    if(len(points[0]) and len(points[1])):
                        coordinatesArray.append(
                            [float(points[0]), float(points[1])])
                values[key] = [coordinatesArray]
            elif(key == "processingCenter"):
                value = getValueBetween("[", "]", values[key])
                values[key] = value
        return values
