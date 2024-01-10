#!/usr/bin/node
const myArray = [];
const argv = process.argv.splice(2);
for (let i = 0; i < argv.length; i++) {
  myArray.push(parseInt(argv[i]));
}
console.log(myArray.sort((a, b) => b - a)[1]);
