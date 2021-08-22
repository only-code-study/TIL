c = int(input())

# 이진 검색 트리
def binarySearch(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def lis(arr):
    # lis를 위한 공간
    resultList = []
    resultList.append(arr[0])
    # 계산하는 위치
    now = 0
    print(arr)
    for i in arr:
        print(resultList, now, i)
        if i > resultList[now]:
            if len(resultList) - 1 == now:
                resultList.append(i)
            else :
                a = now + 1
                if resultList[a] == i:
                    now = now + 1
                    continue
                del(resultList[a])
                resultList.insert(a, i)
            now = now + 1
        elif i == resultList[now]:
            continue
        else:
            a = binarySearch(resultList, i)
            del(resultList[a])
            resultList.insert(a, i)
            now = a
    return len(resultList)

for i in range(c):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print('#', i+1, max(lis(a+b), lis(b+a)))

'''
5 5
3 4 5 7 2
6 4 8 9 1
# 7

5 5
3 4 5 7 2
6 4 8 9 1
# 7

5 5
2 7 7 7 1
5 9 3 6 3
# 4
'''