import sys
sys.setrecursionlimit(10**7)

def solution(numbers, target):
    return s(numbers, target, 0, 0)

def s(numbers, target, sums, l):
    result = 0
    if l == len(numbers): 
        if sums == target: return 1
        else: return 0
    for i in range(l ,len(numbers)):
        n = numbers[i]
        result += s(numbers, target, sums + n, i + 1)
        result += s(numbers, target, sums - n, i + 1)
    return int((result - 1)/2)

n = list(map(int, input().split()))
t = int(input())
print(solution(n, t))

n.index()