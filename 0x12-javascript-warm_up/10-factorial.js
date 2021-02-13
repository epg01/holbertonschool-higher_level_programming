#!/usr/bin/node
function Recursive (number) {
  if (!number || isNaN(number)) {
    return (1);
  } else {
    return (number * Recursive(number - 1));
  }
}

function Control () {
  if (isFinite(process.argv[2]) && (Number(process.argv[2]) < 0)) {
    return undefined;
  } else if (isFinite(process.argv[2]) && (Number(process.argv[2]) === Number(0))) {
    console.log(1);
  } else {
    console.log(Recursive(process.argv[2]));
  }
}

Control();
