from models.literal import Literal
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

    def get(self):
        graph = {}
        graph["@graph"] = self.triples

        return graph