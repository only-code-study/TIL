const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().toUpperCase();

let charCount = Array.from({ length: 26 }, () => 0);

for (let i of input) {
  charCount[i.charCodeAt(0) - "A".charCodeAt(0)] += 1;
}

function solve(arr) {
  let maxCount = Math.max(...arr);
  let maxIndex = arr
    .map((d, i) => {
      if (d == maxCount) return i;
    })
    .filter((d) => d !== undefined);
  if (maxIndex.length > 1) return "?";
  return String.fromCharCode("A".charCodeAt(0) + maxIndex[0]);
}

console.log(solve(charCount));
