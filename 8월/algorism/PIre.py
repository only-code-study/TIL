import sys
sys.setrecursionlimit(10**7)

N = int(input())
arr = input()

def classify(a, b):
    global arr
    M = arr[a:b+1]
    if M == M[0]*len(M): return 1
    prograssive = True
    for i in range(len(M)-1):
        if  int(M[i+1]) - int(M[i]) != int(M[1]) - int(M[0]):
            prograssive = False
    if prograssive and abs(int(M[1]) - int(M[0])) == 1:
        return 2
    alternating = True
    for i in range(len(M)):
        if(int(M[i]) != int(M[i%2])):
            alternating = False
    if alternating: return 4
    if prograssive: return 5
    return 10

cache = [-1]*10002
def memorize(begin):
    global arr
    if(begin == len(arr)): return 0
    ret = cache[begin]
    if(ret != -1) : return ret
    ret = 987654321
    for L in range(3,6):
        if begin + L <= len(arr):
            ret = min(ret, memorize(begin + L) + classify(begin, begin + L - 1))
    return ret

for i in range(N):
    print(memorize(0))
    arr = input()