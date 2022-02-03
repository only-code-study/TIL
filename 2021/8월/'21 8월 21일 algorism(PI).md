# 원주율 외우기
출처: [알고스팟](https://algospot.com/judge/problem/read/PI)

## 문제
(주의: 이 문제는 TopCoder 의 번역 문제입니다.)

가끔 TV 에 보면 원주율을 몇만 자리까지 줄줄 외우는 신동들이 등장하곤 합니다. 이들이 이 수를 외우기 위해 사용하는 방법 중 하나로, 숫자를 몇 자리 이상 끊어 외우는 것이 있습니다. 이들은 숫자를 세 자리에서 다섯 자리까지로 끊어서 외우는데, 가능하면 55555 나 123 같이 외우기 쉬운 조각들이 많이 등장하는 방법을 택하곤 합니다.

이 때, 각 조각들의 난이도는 다음과 같이 정해집니다:

모든 숫자가 같을 때 (예: 333, 5555) 난이도: 1
숫자가 1씩 단조 증가하거나 단조 감소할 때 (예: 23456, 3210) 난이도: 2
두 개의 숫자가 번갈아 가며 출현할 때 (예: 323, 54545) 난이도: 4
숫자가 등차 수열을 이룰 때 (예: 147, 8642) 난이도: 5
그 외의 경우 난이도: 10
원주율의 일부가 입력으로 주어질 때, 난이도의 합을 최소화하도록 숫자들을 3자리에서 5자리까지 끊어 읽고 싶습니다. 최소의 난이도를 계산하는 프로그램을 작성하세요.

## 입력
입력의 첫 줄에는 테스트 케이스의 수 C (<= 50) 가 주어집니다. 각 테스트 케이스는 8글자 이상 10000글자 이하의 숫자로 주어집니다.

## 출력
각 테스트 케이스마다 한 줄에 최소의 난이도를 출력합니다.

## 예제 입력
```
5 
12341234 
11111222 
12122222 
22222222 
12673939
```

## 예제 출력
```
4
2
5
2
14
```

## 풀이
```python
import sys
sys.setrecursionlimit(10**7)

N = int(input())
arr = input()

def classify(a, b):
    global arr
    M = arr[a:b+1]
    if M == M[0]*len(M): return 1
    prograssive = True
    for i in range(len(M)-1):
        if  int(M[i+1]) - int(M[i]) != int(M[1]) - int(M[0]):
            prograssive = False
    if prograssive and abs(int(M[1]) - int(M[0])) == 1:
        return 2
    alternating = True
    for i in range(len(M)):
        if(int(M[i]) != int(M[i%2])):
            alternating = False
    if alternating: return 4
    if prograssive: return 5
    return 10

cache = [-1]*10002
def memorize(begin):
    global arr
    if(begin == len(arr)): return 0
    ret = cache[begin]
    if(ret != -1) : return ret
    ret = 987654321
    for L in range(3,6):
        if begin + L <= len(arr):
            cache[begin] = ret = min(ret, memorize(begin + L) + classify(begin, begin + L - 1))
    return ret

for i in range(N):
    print(memorize(0))
    arr = input()
```

해답지처럼 썻다. DI이기 때문에 시간 초과가 날 것이다.

여기서는 memorize부분과 실제적으로 문제를 푸는 부분을 나누어서 풀었다.
기저사례와 문제 푸는 곳과 나뉘어서 푸는 것이 꽤 인상적이었다.
