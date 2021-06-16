from models.literal import Literal
from rdflib import Graph
import json
class Graph:
    def __init__(self):
        self.triples = []   

    def addTriple(self, subj, pred, obj):
        triple = {}
        triple["subject"] = {
            "type": subj.type,
            "value": subj.value
        }
        triple["predicate"] = {
            "type": pred.type,
            "value": pred.value
        }
        triple["object"] = {
            "type": obj.type,
            "value": obj.value
        }

        if(isinstance(obj, Literal)):
            triple["object"]["datatype"] = obj.datatype

        self.triples.append(triple)

    def serialize(self):
        graph = {}
        graph["@graph"] = self.triples

        return graph


    def printRdf(self, fname="./Output/rdfGraph.json"):
        graph = self.serialize()
        file = open(fname, mode="w")
        file.write(json.dumps(graph, indent=4))
    