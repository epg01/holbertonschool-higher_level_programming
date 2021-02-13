#!/usr/bin/node
function Recursive (number) {
    if (!number || isNaN(number)) {
	return (1);
    } else {
	return (number * Recursive(number - 1));
    }
}

if (isFinite(process.argv[2]) && (Number(process.argv[2]) < 0)) {
    return ;
} else if (isFinite(process.argv[2]) && (Number(process.argv[2]) === Number(0))) {
    console.log(1);
    return ;
}
console.log(Recursive(process.argv[2]));
