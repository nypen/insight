from rdflib import Graph, plugin
from rdflib import Namespace
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, VOID, XMLNS, XSD
from rdflib import URIRef, BNode, Literal
from rdflib.serializer import Serializer
import json 

bob = URIRef("http://example.org/people/Bob")
linda = BNode()  # a GUID is generated

name = Literal('Bob')  # passing a string
age = Literal(24)  # passing a python int
height = Literal(76.5)  # passing a python float

n = Namespace("http://example.org/people/")

n.bob  # = rdflib.term.URIRef(u'http://example.org/people/bob')
n.eve  # = rdflib.term.URIRef(u'http://example.org/people/eve')

RDF.type
# = rdflib.term.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

FOAF.knows
# = rdflib.term.URIRef("http://xmlns.com/foaf/0.1/knows")

PROF.isProfileOf
# = rdflib.term.URIRef("http://www.w3.org/ns/dx/prof/isProfileOf")

SOSA.Sensor
# = rdflib.term.URIRef("http://www.w3.org/ns/sosa/Sensor")

g = Graph()
g.bind("foaf", FOAF)

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.knows, linda))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal("Linda")))

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


print(g.serialize(format="json-ld", indent=4))

print(g.serialize(format="json-ld", indent=4))
f = open("demofile2.txt", "wb")
f.write(g.serialize(format="json-ld", indent=4))
f.close()