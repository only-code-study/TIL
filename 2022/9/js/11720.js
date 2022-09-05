const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let count = input[0];
let numString = input[1].toString();
let sum = 0;
for (let i = 0; i < count; i++) {
  sum += parseInt(numString[i]);
}

console.log(sum);
