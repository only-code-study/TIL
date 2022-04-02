# Rust
## 열거형과 패턴 매칭
### match 흐름 제어 연산자
metch는 분기별로 나눈 것을 한번에 보여주는 연산자이다.
```rs
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u32 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        },
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```
다음과 같이 표현이 되며, Coin::Penny 처럼 안에 식을 쓸 수 도 있다.

웃긴건 enum에 enum을 사용 할 수 있다는 것이다.
```rs
#[derive(Debug)]
enum UsState {
    Albama,
    Alska,
    // ... etc
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```
위와 같이 UsState라는 enum을 만든 후에 Coin에서 Quarter에 괄호로 추가되어 있는 형태이다.

```rs
fn value_in_cents(coin: Coin) -> u32 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quater(state) => {
            println!("State quarter from {:?}!", state);
            25
        },
    }
}
위처럼 안에 state를 인자로 받아서 사용 할 수 있다. 즉 잘쓰면 무궁무진하게 활용 할 수 있다는 이야기 이다.

재미있게도 enum과 같은 성격을 가지고 있는 Option<T>에서도 자주 쓰이게 된다.
```rs
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None =? None,
        Some(i) => Some(i + 1),
    }
}
```
재미 있는 점은 위 중 하나라도 빠지게 되면 컴파일러 단에서 오류를 내뿜게 된다. 그래서 퉁 치는 것 중 하나는 `_`이다. 모든 것들을 대충 이걸로 하겠다 이것이다.

### if let을 사용한 간결한 흐름 제어
위 match문법도 정말 좋은 문법이지만, 써야하는 가지수가 한가지라면 훨신 간단하게 쓰일 수 있다.
```rs
match some_u8_value {
    Some(3) => println!("three"),
    _ => (),
}

if let Some(3) = some_u8_value {
    println!("three");
} else {}
```
위처럼 너무 길다면 if let으로 쓰고, _ 대신 else를 쓰일 수 있다는 것을 생각하면 좋다.

## 모듈 
### mod와 파일 시스템
파일을 쓸때 mod로서 나눌 수 있다.
```rs
mod network {
    fn connect() {}
}

mod client {
    fn content() {}
}
```
물론 위 뿐만 아니라 안쪽으로 넣어서 사용 가능하기도 한다.
```rs
mod client {
    connect() {}
}

mod network {
    fn connect() {}

    mod server {
        fn connect() {}
    }
}
```
위처럼 중첩해서 사용이 가능하다. 또한 다른쪽으로 옮기는 것도 가능하다.

```rs
// lib.rs
mod client;
mod network;
```
위 처럼 만들고, 안에 `client.rs`파일과 `network/mod.rs`그리고 `network/server.rs`파일을 생성하여 옮기면 된다.

### pub으로 가시성 제어하기
rust는 기본적으로 private상태이다. 즉 위 상태를 다른 사람이 쓰게 만들기 위해서는 다음과 같이 pub라는 문구를 붙여 줘야 한다.
```rs
// lib.rs
pub mod client;
mod network;

//client.rs
pub fn connect() {}
```