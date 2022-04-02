# Rust
## 구조체
### 구조체를 이용한 예제 프로그램
```rs
struct Rectanle {
    length: u32,
    width: u32,
}

fn main() {
    let rect1 = Rectangle { length: 50, width: 30 };

    println!("rect1 is {}", rect1);
}
```
위 코드는 에러가 나오는데 rect1이 Display를 구현하지 않아서 오류가 난다. 그래서 `println!(:?)`로 하면 될꺼 같은데 Debug정보를 봐야 하는 것이라서 위에 Debug를 켜줘야 한다.

```rs
#[derive(Debug)]
struct Rectangle {
    length: u32,
    width: u32,
}

fn main() {
    let rect1 = Rectangle { length: 50, width: 30};
    println!("rect1 is {:?}", rect1);
}
```
위를 실행하면 `rect1 is Rectangle { length: 50, width: 30 }`으로 된다.

여기서 조금더 이쁘게 보고 싶다면 `println!{:#?}`를 해야한다.

### 메소드 문법
