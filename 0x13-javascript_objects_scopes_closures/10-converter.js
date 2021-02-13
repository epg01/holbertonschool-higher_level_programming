#!/usr/bin/node

exports.converter = function (base) {
  function Conversor (string) {
    return (string.toString(base));
  }
  return (Conversor);
};
