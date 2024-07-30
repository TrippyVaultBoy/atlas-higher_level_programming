#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episode}`;

request.get(url, (err, response, content) => {
  if (err) {
    console.error(err);
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(content);
  console.log(data.title);
});