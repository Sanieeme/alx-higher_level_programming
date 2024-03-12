#!/usr/bin/node
function computeFactorial(num) {
	if (isNaN(num)) {
		return 1;
	} else if (num === 0 || num === 1) {
		return 1;
	} else {
		return num * computeFactorial(num - 1);
	}
}
const input = parseInt(process.argv[2]);
console.log(computeFactorial(input));
