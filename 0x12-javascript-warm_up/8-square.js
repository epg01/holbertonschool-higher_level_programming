#!/usr/bin/node

const num = parseInt(process.argv[2]);
let i = 0;

if (!num) {
  console.log('Missing size');
} else {
  for (; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
