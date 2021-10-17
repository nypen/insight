from models.graph import Graph
from models.node import Node
from models.literal import Literal

class EOGraph(Graph):
    schema = "http://schema.org/{}"
    fnType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
    firstType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#first"
    restType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest"
    nilType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"
    blankNode = "blank node"
    IRI = "IRI"    

    def addCollection(self, values, parent):
        for i in range (0, len(values)):
            pred = Node(EOGraph.IRI, EOGraph.firstType)
            if(type(values[i])==type([])):
                obj = Node(EOGraph.blankNode)
                self.addTriple(parent, pred, obj)
                self.addCollection(values[i], obj)
            else:
                obj = Literal(values[i])
                self.addTriple(parent, pred, obj)

            pred = Node(EOGraph.IRI, EOGraph.restType)
            if(i==len(values)-1):
                obj = Node(EOGraph.IRI, EOGraph.nilType)
            else:
                obj = Node(EOGraph.blankNode)
            self.addTriple(parent, pred, obj)
            parent=obj

    def addEoTriples(self, graphDefinition, values, types, parent=None):
        for key in graphDefinition:
            pred = Node(EOGraph.IRI, EOGraph.schema.format(key))

            if(type(graphDefinition[key])==type({})):
                nestedGraphObject = graphDefinition[key]
                node = None

                if("id" in nestedGraphObject):
                    idValue = values[key] if key in values.keys() else ""
                    node = Node(EOGraph.IRI, idValue)
                else:
                    node = Node(EOGraph.blankNode)

                if(key in types.keys()):
                    typeValue = types[key]
                    self.addTriple(node, Node(EOGraph.IRI, EOGraph.fnType), Node(EOGraph.IRI, EOGraph.schema.format(typeValue)))
                
                if(parent!=None):
                    self.addTriple(parent, pred, node)

                self.addEoTriples(nestedGraphObject, values, types, node)
            else:
                subj = parent

                if(key=="id" or key not in values or not values[key]):
                    continue        
                
                if(type(values[key])==type([])):
                    obj = Node(EOGraph.blankNode)
                    self.addTriple(parent, pred, obj)
                    self.addCollection(values[key], obj)
                else:
                    obj = Literal(values[key])
                    self.addTriple(subj, pred, obj)
