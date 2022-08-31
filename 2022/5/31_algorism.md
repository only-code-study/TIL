# [셀프넘버](https://www.acmicpc.net/problem/4673)

## 문제 해석
문제를 보면 셀프 넘버라는 개념에 대해서 알아야해요.  
셀프 넘버는 생성자가 없는 숫자를 셀프 넘버라고 해요.  
예를 들어서 39(33 + 3 + 3)은 33이라는 생성자로 이루어져 있어, 39는 셀프넘버가 아니에요.

위와 같은 알고리즘을 보면, 항상 생성자는 생성된 숫자보다 작아요. 이를 이용해서 앞에서 부터 생성을 하고,
자신이 샐프넘버인지 검증을 하면서 문제를 풀 수 있을 꺼 같아요.

`do{}while()`부분에서는 숫자를 생성해 내는 과정, `if(nextNumber != number)`에서는 자신이 생성자일 수는 
없어서 넘기는 부분, 나머지는 `Array`의 `includes`와 `filter`을 이용하여 배열을 다시 정리하는 과정을
넣었어요.

## 솔루션
```javascript
let allNumber = []

const isSalfNumber = (number) => {
    let selfNumber = number;
    let tempNumber = number;

    do {
        selfNumber += tempNumber % 10
        tempNumber = Math.floor(tempNumber / 10)
    } while(tempNumber != 0)

    if (nextNumber != number) {
        allNumber.push(selfNumber);
    }

    if (allNumber.includes(number)) {
        allNumber = allNumber.filter( d => d != number);
        return false
    }
    return true;
}

for (let i = 1; i < 10000; i += 1) {
    if(isSalfNumber(i)) {
        console.log(i);
    }
}
```