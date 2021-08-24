C = int(input())
pSum = [-1]*101
pSqSum = [-1]*101
cache = [[-1]*101 for _ in range(11)]
N, S = map(int, input().split())
A = list(map(int, input().split()))

def precalc():
    global A, N, pSqSum, pSum
    A.sort()
    pSum[0] = A[0]
    pSqSum[0] = A[0] * A[0]
    for i in range(1, N):
        pSum[i] = pSum[i-1] + A[i]
        pSqSum[i] = pSqSum[i-1] + A[i] * A[i]

def minError(lo, hi):
    global pSum, pSqSum
    sum = pSum[hi] - (0 if lo == 0 else pSum[lo-1])
    sqSum = pSqSum[hi] - (0 if lo == 0 else pSqSum[lo -1])
    m = int(0.5 + sum / (hi-lo+1))
    ret = sqSum - 2 * m * sum + m * m * (hi-lo+1)
    return ret

def quantize(frm, parts):
    global N
    if frm == N: return 0
    if parts == 0: return 987654321
    ret = cache[frm][parts]
    if ret != -1: return ret
    ret = 987654321
    for partSize in range(1, N - frm):
        ret = min(ret, minError(frm, frm + partSize - 1) +
        quantize(frm + partSize, parts - 1))
    return ret

for i in range(C):
    pSum = [-1]*101
    pSqSum = [-1]*101
    cache = [[-1]*101 for _ in range(11)]
    precalc()
    print(quantize(0, N))
    N, S = map(int, input().split())
    A = list(map(int, input().split()))