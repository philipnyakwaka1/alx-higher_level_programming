#!/usr/bin/node
const axios = require('axios');
async function getTitle () {
  try {
    const endpoint =
      'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
    const response = await axios.get(endpoint);
    console.log(response.data.title);
  } catch (error) {
    console.log(error.response.status);
  }
}
getTitle();
