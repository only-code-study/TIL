# [문자열 반복](acmicpc.net/problem/2675)

이번 문제도 마찬가지로 분할과 반복으로만 풀 수 있는 문제입니다.  
저번에 배웠던 형식인 `Array.from({length: 개수})`를 통해 결과값을 만들어 출력했어요.

```js
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

for (let i = 1; i <= parseInt(input[0]); i++) {
  let [count, value] = input[i].split(" ");
  let result = "";
  for (let v of value.split("")) {
    result += Array.from({ length: count })
      .map(() => v)
      .join("");
  }
  console.log(result);
}
```
