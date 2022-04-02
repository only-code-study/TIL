# Rust
## I/O 프로젝트: 커맨드 라인 프로그램 만들기
### 커멘드라인 인자 허용하기
커멘드라인 인자를 허용하기 위해서는 `std::env::args`라는 라이브러리를 가지고 와야한다.

```rs
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("{:?}", args);
```
위의 코드를 실행하면 뒤에 인자들이 vec형태로 들어오게 된다.

```
$ cargo run
["target/debug/greprs"]

$ cargo run needle haystack
...snip...
["target/debug/greprs", "needle", "haystack"]
```

이제 vec으로 들어온다는 것을 확인 했으므로 다음과 같이 따로 빼서 저장할 수 있다.
```rs
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let qeury = &args[1];
    let filename = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", filename);
}
```

## 함수형 언어 특성
### 클로저
만약에 다음과 같은 함수가 있다고 가정을 해보자(`simulated_expensive_calculation(intensity)`는 시간이 많이 걸린다)
```rs
fn generate_workout(intensity: u32, random_number: u32) {
    if intensity < 25 {
        println!(
            "Today, do {} pushups!",
            simulated_expensive_calculation(intensity)
        );
        println!(
            "Next, do {} situps!",
            simulated_expensive_calculation(intensity)
        );
    } else {
        if random_number == 3 {
            println!("Take a break today! Remember to stay hydrated!");
        } else {
            println!(
                "Today, run for {} minutes!",
                simulated_expensive_calculation(intensty)
            );
        }
    }
}
```

위의 코드를 `simulated_expensive_calculation(intensity)`를 하나의 변수로 모으고 클로저를 사용하면 쓸 때만 하게 한다면 효율적인 연산 코드가 된다(lazy 한 계산)
```rs
let expensive_closuer = |num| {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
} 
```