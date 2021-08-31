def search(day):
    global homePercentage, goPercentage, arr
    if day == 0: return putResArr()
    length = len(homePercentage)
    tmpArr = [0] * length
    for i in range(length):
        for j in range(length):
            if goPercentage[j] == 0: continue
            elif arr[i][j] == 1:
                tmpArr[i] = tmpArr[i] + homePercentage[j] / goPercentage[j]
    homePercentage = tmpArr
    return search(day - 1)

def putResArr():
    tmpArr = []
    for i in resArr:
        tmpArr.append(homePercentage[i])
    return tmpArr

def getGoPercentage():
    global goPercentage, arr
    pls = 0
    for i in range(len(arr)):
        for j in arr[i]:
            if j == 1:
                pls = pls + 1
        goPercentage[i] = pls
        pls = 0


C = int(input())
arr = []
for i in range(C):
    home, day, prison = map(int, input().split())
    arr.clear()
    for i in range(home):
        arr.append(list(map(int, input().split())))
    case = int(input())
    resArr = list(map(int, input().split()))
    # 현재 자신의 퍼센티지
    homePercentage = [0] * home
    # 고정된 확률 / 로 된거
    goPercentage = [0] * home
    getGoPercentage()
    homePercentage[prison] = 1

    print()
    for i in search(day):
        print(i, end=" ")
    print()