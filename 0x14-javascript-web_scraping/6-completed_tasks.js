#!/usr/bin/node
const axios = require('axios');
async function listCompleted () {
  try {
    const response = await axios.get(process.argv[2]);
    const obj = {};
    for (let i = 0; i < response.data.length; i++) {
      if (response.data[i].completed) {
        const taskID = response.data[i].userId;
        if (obj[taskID] === undefined) {
          obj[taskID] = 0;
        }
        obj[taskID]++;
      }
    }
    console.log(obj);
  } catch (error) {
    console.log(error);
  }
}
listCompleted();
