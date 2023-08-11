#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node getMovieCharacters.js <movie_id>');
  process.exit(1);
}

const filmsApiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieApiUrl = `${filmsApiUrl}${movieId}/`;

request(movieApiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('API responded with status code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  fetchAndDisplayCharacters(charactersUrls, 0);
});

function fetchAndDisplayCharacters (characterUrls, index) {
  if (index >= characterUrls.length) {
    process.exit(0);
  }

  const characterUrl = characterUrls[index];
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('API responded with status code:', response.statusCode);
      return;
    }

    const characterData = JSON.parse(body);
    console.log(characterData.name);

    fetchAndDisplayCharacters(characterUrls, index + 1);
  });
}
