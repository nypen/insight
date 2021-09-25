from models.graph import Graph
from models.node import Node
from models.literal import Literal

class EOGraph(Graph):
    schema = "http://schema.org/{}"
    fnType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
    blankNode = "blank node"
    IRI = "IRI"    

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

                if(key=="id" or key not in values or not len(values[key])):
                    continue        
        
                obj = Literal(values[key])
            
                self.addTriple(subj, pred, obj)
