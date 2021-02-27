import urllib.request
import sys
import json
import models

sentinel1_data = ['Acquisition Type', 'Cycle number', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Orbit number (stop)', 'Pass direction', 'Polarisation', 
    'Resolution', 'Sensing start', 'Sensing stop', 'Satellite name', 'Satellite number', 
    'Instrument abbreviation', 'Instrument mode', 'Instrument swath', 'Instrument id', 
    'Instrument name', 'Instrument description', 'Platform id', 'Satellite description']

sentinel2_data = ['Datatake sensing start', 'Ingestion Date', 'Mission datatake id', 
    'Orbit number (start)', 'Pass direction', 'Sensing start', 'Sensing stop', 'Tile Identifier', 
    'Satellite name','Satellite number', 'Instrument abbreviation', 'Instrument mode', 
    'identifier Instrument id', 'Instrument name', 'identifier Platform id']

with open('Responses/response.json') as f:
  data = json.load(f)

d = data['d']

results = d['results']
instr = models.eoInstrument()
platf = models.eoPlatform()
pr = models.eoAcquisitionParameters()

for info in results:
    metadata = info['__metadata']
    if(info['Id'] in sentinel1_data):
        if(info['Category'] == 'instrument'):
            if(info['Id'] == 'Resolution'):
                instr.resolution = info['Value']
            elif(info['Id'] == 'Instrument abbreviation'):
                instr.instrumentShortName = info['Value']
            elif(info['Id'] == 'Instrument mode'):
                instr.operationalMode = info['Value']
            elif(info['Id'] == 'Instrument swath'):
                instr.swathIdentifier = info['Value']
            elif(info['Id'] == 'Instrument'):
                instr.id = info['Value']
            elif(info['Id'] == 'Instrument name'):
                instr.name = info['Value']
            elif(info['Id'] == 'Instrument description'):
                instr.description = info['Value']
        
        if(info['Category'] == 'platform'):
            if(info['Id'] == 'Satellite name'):
                platf.platformShortName = info['Value']
            elif(info['Id'] == 'Satellite number'):
                platf.platformSerialIdentifier = info['Value']
            elif(info['Id'] == 'Platform id'):
                platf.identifier = info['Value']
            elif(info['Id'] == 'Satellite description'):
                platf.description = info['Value']
        
        if(info['Category'] == 'product'):
            if(info['Id'] == 'Acquisition Type'):
                pr.acquisitionType = info['Value']
            elif(info['Id'] == 'Cycle number'):
                pr.cycleNumber = info['Value']
            elif(info['Id'] == 'Ingestion Date'):
                pr.ascendingNodeDate = info['Value']
            elif(info['Id'] == 'Mission datatake id'):
                pr.acquisitionSubType = info['Value']
            elif(info['Id'] == 'Orbit number (start)'):
                pr.orbitNumber = info['Value']
            # elif(info['Id'] == 'Orbit number (stop)'):
            #     pr.orbitNumber = info['Value']
            #     print('product = ', pr.orbitNumber)
            elif(info['Id'] == 'Pass direction'):
                pr.orbitDirection = info['Value']
            elif(info['Id'] == 'Sensing start'):
                pr.beginningDateTime = info['Value']
            elif(info['Id'] == 'Sensing stop'):
                pr.endingDateTime = info['Value']
            elif(info['Id'] == 'Polarisation'):
                instr.polarisationChannels = info['Value']

instr2 = models.eoInstrument()
platf2 = models.eoPlatform()
pr2 = models.eoAcquisitionParameters()

for info in results:
    if(info['Id'] in sentinel2_data):
        if(info['Category'] == 'instrument'):
            if(info['Id'] == 'Instrument abbreviation'):
                instr2.instrumentShortName = info['Value']
            elif(info['Id'] == 'Instrument mode'):
                instr2.operationalMode = info['Value']
            elif(info['Id'] == 'Instrument'):
                instr2.id = info['Value']
            elif(info['Id'] == 'Instrument name'):
                instr2.name = info['Value']
        
        if(info['Category'] == 'platform'):
            if(info['Id'] == 'Satellite name'):
                platf2.platformShortName = info['Value']
            elif(info['Id'] == 'Platform id'):
                platf2.identifier = info['Value']
            elif(info['Id'] == 'Satellite number'):
                platf2.platformSerialIdentifier = info['Value']
        
        if(info['Category'] == 'product'):
            if(info['Id'] == 'Datatake sensing start'):
                pr2.beginningDateTime = info['Value']
            elif(info['Id'] == 'Ingestion Date'):
                pr2.ascendingNodeDate = info['Value']
            elif(info['Id'] == 'Mission datatake id'):
                pr2.acquisitionSubType = info['Value']
            elif(info['Id'] == 'Orbit number (start)'):
                pr2.orbitNumber = info['Value']
            elif(info['Id'] == 'Pass direction'):
                pr2.orbitDirection = info['Value']
            elif(info['Id'] == 'Sensing start'):
                pr2.beginningDateTime = info['Value']
            elif(info['Id'] == 'Sensing stop'):
                pr2.endingDateTime = info['Value']
            elif(info['Id'] == 'Sensing stop'):
                pr2.endingDateTime = info['Value']
            elif(info['Id'] == 'Tile Identifier'):
                pr2.titleId = info['Value']

print('\nSentinel_1 eoInstrument: \npolarisationChannels = ', instr.polarisationChannels, 
                                '\nresolution = ', instr.resolution,
                                '\ninstrumentShortName = ', instr.instrumentShortName,
                                '\noperationalMode = ', instr.operationalMode,
                                '\nswathIdentifier = ', instr.swathIdentifier,
                                '\nid = ', instr.id,
                                '\nname = ', instr.name,
                                '\ndescription = ', instr.description)

print('\nSentinel_1 eoPlatform: \nplatformShortName = ', platf.platformShortName, 
                            '\nplatformSerialIdentifier = ', platf.platformSerialIdentifier,
                            '\nidentifier = ', platf.identifier,
                            '\ndescription = ', platf.description)

print('\nSentinel_1 eoAcquisitionParameters: \nacquisitionType = ', pr.acquisitionType, 
                            '\ncycleNumber = ', pr.cycleNumber,
                            '\nascendingNodeDate = ', pr.ascendingNodeDate,
                            '\nacquisitionSubType = ', pr.acquisitionSubType,
                            '\norbitNumber = ', pr.orbitNumber,
                            '\norbitDirection = ', pr.orbitDirection,
                            '\nbeginningDateTime = ', pr.beginningDateTime,
                            '\nendingDateTime = ', pr.endingDateTime)   

print()

print('\nSentinel_2 eoInstrument: \ninstrumentShortName = ', instr2.instrumentShortName,
                                '\noperationalMode = ', instr2.operationalMode,
                                '\nid = ', instr2.id,
                                '\nname = ', instr2.name)

print('\nSentinel_2 eoPlatform: \nplatformShortName = ', platf2.platformShortName, 
                            '\nidentifier = ', platf2.identifier,
                            '\nplatformSerialIdentifier = ', platf2.platformSerialIdentifier)

print('\nSentinel_2 eoAcquisitionParameters: \nascendingNodeDate = ', pr2.ascendingNodeDate,
                            '\nbeginningDateTime = ', pr2.beginningDateTime,
                            '\nacquisitionSubType = ', pr2.acquisitionSubType,
                            '\norbitNumber = ', pr2.orbitNumber,
                            '\norbitDirection = ', pr2.orbitDirection,
                            '\nbeginningDateTime = ', pr2.beginningDateTime,
                            '\nendingDateTime = ', pr2.endingDateTime,
                            '\ntileId = ', pr2.tileId)             