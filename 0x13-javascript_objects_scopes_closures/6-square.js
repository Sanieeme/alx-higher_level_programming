#!/usr/bin/node
const s = require('./5-square')

class Square extends s {
	charPrint (c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			let j = '';
			for (let k = 0; k < this.width; k++) {
				j += c;
			}
			console.log(j);
		}
	}
}

module.exports = Square;
