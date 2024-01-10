#!/usr/bin/node
const argv = process.argv;
if (argv.length === undefined || argv.length === 2) {
  console.log(0);
} else {
  const newArgv = Array.from(argv).sort().slice(2);
  console.log(newArgv[newArgv.length - 2]);
}
