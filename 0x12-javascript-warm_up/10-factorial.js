#!/usr/bin/node
function Recursive (Number, Factorial) {
  if (isNaN(Number) || (!Number)) {
    return (Factorial);
  } else {
    return (Recursive(Number - 1, Factorial * Number));
  }
}

if (isFinite(process.argv[2]) && (Number(process.argv[2]) >= 0)) {
  console.log(Recursive(process.argv[2], Number(1)));
}
