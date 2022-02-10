# Rust
## 컬렉션
### 스트링
```rs
let mut s = String::new();
```
위처럼 String 형을 생성 할 수 있다.

```rs
let s = "initial contents".to_string();

let s = String::from("initial contents");
```
위 두 코드는 동일하다. 즉 스타일 문제라고 할 수 있다.

```rs
let mut s = String::from("foo");
s.push_str("bar");

let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(&s2);
println!("s2 is {}", s2);
```
위처럼 2가지 방식으로 할 수 있으며, push_str은 소유권을 안가져가서 맨 밑 구문이 정상적으로 실행됨을 알 수 있다.

```rs
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2;
```
위 코드중 s1은 소유권이 넘어간 상태이다. 그이유는 + 에서 찾을 수 있다. 

```rs
fn add(self, s: &str) -> String {}
```
+는 위 식을 실행 시키게 된다. 여기서 신기한 것은 String이 자동으로 str이 된다는 것이다. 이것은 역참느라는 기능때문인데, 나중에 배운다고 한다. 아무튼 이렇게 + 로 쓰게 되면 소유권을 가져가기도 하고, 여러개를 한번에 못한다.

```rs
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{}-{}-{}", s1, s2, s3);
```
하지만 다음과 format을 사용하면, s1, s2, s3의 소유권을 가져가지도 않고, 문제도 크게 생기지 않는다.

다른 것처럼 슬라이스가 될꺼 같지만, 쓰면 안되고, 또 안된다. 왜냐하면 UTF-8은 저장하는 방식이 다르기 때문이다.

**아무튼 쓰면 안된다.**

```rs
for c in "러스트".chars() {
    println!("{}", c);
}

for b in "러스트".bytes() {
    println1("{}", b);
}
```
그래도 그나마 위와 같이 스트링을 분해하여 다루는 방법은 유효하다.

### 해쉬
```rs
use std::collections::HasMap;

let mut scores = HashMap::new();
scroes.insert(String::from("Blue"), 10);
scroes.insert(STring::from("Yellow"), 50);

let teams = vec![String::from("Blue"), String::from("Yellow")];
let initial_scores = vec![10, 50];

let scores: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();
```
위와 같은 방식으로 생성하고 넣을 수 있다. 만약 집어 넣으면 소유권이 사라지게 된다. 예를 들면 teams와 initial_scores는 소유권이 없다.

```rs
use std::collections::HashMap;

let mut scores = HashMap::new();

socres.insert(String::from("Blue"), 10);
socres.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{}: {}", key, value);
}

let team_name = String::from("Blue");
let score = scores.get(&team_name);
```
위와같은 방식으로 출력이나 값을 받을 수 있다. score은 Option으로 넘어온다.

```rs
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
// 1
socres.insert(String::from("Blue"), 25);

println!("{:?}", scores);

// 2
scores.entry(String::from("Yellow")).or_insert(50);
scores.entry(String::from("Blue")).or_insert(50);

println!("{:?}", scores);

// 3
let text = "hellow world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```
값을 변경할 때 여러가지 상황으로 넣을 수 있다. 예를 들면,
1. 무조건 값을 변경하기
2. 값이 없는 경우에만 변경하기
3. 예전 값을 기초로 값을 갱신하기 
로 나누어서 할 수 있다.

## 에러처리
### panic! 
패닉 매크로는 복구가 불가능한(BOF 같은)오류가 날 때 사용이 된다!