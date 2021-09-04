# 모스 부호 사전
출처: [알고스팟](https://algospot.com/judge/problem/read/MORSE)
## 문제
모스 부호(Morse code)는 전화가 없던 시절 무선 전신에 주로 사용하던 코드로, 짧은 신호(단점, o)와 긴 신호(장점, -)를 섞어 글자를 표현하는 표현방식입니다. 예를 들어 알파벳 J는 모스 부호 o---로 표현되고, M은 --로 표현됩니다.

n개의 장점과 m개의 단점으로 구성된 모든 신호들을 담고 있는 사전이 있다고 합시다. 예를 들어 n = m = 2라면 다음과 같은 신호들이 포함되어 있는 것이죠.
```
--oo
-o-o
-oo-
o--o
o-o-
oo--
```
이 신호들은 사전순서대로 정렬되어 있습니다. -의 아스키 코드는 45이고, o의 아스키 코드는 111이기 때문에 -가 먼저 오게 되죠. n과 m이 주어질 때 이 사전의 k번째 신호를 출력하는 프로그램을 작성해 봅시다. 예를 들어 위 사전에서 네 번째 신호는 o--o입니다.

## 입력
입력의 첫 줄에는 테스트 케이스의 수 C(≤50)가 주어집니다. 각 테스트 케이스는 세 개의 정수 n, m(1≤n, m≤100), k(1≤k≤1,000,000,000)로 주어집니다. 사전에는 항상 k개 이상의 신호가 있다고 가정해도 좋습니다.

## 출력
각 테스트 케이스마다 한 줄에 해당 신호를 출력합니다.

## 예제 입력
```
3
2 2 4
4 8 13
6 4 1
```
## 예제 출력
```
o--o
--o-ooo-oooo
------oooo
```

## 풀이
```python
C = int(input())

M = 10000000000 + 100
bino = [[-1] * 201 for _ in range(201)]
for i in range(200):
    bino[i][0] = bino[i][i] = 1
    for j in range(1, i):
        bino[i][j] = min(M, bino[i-1][j-1] + bino[i-1][j])

def solve(n, m, k):
    if n == 0: return m * 'o'
    if k <= bino[n+m-1][n-1]:
        return '-' + solve(n - 1, m, k)
    return 'o' + solve(n, m - 1, k - bino[n+m-1][n-1])
    
print()
for i in range(C):
    n, m, k = map(int, input().split())
    print(solve(n, m, k))
```