from models.graph import Graph
from models.node import Node
from models.literal import Literal

class EOGraph(Graph):
    schema = "http://schema.org/{}"
    fnType = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
    blankNode = "blank node"
    IRI = "IRI"
    

    def addEoTriples(self, structure, values, types, parent=None):
        for key in structure:
            pred = Node(EOGraph.IRI, EOGraph.schema.format(key))
            # Node("IRI", "http://schema.org/EarthObservation")

            if(type(structure[key])==type({})):
                dictionary = structure[key]
                nodeType = Node(EOGraph.IRI, EOGraph.fnType)
                typeValue = types[key] if key in types.keys() else ""

                if("id" in dictionary):
                    value = values[key] if key in values.keys() else ""
                    idNode = Node(EOGraph.IRI, value)
                    self.addTriple(parent, pred, idNode)
                    
                    self.addTriple(idNode, nodeType, Node(EOGraph.IRI, EOGraph.schema.format(typeValue)))

                    self.addEoTriples(dictionary, values, types, idNode)
                else:
                    b = Node(EOGraph.blankNode)

                    self.addTriple(b, nodeType, Node(EOGraph.IRI, EOGraph.schema.format(typeValue)))
                    
                    if(parent!=None):
                        self.addTriple(parent, pred, b)

                    self.addEoTriples(structure[key], values, types, b)
            else:
                subj = parent

                if(key=="id"):
                    continue
                
                mappedValue = ""
                
                # if the key maps to a list, 
                # e.g. "beginningDateTime" : ["Sensing start", "Datatake sensing start"]
                # check all values of the list and keep the value that exists in collected valued
                if(type(structure[key])==type([])):
                    for value in structure[key]:
                        if(value in values):
                            mappedValue = value
                            break
                else:
                    if(structure[key] in values):
                        mappedValue = structure[key]
                
                if(mappedValue==""):
                    continue

                obj = Literal(values[mappedValue])
            
                self.addTriple(subj, pred, obj)
