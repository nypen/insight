from models.node import Node
class Literal(Node):
    def __init__(
        self,
        nodeValue,
    ):
        self.type = "Literal"
        self.value = nodeValue 
        self.datatype = "http://www.w3.org/2001/XMLSchema#string"
    
class Graph:
    def __init__(self):
        self.triples = []   

    def addTriple(subject, predicate, object):
        triple = {}
        triple["subject"] = subject
        triple["predicate"] = predicate
        triple["object"] = object