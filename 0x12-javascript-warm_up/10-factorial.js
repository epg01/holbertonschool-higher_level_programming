#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  let Factorial = Number(1);
  for (let i = Number(process.argv[2]); i > 0; i--) {
    Factorial = Factorial * i;
  }
  console.log(Factorial);
}
