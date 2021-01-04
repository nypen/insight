class eoInstrument:
    def __init__(
        self,
        id,
        name,
        instrumentShortName,
        description,                # NOT in Sentinel 2
        polarisationChannels,       # NOT in Sentinel 2
        operationalMode,
        swathIdentifier             # NOT in Sentinel 2
    ):
            self.id = ""
            self.name = ""
            self.instrumentShortName = ""
            self.description = ""
            self.polarisationChannels = ""
            self.operationalMode = ""
            self.swathIdentifier = ""


class eoPlatform: 
    def __init__(
        self,
        id,
        description,           
        platformSerialIdentifier,
        platformShortName
    ):
        self.id = ""
        self.description = ""
        self.platformSerialIdentifier = ""
        self.platformShortName = ""

class eoAcquisitionParameters:

    def __init__(
        self,
        acquisitionType,
        cycleNumber,
        ascendingNodeDate,
        acquisitionSubType,
        orbitNumber,
        orbitDirection,
        beginningDateTime,
        endingDateTime,
        #ascendingNodeDate
        #tileId     ONLY IN SENTINEL 2
    ):
        self.id = ""
        self.description = ""
        self.platformSerialIdentifier = ""
        self.platformShortName = ""


