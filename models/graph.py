from models.literal import Literal
from rdflib import Graph
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

    def get_rdf(self, fname):
        graph = self.get()
        print(type(graph))
        file = open(fname+".json", mode="w")
        first = True
        tr = graph["@graph"]
        file.write("{\n\"@graph\":[\n")
        for t in tr:   
            sub = t["subject"]
            pr = t["predicate"]
            ob = t["object"]
            if first:
                first = False
                file.write("{\n\t\"subject\":{\n")
            else:
                file.write(",\n{\n\t\"subject\":{\n")
            file.write("\t\t" + "\"type\":" + "\"" + str(sub["type"]) + "\"" + ",\n")
            file.write("\t\t" + "\"value\":" + "\"" + str(sub["value"]) + "\"" + "\n")
            file.write("\t},\n\t\"predicate\":{\n")
            file.write("\t\t" + "\"type\":"  + "\"" + str(pr["type"]) + "\"" + ",\n")
            file.write("\t\t" + "\"value\":" + "\"" + str(pr["value"]) + "\"" + "\n")
            file.write("\t},\n\t\"object\":{\n")
            file.write("\t\t" + "\"type\":"  + "\"" + str(ob["type"])+  "\"" + ",\n")
            file.write("\t\t" + "\"value\":" + "\"" + str(ob["value"]) + "\"")
            if "datatype" in ob:
                file.write(",\n" + "\t\t" + "\"datatype\":" + "\"" + str(ob["datatype"]) + "\"" + "\n\t}\n")
            else:
                file.write("\n\t}\n")

            file.write("}")
        file.write("\n]\n}")

        # file.write(str(self.get()))            
        # graph.serialize(destination='output.txt', format='turtle')