#!/usr/bin/node


exports.converter = function (base) {
    function Conversor(string) {
	return (parseInt(String(string), base));
    }
    return (Conversor);
};
