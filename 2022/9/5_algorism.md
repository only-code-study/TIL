# [숫자의 합](https://www.acmicpc.net/problem/11720)

TIL이 의미가 없을 정도의 문제 수준인 것 같다.  
두번째 인자의 숫자를 string으로 받은 다음 각각 한개씩 꺼낸 다음 int로 치환하여 더하는 간단한 문제이다.

```js
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let count = input[0];
let numString = input[1].toString();
let sum = 0;
for (let i = 0; i < count; i++) {
  sum += parseInt(numString[i]);
}

console.log(sum);

```