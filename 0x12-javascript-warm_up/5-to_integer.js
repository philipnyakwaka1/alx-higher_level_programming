#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.error('Not a Number');
} else {
  console.log('My number:', number);
}
