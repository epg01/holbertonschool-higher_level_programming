#!/usr/bin/node
function Recursive (Number, Factorial) {
  if (isNaN(Number) || (!Number)) {
    return (Factorial);
  } else {
    return (Recursive(Number - 1, Factorial * Number));
  }
}

if ((isFinite(process.argv[2]) && (Number(process.argv[2]) >= 0)) || (isNaN(process.argv[2]))) {
  if (1/Number(process.argv[2]) === -Infinity || 1/Number(process.argv[2]) === Infinity) {
    console.log(1);
    return ;
  }
  console.log(Recursive(process.argv[2], Number(1)));
}
