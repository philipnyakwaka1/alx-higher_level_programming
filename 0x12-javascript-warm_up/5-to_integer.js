#!/usr/bin/node
try {
  const number = parseInt(process.argv[2]);
  if (isNaN(number)) {
    throw new Error('Not a Number');
  }
  console.log('My number:', number);
} catch (error) {
  console.log(error.message);
}
