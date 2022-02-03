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