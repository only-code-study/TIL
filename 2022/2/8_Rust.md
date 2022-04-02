# Rust
## 컬렉션
### 벡터
```rs
let v: Vec<i32> = Vec::new();

let v = vec![1, 2, 3];

let mut v = Vec::new();
v.push(5);
v.push(6);
v.push(7);
v.push(8);
v.push(9);
```
위처럼 초기화를 할 수 있다.

```rs
let v = vec![1, 2, 3, 4, 5];

let third: &i32 = &v[2];
let third: Option<&i32> = v.get(2);
```
위처럼 접근 할 수 있고, 만약에 잘못 접근하면, None이 뜬다.
```rs
let mut v = vec![1, 2, 3, 4, 5];

let first = &v[0];

v.push(6);
```
위는 안되는 것인데 그이유는 잘 모르겠다.

```rs
let v = vec![100, 32, 57];
for i in &v {
    println!("{}", i);
}

let mut v = vec![100, 32, 57];
for i in &mut v {
    *i += 50;
}
```

위처럼 순환처리 할 수 있다.

```rs
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec! [
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```
