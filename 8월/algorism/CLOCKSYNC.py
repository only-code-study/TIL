N = int(input())
arr = [-1] * 10
success = -1
linked = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]

def areAligned():
    global arr
    for i in arr:
        if i != 12:
            return False
    return True

def push(swtch):
    global linked, arr
    for i in linked[swtch]:
        if arr[i] == 12: arr[i] = 3
        else: arr[i] += 3

def solve(swtch):
    if(swtch == 10): return 0 if areAligned() else 9999;
    ret = 9999
    for i in range(4):
        ret = min(ret, i + solve(swtch+1))
        push(swtch)
    return ret

def init():
    global arr
    arr = list(map(int, input().split()))

for i in range(N):
    init()
    print(solve(0))