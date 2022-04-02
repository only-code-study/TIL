# Rust
## 제네릭타입
### 트레잇
다른 언어에서는 인터페이스라고 불리는 것이다. 즉 강제로 동일한 것을 만드는 것이다

```rs
pub trait Summarizable {
    fn summary(&self) -> String;
}

pub struct NewsArticle {
    pub headline: Stirng,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Smmarizable for NewsArticle {
    fn summary(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summarizable for Tweet {
    fn summary(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```
위와 같이 구현이 되었다면 다음과 같이 쓸 수 있다.

```rs
let tweet = Tweet {
    username: String::from("hourse_ebooks"),
    content: String::from("of course, as you probably already know, people"),
    reply: false,
    retweet: false,
};

println!("1 new tweet:{}", tweet.summary());
```
그리고 다음과 같이 외부에서 끓어다쓸 수 있다.

```rs
extern crate aggregator;

use aggregator::Summarizable;

struct WeatherForecast{
    high_temp: f64,
    low_temp: f64,
    change_of_precipitation: f64,
}

impl Summarizable for WeatherForecast{
    fnsummary(&self) -> String {
        format!("The high will be {}, and the low will be {}. The chance of precipitation is {}%.",self.hight_temp, self.low_temp, self.chance_of_precipitation)
    }
}
``
위에서 아래로 내려오는 것은 괜찮지만, 외부에 있는 트레잇을 바꾸어서 외부로 적용하는 것은 혀용하지 않는다. 이는 부모 타입이 존재하지 않기 때문에 고아 규칙이라고 불린다.

```rs
pub trait Summarizable {
    fn author_summary(&self) -> String;

    fn summary(&self) -> String {
        format!("(Read more from {}...)", self.author_summary())
    }
}
```
위와 같이 쓰면 Summarizable을 구현할때, author_summary만 써도 된다.

```rs
pub fn nofity<T: Summarizable>(item: T) {
    piintln!("Breaking news! {}", item.summary());
}

fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 {}

fn some_function<T, U>(t: T, u: U) -> i32 where T: Display + Clone, U: Clone + Debug{}
```
위와 같은 방법으로 트레잇을 걸 수 있다.

### 라이프타임
```rs
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {}", result);
}

fn longest(x: &str, y: &str) -> &str {
    if .len() > y.len() {
        x
    } else {
        y
    }
}
```
위와 같이 쓴다면 작동이 될것 같지만, return이 되는 값이 무엇인지 모르기 때문에 어느것이 더 라이프타임이 긴지 몰르기 때문에 오류가 난다.

그래서 동일한 라이프타임을 가지고 있다고 표현을 하는데 보통 `'a`라고 표현을 많이 한다.

```rs
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```
그래서 위와 같이 고치면 x, y와 return이 모두 생명주기가 같은 값들이 와야한다는 것이 포함이 되도록 컴파일이 된다.

```rs
fn main() {
    let string1 = String::from("long string is long");
    let result;
    {
        let string2 = String::from("xyz");
        result = longest(string1.as_str(), string2.as_str());
    }
    println!("The longest string is {}", result);
}
```
그러나 위와 같은 식은 돌아가지 않는다. 왜냐하면 result는 string2의 생명주기를 받았기 때문에 밖에서 쓰일 수 없다.

현재 rust는 버전업에 따라서 lifetime을 생략할 수 있도록 했는데 3가지 규칙을 따른다.
* 참조자인 각각의 파라미터는 고유한 라이프 타임 파라미터를 갖는다.
* 딱 하나의 라이프타임 파라미터만 있다면, 그 라이프타임이 모든 출력 라이프타임 파라미터들에 대입된다.
* 여러 개의 입력 라이프타임 파라미터가 있는데, 메소드라서 그 중 하나가 &self 또는 &mut self라고 한다면, self의 라이프타임이 모든 출력 라이프타임 파라미터에 대입된다.

그리고 여기서 재미있는 것은 static이다. 생명주기 중에 전체를 나타낸 것으로 `'static`을 쓸 수 있다.

## 테스팅
### 테스트문법 작성하기
* 필요한 데이터 혹은 상태를 설정하기
* 우리가 테스트하고 싶은 코드 실행하기
* 그 결과가 예상대로인지 단언하기(assert)

```rs
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
```
`cargo new adder --lib`로 생성하면 위와 같은 코드가 생긴다. 그 이후 `cargo test`를 하면 테스트를 싱행한다.

예시로 코드를 써보자면
```rs
#[derive(Debug)]
pub struct Rectangle {
    length: u32,
    width: u32,
}

impl Rectangle {
    pub fn can_hold(&self, other: &Rectangle) -> bool {
        self.length > other.length && self.width > other.width
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle { length: 8, width: 7};
        let smaller = Rectangle { length: 5, width: 1 };

        assert!(larger.can_hold(&smaller));
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle { length: 8, width: 7 };
        let smaller = Rectangle { length: 5, width: 1 };

        assert!(!smaller.can_hold(&larger));
    }
}
```
저렇게 코드를 하나씩 짜서 테스트를 해봐야 한다.

==, != 로도 짜도 되지만, assert_eq!, assert_ne!로도 짜도 된다.

```rs
#[test]
fn greeting_contains_name() {
    let result = greeting("Carol");
    assert!(
        result.contains("Carol"),
        "Greeting did not contain name, value was `{}`", result
    );
}
```
위처럼 test를 할때 좀 더 정보를 주고 싶다면 저렇게 하면 된다.

```rs
impl Guess {
    pub fn new(value: u32) -> Guess {
        if value < 1 {
            panic!("Guess value must be greater than or equal to 1, got {}.", value);
        } else if value > 100 {
            panic!("Guess value must be less than or equal to 100, got {}.", value);
        }

        Guess {
            value
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic(expected = "Guess value must be less than or equal to 100")]
    fn greater_than_100() {
        Guess::new(200);
    }
}
```
위처럼 `should_panic`을 쓰면 오류가 나더라도 패스가 되고, expected안에 있는 말을 출력한다.

### 테스트의 실행 방식 제어
테스트는 빠르게 끝내야하기 때문에 멀티 스레딩 방식으로 한다. 이는 thread에 안전하지 않는데 만일 한개의 thread로 하고 싶다면, `cargo test -- --test-threads=1`로 하면 된다.

성공한 부분만 나오게 해야하는데 캡쳐때문에 문제가 된다면, `--nocapture`을 하면 된다.

한가지만 실행한다면 `cargo test 함수 이름`으로 하면 된다. 또한 필터링도 된다.

기본적으로 `#[ignore]`을 하면 실행이 안되다가 `cargo test -- --ignored`로 실행하면 위 어노테이션이 들어간 것이 실행 된다.
