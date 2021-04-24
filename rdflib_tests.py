# pip install rdflib
# pip install rdflib-jsonld

from rdflib import Graph, plugin
from rdflib import Namespace
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, VOID, XMLNS, XSD
from rdflib import URIRef, BNode, Literal
from rdflib.serializer import Serializer
import json 



RDF.type
# = rdflib.term.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

g = Graph()

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

eoNode = BNode()
g.add((eoNode, RDF.type, schemaorg.EarthObservation))


    # "eoPlatform": {
    #   "@type":"Platform",
    #   "id": "http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3",
    #   "platformSerialIdentifier":"A",
    #   "platformShortName":"Sentinel-2"
    # }

eoPlatform = URIRef("http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3")
g.add((eoPlatform, RDF.type, schemaorg.Platform))
g.add((eoPlatform, schemaorg.platformSerialIdentifier, Literal("A")))
g.add((eoPlatform, schemaorg.platformShortName, Literal("Sentinel-2")))

f = open("earthobservation.json", "wb")
f.write(g.serialize(format="json-ld", indent=4))
f.close()