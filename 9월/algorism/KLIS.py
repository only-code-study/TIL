C = int(input())

# def solve():
#     global N, arr
#     tmpArr = []
#     tmpArr.append(arr[0])
#     maxLen = 1
#     for i in arr[1:]:
#         index = binary_search(tmpArr, i)
#         tmpArr = tmpArr[:index]
#         tmpArr.append(i) 
#         print(tmpArr)
#         maxLen = max(maxLen, len(tmpArr))
#     return maxLen

# def binary_search(arr, x):
#     low = 0
#     high = len(arr)
#     mid = 0
#     while low < high:
#         mid = (high + low) // 2
#         if arr[mid] > x:
#             high = mid
#         else:
#             low = mid + 1
#     return high

for i in range(C):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#', solve())
