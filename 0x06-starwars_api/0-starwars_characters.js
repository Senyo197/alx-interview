#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const fetch = url => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const fetchCharacters = async (movieId) => {
  try {
    const movieData = await fetch(`https://swapi-api.alx-tools.com/api/films/${movieId}/`);
    const characterPromises = movieData.characters.map(url => fetch(url));
    const characters = await Promise.all(characterPromises);
    characters.forEach(character => console.log(character.name));
  } catch (error) {
    console.error(error);
  }
};

fetchCharacters(movieId);
