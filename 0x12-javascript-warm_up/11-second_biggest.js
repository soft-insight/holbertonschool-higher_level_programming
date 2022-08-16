#!/usr/bin/node

let array = process.argv.slice(2);

if (process.argv[2] == null || process.argv[3] == null) {
  console.log(0);
} else {
  array = array.map(Number);
  array = array.sort((a, b) => { return (b - a); });

  console.log(array);
  console.log(array[1]);
}
