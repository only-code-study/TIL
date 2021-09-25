# Rust
이 문서는 공식가이드를 보고 쓰는 문서입니다.

### match 추가적인 내용
match는 모든것을 표시해야 한다. 그래도 귀찮으니깐 하나로 퉁 치는 것도 있다.
```rs
let some_u8_value = 0u8;
match some_u8_value {
    1 => println!("one");
    3 => println!("three");
    5 => println!("five");
    7 => println!("seven");
    _ => (),
}
```
위에서 보면 _는 다른 모든것을 칭한다. 약간 default같은거 같다.
그리고 여러개가 아니라 한가지만 생각해보고 싶다면, if let도 좋은 선택지 인거 같다.
```rs
let some_u8_value = Some(0u8);
match some_u8_value {
    Some(3) => println!("three"),
    _ => (),
}

if let Some(3) = Some_u8_value {
    println!("three");
}

if mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("{:?}주의 25센트 동전!", state);
} else {
    count += 1;
}
```

# algorism

## KLIS
출처: [알고스팟](https://algospot.com/judge/problem/read/KLIS)

```cpp
#include <iostream>
#include <algorithm> 
#include <vector>

using namespace std;

int n;
int cacheLen[501], cacheCnt[501], S[500];

const int MAX = 20000000 + 1;

int lis(int start) {
	int& ret = cacheLen[start + 1];
	if(ret != -1) return ret;
	
	ret = 1;
	for(int next = start + 1; next < n; ++next)
		if(start == -1 || S[start] < S[next])
			ret = max(ret, lis(next + 1));
	return ret;
}

int count(int start) {
	if(lis(start) == 1) return 1;
	int& ret = cacheCnt[start + 1];
	if(ret != -1) return ret;
	ret = 0;
	for(int next = start + 1; next < n; ++next) {
		if((start == -1 || S[start] < S[next]) && lis(start) == lis(next) + 1)
			ret = min<long long>(MAX, (long long)ret + count(next));
	}
	return ret;
}

int cache[501];

int lis3(int start) {
    int& ret = cache[start+1];
    if(ret != -1) return ret;
    ret = 1;
    for(int next = start+1; next < n; ++next)
        if(start == -1 || S[start] < S[next])
            ret = max(ret, lis3(next) + 1);
    return ret;
}

void reconstruct (int start, int skip, vector<int>& lis) {
    if(start != -1) lis.push_back(S[start]);

    vector<pair<int, int> > followers;
    for(int next = start + 1; next < n; ++next)
        if((start == 1 || S[start] < S[next]) && lis3(start) == lis3(next) + 1)
            followers.push_back(make_pair(S[next], next));
    sort(followers.begin(), followers.end());

    for(int i = 0; i < followers.size(); ++i) {
        int idx = followers[i].second;
        int cnt = count(idx);
        if(cnt <= skip)
            skip -= cnt;
        else {
            reconstruct(idx, skip, lis);
            break;
        }
    }
}

int main()
{
	int C, n, k;
	cin >> C;
	for(int i = 0; i < C; i++) {
		cin >> n >> k;
		for (int j = 0; j < n; j++) {
			cin >> S[j];
		} 
		cout << reconstruct(0, k, cache) << endl;
	} 
}

```