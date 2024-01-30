#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const outputFile = process.argv[3];

const fileStream = fs.createWriteStream(outputFile);

fileStream.on('finish', () => {
  console.log(`File downloaded and saved as ${outputFile}`);
});

fileStream.on('error', (err) => {
  console.error('Error writing to file:', err);
});

request(url)
  .on('error', (err) => {
    console.error('Error downloading file:', err);
  })
  .pipe(fileStream);
