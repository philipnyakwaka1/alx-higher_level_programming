#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
async function getContent () {
  try {
    const response = await axios.get(process.argv[2]);
    fs.writeFile(process.argv[3], response.data, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  } catch (error) {
    console.log(error);
  }
}
getContent();
