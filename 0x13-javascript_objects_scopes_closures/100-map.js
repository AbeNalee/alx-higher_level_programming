#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
function printList(l) {
	console.log(l);
	console.log(l.map((item, index) => item * index));
}
printList(list);
