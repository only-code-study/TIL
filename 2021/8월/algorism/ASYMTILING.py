MOD = 1000000007

cache = [0] * 101
# 1값 직접 대입
cache[1] = 1

def tiling(width):
    if width <= 1: return 1
    ret = cache[width]
    if ret != 0: return ret
    # 모든 경우의 수
    ret = cache[width] = tiling(width - 2) + tiling(width - 1)
    return ret

N = int(input())
for i in range(N):
    width = int(input())
    if width == 2: print(0); continue
    if width == 4: print(2); continue
    tiling(width)
    mid = int(width/2)
    if width % 2 == 0:
        ret = (cache[width] - 2 * cache[mid - 1] - cache[mid - 2])
    else:
        ret = (cache[width] - cache[mid])
    print(ret % MOD)