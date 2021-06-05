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

sentinel1_data = ['Acquisition Type', 'Cycle number', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Orbit number (stop)', 'Pass direction', 'Polarisation', 
    'Resolution', 'Sensing start', 'Sensing stop', 'Satellite name', 'Satellite number', 
    'Instrument abbreviation', 'Instrument mode', 'Instrument swath', 'Instrument id', 
    'Instrument name', 'Instrument description', 'Platform id', 'Satellite description']

sentinel2_data = ['Datatake sensing start', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Pass direction', 'Sensing start', 'Sensing stop', 'Tile Identifier', 
    'Satellite name','Satellite number', 'Instrument abbreviation', 'Instrument mode', 
    'Instrument id', 'Instrument name', 'Platform id']

user = "pennypapadimas"
password = "pennypapadimas88"
id1 = "2b17b57d-fff4-4645-b539-91f305c27c69"
id2 = "c444677e-3484-49a7-b3fc-7e6282a044f9"

oah = OpenAccessHubAPI()
oah.login(user, password)

result1 = oah.getProductData(id1)
result2 = oah.getProductData(id2)

print("---------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------")

result1 = EOCollector.collect(result1, sentinel1_data)
result2 = EOCollector.collect(result2, sentinel2_data)

for key in result1:
    print(key, " : ", result1[key])

print("---------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------")

for key in result2:
    print(key, " : ", result2[key])

frame_file = open("./inputs/frame.json", "r")
frame = json.load(frame_file)

context_file = open("./context.json", "r")
context = json.load(context_file)

print("---------------------------------------------------------------------------------------------------")
print("Sentinel 1 JSONLD")
print("---------------------------------------------------------------------------------------------------")

graph1 = EOGraph()

structure1_file = open("./inputs/structure1.json", "r")
structure1 = json.load(structure1_file)

graph1.addEoTriples(structure1, result1)

g1 = jsonld.from_rdf(graph1.get())
compacted = jsonld.compact(g1, "https://schema.org/docs/jsonldcontext.jsonld")

framed = jsonld.frame(g1, frame)
print(json.dumps(framed, indent=2))


print("---------------------------------------------------------------------------------------------------")      
print("Sentinel 2 JSONLD")
print("---------------------------------------------------------------------------------------------------")

graph2 = EOGraph()

structure2_file = open("./inputs/structure2.json", "r")
structure2 = json.load(structure2_file)

graph2.addEoTriples(structure2, result2)

graph2.get()

g2 = jsonld.from_rdf(graph2.get())

framed = jsonld.frame(g2, frame)

print(json.dumps(framed, indent=2))

compacted = jsonld.compact(g2, "https://schema.org/docs/jsonldcontext.jsonld")

platformId = GCMDApi.getPlatformId("Sentinel-2A")

print(platformId)
