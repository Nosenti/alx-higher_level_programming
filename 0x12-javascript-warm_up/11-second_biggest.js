#!/usr/bin/node
const numArgs = process.argv.length;
if (numArgs == 2 || numArgs == 3) {
	console.log(0);
}else {
	const argsArr = process.argv.slice(2);
	const sorted = argsArr.sort((a, b) => a - b);
	console.log(sorted[sorted.length - 2]);
}

