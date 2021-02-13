#!/usr/bin/node
let Argument = Number(0);
exports.logMe = function (item) {
  console.log(Argument + ': ' + `${item}`);
  Argument++;
};
