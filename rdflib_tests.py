from rdflib import Graph, plugin
from rdflib import Namespace
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, VOID, XMLNS, XSD
from rdflib import URIRef, BNode, Literal
from rdflib.serializer import Serializer
import json 

RDF.type
# = rdflib.term.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

g = Graph()
g.bind("foaf", FOAF)

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

eoRef1 = URIRef("http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480")
eoRef2 = URIRef("http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3")
g.add((eoRef1, RDF.type, schemaorg.Instrument))

f = open("earthobservation.json", "wb")
f.write(g.serialize(format="json-ld", indent=4))
f.close()