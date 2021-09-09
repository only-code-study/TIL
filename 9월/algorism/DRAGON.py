C = int(input())

cache = [''] * 51
cache[0] = 'FX'

def solve(genaration):
    if cache[genaration] != '': return cache[genaration]
    for i in range(genaration + 1):
        if cache[i] != '': continue
        tmpst = cache[i - 1]
        for j in list(tmpst):
            if j == 'X':
                cache[i] = cache[i] + 'X+YF'
            elif j == 'Y':
                cache[i] = cache[i] + 'FX-Y'
            else:
                cache[i] = cache[i] + j

    return cache[genaration]

for i in range(C):
    n, p, l = map(int, input().split())
    print(solve(n)[p - 1:p + l - 1])