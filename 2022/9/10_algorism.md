# [단어공부](https://www.acmicpc.net/problem/1157)

이번 문제는 `Array`의 `prototype`을 써보았어요.  
`prototype`을 아직도 초보적으로 사용하여 기초적인 `map`과 `filter`을 이용했어요.  
`reduce`를 이용했다면, 좀 간단하게 표현 할 수 있었지 않나 생각이 되네요.  
javascript에는 `char`을 다루는 기술이 좀 더 있었으면 좋겠네요.  

```js
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
```