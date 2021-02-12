#!/usr/bin/node
function Recursive (Number, Factorial) {
  if (isNaN(Number) || (!Number)) {
    return (Factorial);
  }
  else {
    return (Recursive(Number - 1, Factorial * Number));
  }
}

console.log(Recursive(process.argv[2], Number(1)));
