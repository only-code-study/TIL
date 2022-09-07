const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();

let result = Array.from({ length: 26 }, (i) => -1);
for (let i = 0; i < input.length; i++) {
  let charIndex = input.charCodeAt(i) - "a".charCodeAt(0);
  if (result[charIndex] === -1) result[charIndex] = i;
}
console.log(result.join(" "));
