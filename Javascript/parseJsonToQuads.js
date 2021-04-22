import {JsonLdParser} from "jsonld-streaming-parser";
import * as fs from 'fs';

const myParser = new JsonLdParser();

fs.createReadStream('../Output/Listing3_sel41.json')
  .pipe(myParser)
  .on('data', console.log)
  .on('error', console.error)
  .on('end', () => console.log('All triples were parsed!'));


//  npm install jsonld-streaming-parser
// 
//  run script: node .\parseJsonToQuads.js