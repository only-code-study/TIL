import sys
sys.setrecursionlimit(10**7)

C = int(input())

cache = [[-1]*1001 for _ in range(101)]
# 가장 많은 절박도를 뽑아 내는 것
def solve(weight, itemIndex):
    if itemIndex == N: return 0
    ret = cache[weight][itemIndex]
    if ret != -1: return ret
    ret = cache[weight][itemIndex] = solve(weight, itemIndex + 1)
    if weight >= int(thingInfoArr[itemIndex][1]):
        ret = cache[weight][itemIndex] = max(ret, solve(weight - int(thingInfoArr[itemIndex][1]), itemIndex + 1) + int(thingInfoArr[itemIndex][2]))
    return ret

def reconstruct(weight, item):
    if item == N: return
    if solve(weight, item) == solve(weight, item + 1):
        reconstruct(weight, item+1)
    else:
        items.append(thingInfoArr[item][0])
        reconstruct(weight - int(thingInfoArr[item][1]), item + 1)
    return

for i in range(C):
    # N 가져가고 싶은 물건의 수
    # W 케리어의 용량
    N, W = map(int, input().split())
    # 이름[0], 무게[1], 절박도[2]
    thingInfoArr = []
    for j in range(N):
        thingInfoArr.append(input().split())
        # w이하이면서 최대의 물건
    items = []
    reconstruct(W, 0)
    # 값 나올때는 절박도의 합, 물건 개수 그다음 물건 이름 들
    print(solve(W, 0), len(items))
    for i in items:
        print(i)
