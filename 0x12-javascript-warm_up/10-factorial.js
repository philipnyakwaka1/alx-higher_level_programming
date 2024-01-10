#!/usr/bin/node
function myFactorial (num) {
  if (isNaN(num) || num === 1) {
    return 1;
  }
  return num * myFactorial(num - 1);
}
console.log(myFactorial(parseInt(process.argv[2])));
