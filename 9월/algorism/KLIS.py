import math

C = int(input())
casheLen = [-1] * 501
cacheCnt = [-1] * 501
S = [-1] * 501

def lis(arr):
    if not arr:
        return 0
    
    ret = 1
    for i in range(len(arr)):
        nxt = []
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
        ret = max(ret, 1 + lis(nxt))
    return ret	

for i in range(C):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#', lis(arr))