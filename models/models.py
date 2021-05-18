class eoInstrument:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.instrumentShortName = ""
        self.description = ""           # NOT in Sentinel 2
        self.polarisationChannels = ""  # NOT in Sentinel 2
        self.resolution = ""            # NOT in Sentinel 2
        self.operationalMode = ""
        self.swathIdentifier = ""       # NOT in Sentinel 2


class eoPlatform: 
    def __init__(self):
        self.identifier = ""
        self.description = ""
        self.platformSerialIdentifier = ""  #NOT in sentinel 2
        self.platformShortName = ""

class eoAcquisitionParameters:

    def __init__(self):
        self.acquisitionType = ""
        self.cycleNumber = ""
        self.ascendingNodeDate = ""
        self.acquisitionSubType = ""
        self.orbitNumber = ""
        self.orbitDirection = ""
        self.beginningDateTime = ""
        self.endingDateTime = ""
        self.tileId = ""                #ONLY IN SENTINEL 2
