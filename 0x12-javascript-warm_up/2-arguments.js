#!/usr/bin/node
let counter = Number();
process.argv.forEach((val, index) => {
  counter = Number(index);
});
if (counter === 1) {
  console.log('No argument');
} else if (counter === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
