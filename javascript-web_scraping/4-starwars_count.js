#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, response, content) => {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode != 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }
  const movies = JSON.parse(content).results;
  const count = movies.filter((movie) => movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/'));
  console.log(count.length);
});
