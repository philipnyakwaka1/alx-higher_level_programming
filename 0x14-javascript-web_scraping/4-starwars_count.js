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
        const regexID = /\/18\//;
        if (regexID.test(characters[j])) {
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
