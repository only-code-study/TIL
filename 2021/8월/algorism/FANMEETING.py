import sys
sys.setrecursionlimit(10**7)
import faulthandler; faulthandler.enable()

def hugs(members, fans):
    N = len(members)
    M = len(fans)
    A = []
    B = []
    for i in range(N):
        A.append(1 if members[i] == 'M' else 0)
    for i in range(M):
        B.append(1 if fans[i] == 'M' else 0)
    C = karatsuba(A, B)
    allHugs = 0
    for i in range(N-1, M):
        if C[i] == 0:
            allHugs += 1
    return allHugs

def karatsuba(A, B):


N = int(input())
for i in range(N):
    print(hugs(input(), input()))