cache= [[-1]*101 for _ in range(101)]

def solve(n, first):
    if n == first: return 1

    if cache[n][first] != -1: return cache[n][first]
    cache[n][first] = 0

    for second in range(1, n - first + 1):
        cache[n][first] = cache[n][first] + solve(n - first, second) * (second + first - 1)
    return cache[n][first] % 10000000

C = int(input())
for i in range(C):
    N = int(input())
    add = 0
    for i in range(1, N + 1):
        add = add + solve(N, i)
    print(add%10000000) 
    