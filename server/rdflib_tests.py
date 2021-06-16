# pip install rdflib
# pip install rdflib-jsonld

from rdflib import Graph, plugin
from rdflib import Namespace
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, VOID, XMLNS, XSD
from rdflib import URIRef, BNode, Literal
from rdflib.serializer import Serializer
import json 

# RDF.type
# = rdflib.term.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

# Quad {
#   termType: 'Quad',
#   value: '',
#   subject: BlankNode { termType: 'BlankNode', value: 'df_0_2' },
#   predicate: NamedNode {
#     termType: 'NamedNode',
#     value: 'http://schema.org/eoAquisitionInformation'
#   },
#   object: BlankNode { termType: 'BlankNode', value: 'df_0_1' },
#   graph: DefaultGraph { termType: 'DefaultGraph', value: '' }
# }

g = Graph()
schemaorg = Namespace("http://schema.org/")
b0 = URIRef("_:b0")
b1 = URIRef("_:b1")
b2 = URIRef("_:b2")

# eoRef1 = URIRef("http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480")
# eoRef2 = URIRef("http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3")
# g.add((eoRef1, RDF.type, schemaorg.Instrument))
g.add((b0, RDF.type, schemaorg.EarthObservation))
g.add((b0, schemaorg.eoAquisitionInformation, b1))

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


#     "eoInstrument": {
#       "@type" :"Instrument",
#       "id" : "http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480",
#       "name" : "Multi-Spectral Instrument",
#       "instrumentShortName" : "MSI",
#       "operationalMode" : "INS-NOBS"
eoInstrument = URIRef("http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480")
g.add((b1, schemaorg.eoInstrument, eoInstrument))
g.add((eoInstrument, schemaorg.instrumentShortName, Literal("MSI")))
g.add((eoInstrument, schemaorg.name, Literal("Multi-Spectral Instrument")))
g.add((eoInstrument, schemaorg.operationalMode, Literal("INS-NOBS")))

# "eoAcquisitionParameters": {
#       "@type" : "AcquisitionParameters",
#       "acquisitionType" : "NOMINAL",
#       "ascendingNodeDate" : "2018-11-07T16:36:06.154Z",
#       "acquisitionSubType" : "GS2A_20181107T105231_017637_N02.07",
#       "orbitNumber" : "17637",
#       "orbitDirection" : "DESCENDING",
#       "beginningDateTime" : "2018-11-07T10:52:31.025Z",
#       "endingDateTime" : "2018-11-07T10:52:31.025Z",
#       "tileId" : "31UFU"
g.add((b1, schemaorg.AcquisitionParameters, b2))
g.add((b1, RDF.type, schemaorg.AcquisitionParameters))
g.add((b2, schemaorg.acquisitionType, Literal("NOMINAL")))
g.add((b2, schemaorg.ascendingNodeDate, Literal("2018-11-07T16:36:06.154Z")))
g.add((b2, schemaorg.acquisitionSubType, Literal("GS2A_20181107T105231_017637_N02.07")))
g.add((b2, schemaorg.orbitNumber, Literal("17637")))
g.add((b2, schemaorg.orbitDirection, Literal("DESCENDING")))
g.add((b2, schemaorg.beginningDateTime, Literal("2018-11-07T10:52:31.025Z")))
g.add((b2, schemaorg.endingDateTime, Literal("2018-11-07T10:52:31.025Z")))
g.add((b2, schemaorg.tileId, Literal("31UFU")))




f = open("earthobservation.json", "wb")
f.write(g.serialize(format="json-ld", indent=4))
f.close()