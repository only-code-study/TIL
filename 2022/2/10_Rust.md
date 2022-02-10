# Rust
## 에러처리
### Result
```rs
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```
Result는 복구가 가능하고, 2가지의 값으로 구성되어 있다.

```rs
use std::fs::File;

fn main() {
    let f = File::open("hello,txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => {
            panic!("There was a problem opening the file: {:?}", error)
        },
    };
}
```
위와 같이 Result타입은 Err로 처리 가능하다.

```rs
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hellow.txt.");

    let f = match f {
        Ok(file) => file,
        Err(ref error) if erro.kind() == ErrorKind::NotFount => {
            match File::create("hellow.txt") {
                Ok(fc) => fc,
                Err(e) => {
                    panic!(
                        "Tried to create file but there was a problem: {:?}",
                        e
                    )
                },
            }
        },
        Err(error) => {
            panic!(
                "There was a problem opening the file: {:?}",
                error
            )
        },
    };
}
```
재미있는 것은 try catch처럼 여러개 찾아서 쓸 수 있다는 것이다.

```rs
use std::fs::File;

fn main() {
    let f = File::open("hello.txt").unwrap();
    let f = File::open("hello.txt").expect("Failed to open hellow.txt");
}
```
위처럼 match가 길기때문에 숏컷을 지원해준다.

```rs
use std::io;
use std::io::Read;
use std::fs::File;

fn read_username_from_file() -> Result<String, io::Error> {
    let f = File::open("hello.txt");

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}
```
Result을 이용하여, 에러를 전파 할 수 도 있다.

```rs
use std::io;
use std::io::Read;
use std::fs::File;

fn read_username_from_file() -> Result<String, to::Error> {
    let mut f = File::open("hellow.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}

fn read_username_from_file() -> Result<String, io::Error> {
    let mut s = String::new();

    File::open("hello.txt")?.read_to_string(&mut s)?;

    Ok(s)
}
```
위처럼 ?을 이용하여 숏컷을 사용해서 코드를 많이 줄일 수 있다. 하지만 ?는 Result를 반환하는 함수에서만 사용이 가능하다.

### panic! vs Result선택법
테스트코드들은 전부 panic!을 해도 되고, result를 해도 된다. 하지만, 모른다면 Result를 호출하자. 만약 이 코드가 절대 오류가 나지 않은 경우에는 .unwrap()으로 마무리 하자.

## 제네릭타입, 트레잇, 라이프타임
### 제네릭 데이터 타입
제레릭은 다른 언어과는 다르게 무언가를 보장해줘야 할 수 있다. 할 수 있는 것을 보장 해줘야 한다.
```rs
struct Point<T, U> {
    x: T,
    y: U,
}

impl<T, U> Point<T, U> {
    fn mixup<V, W>(self, other: Point<V, W>) -> Point<T, W> {
        Point {
            x: self.x,
            y: other. y,
        }
    }
}

fn main() {
    let p1 = Point { x: 5, y: 10.4};
    let p2 = Point { x: "Hello", y: 'c'};

    let p3 = p1.mixup(p2);

    println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
```