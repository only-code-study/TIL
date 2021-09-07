cache = []
N = int(input())

def jlis(indexA, indexB):
    ret = cache[indexA+1][indexB+1]
    if ret != -1: return ret
    ret = 2
    a = -1 if indexA == -1 else A[indexA]
    b = -1 if indexB == -1 else B[indexB]
    maxElement = max(a, b);
    for nextA in range(indexA+1, n):
        if maxElement < A[nextA]:
            ret = max(ret, jlis(nextA, indexB) + 1)
    for nextB in range(indexB+1, m):
        if maxElement < B[nextB]:
            ret = max(ret, jlis(indexA, nextB) + 1)
    return ret

for i in range(N):
    n, m= map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    jlis()

