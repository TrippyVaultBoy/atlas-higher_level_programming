#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filepath = process.argv[3];

request.get(url, (err, response, content) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch webpage. Status code: ${response.statusCode}`);
    return;
  }
  fs.writeFile(filepath, content, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing file:', err);
    }
  });
});
