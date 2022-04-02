# Rust
## strut(구조체)다루기
### 1. 구조체를 정의하고 초기화하기
```rs
strut User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}
```
위처럼 User을 struct로 정의할 수 있다.

```rs
let user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
};
```
위처럼 정의한 struct를 객체로 생성 할 수 있다. 당연하게도 내부의 값을 바꿀려면 mut를 써야한다.

```rs
fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}
```
위처럼 변수 이름이 같다면 줄일 수 있다.

```rs
let user2 = User {
    email: String::from("another@example.com"),
    username: String::from("anothorusername567"),
    ..user1
};
```
위처럼 나머지 값을 user1처럼 가지고 올때 `..user1`을 쓴다.

```rs
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

let black = Color(0, 0, 0);
let origin = Point(0, 0, 0);
```
위처럼 이름 없는 struct를 쓸 수 있다.

### 구조체를 이용한 예제 프로그램
```rs
	fn main() {
    let length1 = 50;
    let width1 = 30;
	//let rect1 = (50, 30);

    println!(
        "The area of the rectangle is {} square pixels.",
        area(length1, width1) // or area(rect1)
    );
}

fn area(length: u32, width: u32) -> u32 {
    length * width
}

fn area(dimensions: (u32, u32)) -> u32 {
	dimensions.0 * dimensions.1
} 
```
위와 같이 보면 묶어서 쓸 수도 있다.
