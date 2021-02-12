#!/usr/bin/node
if (isFinite(process.argv[2])) {
  if (process.argv[2] > 0) {
    const square = 'X'.repeat(process.argv[2]);
    for (let i = 0; i < process.argv[2]; i++) {
      console.log(square);
    }
  }
} else {
  console.log('Missing size');
}
