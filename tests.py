import urllib.request
import sys
import json
import models
from gcmdApi import GCMDApi
from pyld import jsonld

from getOAData import OpenAccessHubAPI
from eoCollector import EOCollector
from models.eoGraph import EOGraph
from models.node import Node
from models.literal import Literal

sentinel_data = ['Acquisition Type', 'Cycle number', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Orbit number (stop)', 'Pass direction', 'Polarisation', 
    'Resolution', 'Sensing start', 'Sensing stop', 'Satellite name', 'Satellite number', 
    'Instrument abbreviation', 'Instrument mode', 'Instrument swath', 'Instrument id', 
    'Instrument name', 'Instrument description', 'Platform id', 'Satellite description',
    'Datatake sensing start', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Pass direction', 'Sensing start', 'Sensing stop', 'Tile Identifier', 
    'Satellite name','Satellite number', 'Instrument abbreviation', 'Instrument mode', 
    'Instrument id', 'Instrument name', 'Platform id']

user = "pennypapadimas"
password = "pennypapadimas88"


ids = [
    "a239b5b3-62a4-4509-9bd6-ff6db6a3b40b",
    "c444677e-3484-49a7-b3fc-7e6282a044f9",
    "2b17b57d-fff4-4645-b539-91f305c27c69"
]

oah = OpenAccessHubAPI()
oah.login(user, password)

frame_file = open("./inputs/frame.json", "r")
frame = json.load(frame_file)

context_file = open("./context.json", "r")
context = json.load(context_file)

structure1_file = open("./inputs/structure1.json", "r")
structure1 = json.load(structure1_file)

for id in ids:

    result = oah.getProductData(id)

    print("---------------------------------------------------------------------------------------------------")
    print("Values collected from Copernicus for " + id)
    print("---------------------------------------------------------------------------------------------------")

    result = EOCollector.collect(result, sentinel_data)

    for key in result:
        print(key, " : ", result[key])

    print("---------------------------------------------------------------------------------------------------")
    print(id + " JSONLD")
    print("---------------------------------------------------------------------------------------------------")

    graph = EOGraph()

    graph.addEoTriples(structure1, result)

    g = jsonld.from_rdf(graph.get())
    compacted = jsonld.compact(g, "https://schema.org/docs/jsonldcontext.jsonld")

    framed = jsonld.frame(g, frame)
    print(json.dumps(framed, indent=2))
    print()
    print()

platformId = GCMDApi.getPlatformId("Sentinel-2A")

print(platformId)
