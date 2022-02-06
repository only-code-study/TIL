# SpringBoot

## SpringData JPA
### @Query 어노테이션
JPQL(Java Persistence Query Language)로 작성하는 '객체지향 쿼리'이다.
다음 작업을 시행 할 수 있다.
* 필요한 데이터만 선별적으로 추출하는 기능
* 데이터베이스에 맞는 순수한 SQL을 사용하는 기능
* insert, update, delete와 같은 select가 아닌 DML 등을 처리하는 기능(@Modifying과 함꼐 사용)

#### 파라미터 바인딩
파라미터들은 다음과 같이 쓸 수 있다.
* '?1, ?2'와 1부터 시작하는 파라미터의 순서를 이용하는 방식
* ':xxx'와 같이 ':파라미터 이름'을 활용하는 방식
* '#[ ]'과 같이 자바 빈 스타일을 이용하는 방식

그리고 Native SQL처리를 할 수도 있다.
```java
@Query(value = "select * from memo where mno > 0 ", nativeQuery = true)
List<Object[]> getNativeResult();
```

# Rust
## Struct
### 메소드 문법
메소드는 fn으로 쓰게 되는데, 첫번째 파라미터는 여타 다른 언어와 마찬가지로 selfd이다.
공식 문서를 조금 빌리자면
```rs
#[derive(Debug)]
struct Rectangle {
    length: u32,
    width: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.length * self.width
    }
}

fn main() {
    let rect1 = Recangle { length: 50, width: 30 };

    println! (
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
}
```
여기서 `area`를 보자면, `&self`로 시작한다. 여기서 이 것을 소유권을 가져가거나, 변경 불가능하게 빌리거나, 변경이 가능하도록 빌려울 수도 있다.

그리고 여타 다른 언어처럼 뒤에 더 추가하고 싶다면, 추가하면 인자로 받아 올 수 있다.

또한 self가 없더라도 충분히 계속해서 사용 할 수 있다.

## 열거형과 패턴 매칭
### 열겨형
열거형은 한개만 존재야하 할 때 쓰는 것이다.

근데 이 열거형은 다른 struct여러개를 가지고 올 수 있다.

이 기술을 이용하여 옵셔널이라는 것을 쓸 수 있다. rust는 nil(null)을 안쓰고 Option을 넣어서 null pointer에러에 대해서 대응한다.

그리고 오류 또는 none상태일 때에 다루는 편리한 것이 많다. (예를 들면 앞으로 소개할 match 구문 같은거?)