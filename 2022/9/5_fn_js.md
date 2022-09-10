# 함수형 자바스크립트 프로그래밍

안녕하세요! [함수형 자바프로그래밍](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788966262120) 책을 오늘부터 조금씩이라도 읽어보려고 해요.

## 함수형 프로그래밍(FP; functional programming)

대표적인 함수형 자바스크립트 라이브러리인 Underscore.js의 `each`, `map`, `filter`, `reduce`등을 보았을 때 `for`을 대체한 것이라는 생각이 들어요.

좀 더 깊게 보면 다음과 같이 함수 안에 함수를 리턴하는 기법인 커링이라는 기술을 볼 수 있어요.

```js
function outer(a) {
  return function inner(b) {
    return a + b;
  }
}
outer(1)(2); // 3

const inner3 = outer(3);
inner3(1); // 4
inner4(1); // 5
```

FP을 다른 관점에서 보면 '항상 동일하게 동작하는 함수'를 통해 살을 붙여가며 만드는 식이라고 보면 좋을꺼 같아요. OOP관점과 다른 점으로 살펴보자면, 객체를 class관점으로 볼지, function관점으로 볼지의 차이점으로 보는 것이 가장 큰 차이점 중 하나라고 볼 수 있네요.

함수형 프로그래밍의 묘미는 함수들을 이리저리 조합해서 원하는 동작을 구현하는 거에요.  