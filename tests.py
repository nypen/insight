import urllib.request
import sys
import json
import models
from pyld import jsonld

from getOAData import OpenAccessHubAPI
from eoCollector import EOCollector
from models.graph import Graph
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
    'identifier Instrument id', 'Instrument name', 'identifier Platform id']

print("---------------------------------------------------------------------------------------------------")      
print("---------------------------------------------------------------------------------------------------")      
print("---------------------------------------------------------------------------------------------------")      
print("---------------------------------------------------------------------------------------------------")

user = "pennypapadimas"
password = "pennypapadimas88"
id1 = "2b17b57d-fff4-4645-b539-91f305c27c69"
id2 = "c444677e-3484-49a7-b3fc-7e6282a044f9"

oah = OpenAccessHubAPI()
oah.login(user, password)

result1 = oah.getProductData(id1)
result2 = oah.getProductData(id2)

print (result1)

print("---------------------------------------------------------------------------------------------------")      
print("---------------------------------------------------------------------------------------------------")      

print (result2)

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

fnType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
fnblankNodeType = "blank node"

b1 = Node(fnblankNodeType, "b1")
pred = Node("IRI", "http://schema.org/eoInstrument")
eoInstrument = Node("IRI", "http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480")

graph = Graph()


graph.addTriple(b1, pred, eoInstrument)

#     "eoInstrument": {
#       "@type" :"Instrument",
#       "id" : "http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480",
#       "name" : "Multi-Spectral Instrument",
#       "instrumentShortName" : "MSI",
#       "operationalMode" : "INS-NOBS"

graph.addTriple(eoInstrument, Node("IRI", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), Node("IRI", "http://schema.org/Instrument"))
graph.addTriple(eoInstrument, Node("IRI", "http://schema.org/eoInstrumentShortName"), Literal("MSI"))
graph.addTriple(eoInstrument, Node("IRI", "http://schema.org/name"), Literal("Multi-Spectral Instrument"))
graph.addTriple(eoInstrument, Node("IRI", "http://schema.org/operationalMode"), Literal("INS-NOBS"))

# "eoPlatform": {
#   "@type":"Platform",
#   "id": "http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3",
#   "platformSerialIdentifier":"A",
#   "platformShortName":"Sentinel-2"
# }
eoPlatform = URIRef("http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3")


g.add((b1, schemaorg.eoPlatform, eoPlatform))
g.add((eoPlatform, RDF.type, schemaorg.Platform))
g.add((eoPlatform, schemaorg.platformSerialIdentifier, Literal("A")))
g.add((eoPlatform, schemaorg.platformShortName, Literal("Sentinel-2")))

b1 = Node(fnblankNodeType, "b1")
pred = Node("IRI", "http://schema.org/eoPlatform")
eoPlatform = Node("IRI", "http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3")

graph.addTriple(b1, pred, eoPlatform)
graph.addTriple(eoPlatform, pred, eoPlatform)

graph.get()

g = jsonld.from_rdf(graph.get())

compacted = jsonld.compact(g, "https://schema.org/docs/jsonldcontext.jsonld")
print(json.dumps(compacted, indent=2))


print()
print()
print()
print()
frame_file = open("./inputs/frame.json", "r")
frame = json.load(frame_file)

framed = jsonld.frame(g, frame)

print(json.dumps(framed, indent=2))

# with open('Responses/response.json') as f:
#   data = json.load(f)

# d = data['d']

# results = d['results']

# diction = {}

# for info in results:
#     metadata = info['__metadata']
#     if(info['Id'] in sentinel1_data):
#         diction[info['Id']] = info['Value']

# for key in diction:
#     print(key, " : ", diction[key])

# # instr = models.eoInstrument()
# # platf = models.eoPlatform()
# # pr = models.eoAcquisitionParameters()


# # instr.resolution = info['Value']
# # instr.instrumentShortName = info['Value']
# # instr.operationalMode = info['Value']
# # instr.swathIdentifier = info['Value']
# # instr.id = info['Value']
# # instr.name = info['Value']
# # instr.description = info['Value']

# if(info['Category'] == 'instrument'):
#     if(info['Id'] == 'Resolution'):
#     elif(info['Id'] == 'Instrument abbreviation'):
#     elif(info['Id'] == 'Instrument mode'):
#     elif(info['Id'] == 'Instrument swath'):
#     elif(info['Id'] == 'Instrument'):
#     elif(info['Id'] == 'Instrument name'):
#     elif(info['Id'] == 'Instrument description'):

# if(info['Category'] == 'platform'):
#     if(info['Id'] == 'Satellite name'):
#     elif(info['Id'] == 'Satellite number'):
#     elif(info['Id'] == 'Platform id'):
#     elif(info['Id'] == 'Satellite description'):

# if(info['Category'] == 'product'):
#     if(info['Id'] == 'Acquisition Type'):
#     elif(info['Id'] == 'Cycle number'):
#     elif(info['Id'] == 'Ingestion Date'):
#     elif(info['Id'] == 'Mission datatake id'):
#     elif(info['Id'] == 'Orbit number (start)'):
#     # elif(info['Id'] == 'Orbit number (stop)'):
#     #     print('product = ', pr.orbitNumber)
#     elif(info['Id'] == 'Pass direction'):
#     elif(info['Id'] == 'Sensing start'):
#     elif(info['Id'] == 'Sensing stop'):
#     elif(info['Id'] == 'Polarisation'):
#         platf.platformShortName = info['Value']
#         platf.platformSerialIdentifier = info['Value']
#         platf.identifier = info['Value']
#         platf.description = info['Value']
#         pr.acquisitionType = info['Value']
#         pr.cycleNumber = info['Value']
#         pr.ascendingNodeDate = info['Value']
#         pr.acquisitionSubType = info['Value']
#         pr.orbitNumber = info['Value']
#     #     pr.orbitNumber = info['Value']
#         pr.orbitDirection = info['Value']
#         pr.beginningDateTime = info['Value']
#         pr.endingDateTime = info['Value']
#         instr.polarisationChannels = info['Value']

# # instr2 = models.eoInstrument()
# # platf2 = models.eoPlatform()
# # pr2 = models.eoAcquisitionParameters()

# # for info in results:
# #     if(info['Id'] in sentinel2_data):
# #         if(info['Category'] == 'instrument'):
# #             elif(info['Id'] == 'Instrument'):
# #                 instr2.id = info['Value']
        
# #         if(info['Category'] == 'platform'):
        
# #         if(info['Category'] == 'product'):
# #             elif(info['Id'] == 'Sensing start'):
# #                 pr2.beginningDateTime = info['Value']
# #             elif(info['Id'] == 'Sensing stop'):
# #                 pr2.endingDateTime = info['Value']
# #             elif(info['Id'] == 'Sensing stop'):
# #                 pr2.endingDateTime = info['Value']
# #             elif(info['Id'] == 'Tile Identifier'):
# #                 pr2.titleId = info['Value']

# # print('\nSentinel_1 eoInstrument: \npolarisationChannels = ', instr.polarisationChannels, 
# #                                 '\nresolution = ', instr.resolution,
# #                                 '\ninstrumentShortName = ', instr.instrumentShortName,
# #                                 '\noperationalMode = ', instr.operationalMode,
# #                                 '\nswathIdentifier = ', instr.swathIdentifier,
# #                                 '\nid = ', instr.id,
# #                                 '\nname = ', instr.name,
# #                                 '\ndescription = ', instr.description)

# # print('\nSentinel_1 eoPlatform: \nplatformShortName = ', platf.platformShortName, 
# #                             '\nplatformSerialIdentifier = ', platf.platformSerialIdentifier,
# #                             '\nidentifier = ', platf.identifier,
# #                             '\ndescription = ', platf.description)

# # print('\nSentinel_1 eoAcquisitionParameters: \nacquisitionType = ', pr.acquisitionType, 
# #                             '\ncycleNumber = ', pr.cycleNumber,
# #                             '\nascendingNodeDate = ', pr.ascendingNodeDate,
# #                             '\nacquisitionSubType = ', pr.acquisitionSubType,
# #                             '\norbitNumber = ', pr.orbitNumber,
# #                             '\norbitDirection = ', pr.orbitDirection,
# #                             '\nbeginningDateTime = ', pr.beginningDateTime,
# #                             '\nendingDateTime = ', pr.endingDateTime)   

# # print()

# # print('\nSentinel_2 eoInstrument: \ninstrumentShortName = ', instr2.instrumentShortName,
# #                                 '\noperationalMode = ', instr2.operationalMode,
# #                                 '\nid = ', instr2.id,
# #                                 '\nname = ', instr2.name)

# # print('\nSentinel_2 eoPlatform: \nplatformShortName = ', platf2.platformShortName, 
# #                             '\nidentifier = ', platf2.identifier,
# #                             '\nplatformSerialIdentifier = ', platf2.platformSerialIdentifier)

# # print('\nSentinel_2 eoAcquisitionParameters: \nascendingNodeDate = ', pr2.ascendingNodeDate,
# #                             '\nbeginningDateTime = ', pr2.beginningDateTime,
# #                             '\nacquisitionSubType = ', pr2.acquisitionSubType,
# #                             '\norbitNumber = ', pr2.orbitNumber,
# #                             '\norbitDirection = ', pr2.orbitDirection,
# #                             '\nbeginningDateTime = ', pr2.beginningDateTime,
# #                             '\nendingDateTime = ', pr2.endingDateTime,
# #                             '\ntileId = ', pr2.tileId)       

