# 1 모든 숫자가 같을때
# 2 숫자가 1씩 증가하거나 감소할 때
# 4 두개의 숫자가 번갈아 가며 나타날 때
# 10 이 외의 모든 경우

def getLevel(arr):
    result = 0
    sameValues = False
    upOrdownValues = False
    switchValues = False
    tmp = 0
    count = 0
    for i in range(len(arr)):
        count = count + 1
        if i == 0: continue
        
        first = arr[i-1]
        second = arr[i]
        if i > 1: tmp = arr[i-2]

        if first == second: 
            if sameValues: continue
            count = 0
            sameValues = True
            upOrdownValues = False
            switchValues = False
            if count < 4: continue
            result = result + 1
            if count == 5:
                sameValues = False
            continue
        if first == second + 1 or first == second - 1:
            if upOrdownValues: continue
            count = 0
            result = result + 2
            sameValues = False
            upOrdownValues = True
            switchValues = False
            continue
        if tmp == second:
            if switchValues: continue
            count = 0
            result = result + 4
            sameValues = False
            upOrdownValues = False
            switchValues = True
            continue
        result = result + 10
    return result

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    print(getLevel(arr))

