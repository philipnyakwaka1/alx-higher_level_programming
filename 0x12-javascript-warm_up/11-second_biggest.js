#!/usr/bin/node
const vector = process.argv;
if (vector.length === 2 || vector.length == 3) {
  console.log(0);
} else {
  const myArray = [];
  const argv = vector.splice(2);
  for (let i = 0; i < argv.length; i++) {
    myArray.push(parseInt(argv[i]));
  }
  console.log(myArray.sort((a, b) => b - a)[1]);
}
