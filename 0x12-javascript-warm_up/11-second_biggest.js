#!/usr/bin/node

if (process.argv[2] && process.argv[3]) {
  let Array_Shallow_2 = Array();
  let Array_Shallow = Array.from(process.argv.splice(2));
  let Max_Number = Math.max.apply(null, Array_Shallow);

  for (let i = 0, j = 0; i < Array_Shallow.length; i++) {
    if (Array_Shallow[i] != Max_Number) {
      Array_Shallow_2[j] = Array_Shallow[i];
      j++;
    }
  }

  console.log(Math.max.apply(null, Array_Shallow_2))
} else {
    console.log(0);
}
