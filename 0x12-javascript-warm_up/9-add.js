#!/usr/bin/node
function add (a, b) {
  if (isFinite(a) && isFinite(b)) {
    return (Number(a) + Number(b));
  }
  return NaN;
}

console.log(add(process.argv[2], process.argv[3]));
