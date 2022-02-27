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