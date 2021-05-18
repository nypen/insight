class Literal(Node):
    def __init__(
        self,
        nodeType,
        nodeValue,
    ):
        self.type = nodeType
        self.value = nodeValue 
        self.datatype = type(nodeValue).__name__
    
class Graph:
    def __init__(self):
        self.triples = []   

    def addTriple(subject, predicate, object):
        triple = {}
        triple["subject"] = subject
        triple["predicate"] = predicate
        triple["object"] = object