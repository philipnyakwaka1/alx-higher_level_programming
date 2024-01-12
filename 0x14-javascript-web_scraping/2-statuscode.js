#!/usr/bin/node
const axios = require('axios');
async function getURL () {
  try {
    const response = await axios.get(process.argv[2]);
    console.log('code:', response.status);
  } catch (err) {
    console.log('code:', err.response.status);
  }
}
getURL();
