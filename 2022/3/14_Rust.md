# Rust
## 함수형 언어
### 클로저
#### 클로저 타입 추론과 어노테이션

다음과 같이 클로져를 쓸 수 있다.
```rs
let expensive_closuer = |num:u32| -> u32 {
    println!("calculating slowly...");
    thread::sleep(Duration::from_secs(2));
    num
};
```

재미있는 것은 클로저는 다양한 형태로 쓰일 수 있다.(swift에서 따와서 그런가)

```rs
fn add_one_v1 (x: u32) -> u32 { x + 1 }
let add_one_v2 = |x: u32| -> u32 { x + 1 };
let add_one_v3 = |x| { x + 1 };
let add_one_v4 = |x| x + 1;
```