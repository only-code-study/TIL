# 타일링
출처: [알고스팟](https://algospot.com/judge/problem/read/TILING2)

## 문제
2xn 크기의 사각형을 2x1 크기의 사각형으로 빈틈없이 채우는 경우의 수를 구하는 프로그램을 작성하세요.

예를 들어 n=5라고 하면 다음 그림과 같이 여덟 가지의 방법이 있습니다.

경우의 수는 n이 커지면 아주 커질 수 있으므로, 1000000007으로 나눈 값을 대신 출력하세요.

## 입력
입력의 첫 줄에는 테스트 케이스의 수(C <= 50)가 주어집니다. 그후 C줄에 각각 1개의 자연수로 n(1 <= n <= 100)이 주어집니다.

## 출력
각 테스트 케이스마다 한 줄에 경우의 수를 1000000007로 나눈 나머지를 출력합니다.

## 예제 입력
```
3
1
5
100
```
## 예제 출력
```
1
8
782204094
```

## 풀이
```python
MOD = 1000000007
cache = [-1] * 101

def tiling(width):
    if width <= 1: return 1
    ret = cache[width]
    if ret != -1: return ret
    ret = cache[width] = (tiling(width-2) + tiling(width - 1)) % MOD
    return ret

N = int(input())
for i in range(N):
    print(tiling(int(input())))
```
