import json

class Configuration:
    def __init__(self):
        pfile = open("./configurations/frame.json", "r")
        self.frame = json.load(pfile)
        pfile.close()
        
        pfile = open("./configurations/graphDefinition.json", "r")
        self.graphDefinition = json.load(pfile)
        pfile.close()
        
        pfile = open("./configurations/types.json", "r")
        self.types = json.load(pfile)
        pfile.close()
