class Graph:
    def __init__(self):
        self.triples = []   

    def addTriple(subj, pred, obj):
        triple = {}
        triple["subject"] = subj
        triple["predicate"] = pred
        triple["object"] = obj

        self.triples.append(triple)

    def get(self):
        graph = {}
        graph["@graph"] = self.triples

        return graph