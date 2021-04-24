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

f = open("earthobservation.json", "wb")
f.write(g.serialize(format="json-ld", indent=4))
f.close()