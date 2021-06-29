from pyld import jsonld
from services.eoCollector import EOCollector
from models.eoGraph import EOGraph
from services.gcmdService import GcmdService

sentinel_data = ['Acquisition Type', 'Cycle number', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Orbit number (stop)', 'Pass direction', 'Polarisation', 
    'Resolution', 'Sensing start', 'Sensing stop', 'Satellite name', 'Satellite number', 
    'Instrument abbreviation', 'Instrument mode', 'Instrument swath', 'Instrument id', 
    'Instrument name', 'Instrument description', 'Platform id', 'Satellite description',
    'Datatake sensing start', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Pass direction', 'Sensing start', 'Sensing stop', 'Tile Identifier', 
    'Satellite name','Satellite number', 'Satellite', 'Instrument', 'Instrument abbreviation', 'Instrument mode', 
    'Instrument id', 'Instrument name', 'Platform id']

class GeoJsonProducer:
    def produceGeoJsonLd(data, structure, frame):
        
        result = EOCollector.collect(data, sentinel_data)

        result['eoPlatform'] = GcmdService.getPlatformUrl(result['Satellite'])
        result['eoInstrument'] = GcmdService.getInstrumentUrl(result['Instrument'])

        graph = EOGraph()

        graph.addEoTriples(structure, result)
    
        g = jsonld.from_rdf(graph.serialize())

        framed = jsonld.frame(g, frame)

        return framed