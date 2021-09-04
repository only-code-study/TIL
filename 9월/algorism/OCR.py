## 빠른 입력
import sys
m, q = map(int, sys.stdin.readline().rstrip().split())
words = sys.stdin.readline().rstrip().split()
T = []
M = []
answers = []
first = list(map(float, sys.stdin.readline().rstrip().split()))
for i in range(m):
    T.append(list(map(float, sys.stdin.readline().rstrip().split())))
for i in range(m):
    M.append(list(map(float, sys.stdin.readline().rstrip().split())))
for i in range(q):
    answers.append(sys.stdin.readline().rstrip().split())
    del answers[i][0]
rightPer = first
## logic
for i in answers:
    firstWord = words.index(i[0])
    
