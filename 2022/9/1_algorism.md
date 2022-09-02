# [한수](https://www.acmicpc.net/problem/1065)

이번에는 한술라는 수의 개수를 세는 프그램이에요.  
나누었을 때 등차수열대로 올라가는지 확인하면 되요.  
이를 쉽게 확인 할 수 있는 방법은 아래와 같이 모든 수를 비교하는 것이에요.

하지만 이를 좀 더 생각해 보면 더 간단하고 쉽게 다를 수 있는 방법이 생겨요.  
예를 들어 2자리를 보죠. 2자리는 12, 13, 14등 모든 수가 한수에요.  
넘어가서  3자리를 보면 여기서부터 한수를 찾기에는 어려워요.

1\*\*으로 시작하는 수를 보면, 111, 123, 135, 147, 159 이렇게 5개가 있어요.  
또한 2\*\*으로 시작하는 수를 보면, 222, 234, 246, 258 이렇게 4개가 있네요.  
간단히 보면, +0, +1, +2, +3, +4, +5같이 올라가는 수를 발견하되, 10이 넘어가는 순간 안되는 것만 고르면 된요.

이 방법이 훨신 비교연산을 하기 쉬울 꺼라고 생각하지만, 한수는 비교를 9자리수까지만 하면 되고, 문제에서도 1000개 이하를 불렀기 때문에, 우리는 여기까지만 생각하도록 하고, 쉬운 방법으로 코딩하죠.

```js
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

let result = 0;
for (let i = 1; i <= input[0]; i += 1) {
    let splitedNum = i.toString().split('')
    let prev = -1;
    let gap = 10;
    let re = true;
    for (let a = 0; a < splitedNum.length; a += 1) {
        if (prev == -1) {
            prev = parseInt(splitedNum[a]);
            continue;
        }
        if (gap == 10) {
            gap = prev - parseInt(splitedNum[a]);
            prev = parseInt(splitedNum[a]);
            continue;
        }
        if (gap != prev - parseInt(splitedNum[a])) {
            re = false;
            break;
        }
        prev = parseInt(splitedNum[a]);
    }
    if (re) {
        result += 1;
    }
}

console.log(result)

```
