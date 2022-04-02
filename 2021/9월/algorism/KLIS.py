C = int(input())

# 어떠한 수 뒤에 올 lis의 개수를 샌다 + 

def solve():
    global N, arr
    countArr = []
    countArr.append(arr[0])
    maxLen = 1
    tmpArr = []
    tmpLen = 1
    for i in arr[1:]:
        index = binary_search(countArr, i)
        countArr = countArr[:index]
        countArr.append(i) 
        maxLen = max(maxLen, len(countArr))
        # 임시 배열에 배열을 추가
        if maxLen > tmpLen:
            tmpArr.clear()
        tmpArr.append(countArr)
        if len(countArr) < tmpLen:
            tmpArr.pop()

        tmpLen = maxLen
    print(tmpArr)
    return maxLen

def binary_search(arr, x):
    low = 0
    high = len(arr)
    mid = 0
    while low < high:
        mid = (high + low) // 2
        if arr[mid] > x:
            high = mid
        else:
            low = mid + 1
    return high

for i in range(C):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#', solve())
