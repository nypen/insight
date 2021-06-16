class Node:
    count = 0
    def __init__(
        self,
        nodeType,
        nodeValue=None,
    ):
        self.type = nodeType
        self.value = nodeValue

        if(self.value==None):
            self.value = "_:b{}".format(Node.count)
            Node.count+=1