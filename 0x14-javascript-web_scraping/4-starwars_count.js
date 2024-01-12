#!/usr/bin/node
const axios = require('axios');
let count = 0;
async function getTitle () {
  try {
    const response = await axios.get(process.argv[2]);
    const movies = response.data.results;
    for (let i = 0; i < movies.length; i++) {
      const characters = movies[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (
          characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/'
        ) {
          count++;
        }
      }
    }
    console.log(count);
  } catch (error) {
    console.log(error);
  }
}
getTitle();
