C = int(input())

def getResult(n):
    global result
    if n == 0:
        return
    for i in range(n):
        result[n-1][i] = max(result[n-1][i]+result[n][i], result[n-1][i]+result[n][i+1])
    getResult(n-1)

for i in range(C):
    n = int(input())
    result = []
    # 5개 받는 구문
    for j in range(n):
        result.append(list(map(int, input().split())))
    #아래에서 부터 더하는 부분
    getResult(n-1)
    print(result[0][0])
