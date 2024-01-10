#!/usr/bin/node
try {
  const number = parseInt(process.argv[2]);
  if (isNaN(number)) {
    throw new Error('Not a Number');
  }
  console.log(number);
} catch (error) {
  console.error(error.message);
}
