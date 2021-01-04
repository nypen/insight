import urllib.request
import sys
import json

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
print(type(d))

results = d['results']
print(type(results))

for info in results:
    # print(info['__metadata'])
    metadata = info['__metadata']
    if(info['Id'] in sentinel1_data):
        print("sentinel1 - ", info['Id'])
    
    if(info['Id'] in sentinel2_data):
        print("sentinel2 - ", info['Id'])
