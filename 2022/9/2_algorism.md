# [아스키 코드](https://www.acmicpc.net/problem/11654)

ASCII는 영어와 특수문자 등을 표현하기 위한 코드이다.  
대부분의 언어는 변환을 지원하고 있으며, javascript또한 String의 프로토타입으로 `charCodeAt(index: number)`의 함수로 지원하고 있다.

```js
let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");
// let input = fs.readFileSync("ex.txt").toString().split(" ");

console.log(input[0].charCodeAt(0));
```
