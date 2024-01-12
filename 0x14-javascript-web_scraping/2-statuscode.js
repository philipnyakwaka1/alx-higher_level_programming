#!/usr/bin/node
const axios = require('axios');
async function getURL () {
  try {
    const response = await axios.get(process.argv[2]);
    console.log(response.status);
  } catch (err) {
    console.log(err.response.status);
  }
}
getURL();
