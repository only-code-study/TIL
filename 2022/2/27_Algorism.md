# Algorism
## [웨브바짐](https://algospot.com/judge/problem/read/ZIMBABWE)
### 풀이
```py
import sys
sys.setrecursionlimit(200000000)

def countResult(e: str, m: str, c: list[int], b:str):
    result = 0
    for i, v in enumerate(c):
        if v != 0:
            if b == '' and v == 0: continue

            c[i] -= 1
            b += str(i)

            r = countResult(e, m, c, b)
            if r == -1:
                return result % 1000000007
            result += r

            b = b[:-1]
            c[i] += 1
        if i == 9 and len(e) == len(b):
            if int(e) > int(b):
                if (int(b) % int(m)) == 0:
                    return 1
            else:
                return -1
    return result % 1000000007

def countNumber(e):
    result = [0 for i in range(10)]
    for i in e:
        result[int(i)] += 1
    return result

for i in range(int(input())):
    e, m = input().split()
    c = countNumber(e)
    r = countResult(e, m, c, "")
    print(r)
```
다음과 같이 풀었다.

1. 적은 수부터 계산한다
2. 마지막과 총 길이가 같다면(어자피 중복이 안된다) 나누어서 검사한다
3. 만약 맞다면 1을 더하고 아니라면 넘어간다
4. 큰 수를 만난다면 어자피 그 뒤 수도 큰 수이므로, -1을 넘겨 넘기라는 코드로 한다.

알고스팟에서는 python3로 하면 RTE(nonzero return code)가 뜬다. 아마 제 시간안에 못풀어서 그러거나, 메모리를 초과(하려나...? 메모리 안쓰는데?)해서 그럴 것이다.