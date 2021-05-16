from pyld import jsonld
import json


json_file = open("./Output/Listing3_sel41.json", "r")
data = json.load(json_file)

context_file = open("./context.json", "r")
context = json.load(context_file)

graph = jsonld.to_rdf(data)


FNSubject = "subject"
FNObject = "object"
FNPredicate = "predicate"
FNDatatype = 'datatype'

FNType = "type"
FNValue = "value"

BlankNode = 'blank node'
IRI = 'IRI'
Literal = 'literal'


print(type(graph["@default"]))
print()
print()
print()
print()
for triple in graph["@default"]:
    print(triple)

print()
print(graph)

graph ={
  "@graph":[
    {
      "subject":{
        "type":"blank node",
        "value":"_:b0"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
      },
      "object":{
        "type":"IRI",
        "value":"http://schema.org/EarthObservation"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b0"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/eoAcquisitionInformation"
      },
      "object":{
        "type":"blank node",
        "value":"_:b1"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b1"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
      },
      "object":{
        "type":"IRI",
        "value":"http://schema.org/AcquisitionInformation"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b1"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/eoAcquisitionParameters"
      },
      "object":{
        "type":"blank node",
        "value":"_:b2"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b1"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/eoInstrument"
      },
      "object":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b1"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/eoPlatform"
      },
      "object":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
      },
      "object":{
        "type":"IRI",
        "value":"http://schema.org/AcquisitionParameters"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/acquisitionSubType"
      },
      "object":{
        "type":"literal",
        "value":"GS2A_20181107T105231_017637_N02.07",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/acquisitionType"
      },
      "object":{
        "type":"literal",
        "value":"NOMINAL",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/ascendingNodeDate"
      },
      "object":{
        "type":"literal",
        "value":"2018-11-07T16:36:06.154Z",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/beginningDateTime"
      },
      "object":{
        "type":"literal",
        "value":"2018-11-07T10:52:31.025Z",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/endingDateTime"
      },
      "object":{
        "type":"literal",
        "value":"2018-11-07T10:52:31.025Z",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/orbitDirection"
      },
      "object":{
        "type":"literal",
        "value":"DESCENDING",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/orbitNumber"
      },
      "object":{
        "type":"literal",
        "value":"17637",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"blank node",
        "value":"_:b2"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/tileId"
      },
      "object":{
        "type":"literal",
        "value":"31UFU",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
      },
      "object":{
        "type":"IRI",
        "value":"http://schema.org/Instrument"
      }
    },
    {
      "subject":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/instrumentShortName"
      },
      "object":{
        "type":"literal",
        "value":"MSI",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/name"
      },
      "object":{
        "type":"literal",
        "value":"Multi-Spectral Instrument",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/081f9b6e-d0a0-4f1d-ad8-638189418480"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/operationalMode"
      },
      "object":{
        "type":"literal",
        "value":"INS-NOBS",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
      },
      "object":{
        "type":"IRI",
        "value":"http://schema.org/Platform"
      }
    },
    {
      "subject":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/platformSerialIdentifier"
      },
      "object":{
        "type":"literal",
        "value":"A",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    },
    {
      "subject":{
        "type":"IRI",
        "value":"http://gcmdservices.gsfc.nasa.gov/kms/concept/2ce20983-98b2-40b9-bb0e-a08074fb93b3"
      },
      "predicate":{
        "type":"IRI",
        "value":"http://schema.org/platformShortName"
      },
      "object":{
        "type":"literal",
        "value":"Sentinel-2",
        "datatype":"http://www.w3.org/2001/XMLSchema#string"
      }
    }
  ]
}

g = jsonld.from_rdf(graph)

print(type(g))

for i in g:
    print(i)

compacted = jsonld.compact(g, "https://schema.org/docs/jsonldcontext.jsonld")
print(json.dumps(compacted, indent=2))


print()
print()
print()
print()
frame_file = open("./inputs/frame.json", "r")
frame = json.load(frame_file)

framed = jsonld.frame(g, frame)

print(json.dumps(framed, indent=2))
