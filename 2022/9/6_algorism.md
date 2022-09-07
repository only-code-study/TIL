# [알파벳 찾기](https://www.acmicpc.net/problem/10809)

알파벳찾기중 흥미로운 내용은 Array.from을 통해서 원하는 배열의 개수를 만들 수 있고, 초기화도 쉽게 할 수 있다는 점이었어요.

```js
const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString();

let result = Array.from({ length: 26 }, (i) => -1);
for (let i = 0; i < input.length; i++) {
  let charIndex = input.charCodeAt(i) - "a".charCodeAt(0);
  if (result[charIndex] === -1) result[charIndex] = i;
}
console.log(result.join(" "));
```