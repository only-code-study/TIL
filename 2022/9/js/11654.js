let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
// let input = fs.readFileSync("ex.txt").toString().split(" ");

console.log(input[0].charCodeAt(0));
