#!/usr/bin/node

if (process.argv[2] && process.argv[3]) {
  const ArrayShallow2 = [];
  const ArrayShallow = Array.from(process.argv.splice(2));
  const IndexMaxNumber = ArrayShallow.indexOf(String(Math.max.apply(null, ArrayShallow)));

  for (let i = 0, j = 0; i < ArrayShallow.length; i++) {
    if (ArrayShallow[i] !== ArrayShallow[IndexMaxNumber]) {
      ArrayShallow2[j] = ArrayShallow[i];
      j++;
    }
  }

  console.log(Math.max.apply(null, ArrayShallow2));
} else {
  console.log(0);
}
