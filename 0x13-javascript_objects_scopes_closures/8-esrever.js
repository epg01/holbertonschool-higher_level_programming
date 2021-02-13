#!/usr/bin/node
exports.esrever = function (list) {
  let LengthList = list.length - 1;
  const CopyList = Array.from(list);

  for (let i = 0; i < list.length; i++, LengthList--) {
    list[i] = CopyList[LengthList];
  }
  return (list);
};
