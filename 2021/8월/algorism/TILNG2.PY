MOD = 1000000007
cache = [-1] * 101

def tiling(width):
    if width <= 1: return 1
    ret = cache[width]
    if ret != -1: return ret
    ret = cache[width] = (tiling(width-2) + tiling(width - 1)) % MOD
    return ret

N = int(input())
for i in range(N):
    print(tiling(int(input())))