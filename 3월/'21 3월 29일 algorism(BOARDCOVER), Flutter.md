# BOARDCOVER

내가 푼거... 속도가 느리다.
'''python
N = int(input())
board = [['#']* 20 for _ in range(20)]
result = 0

def getResult (board, x, y):
    global result
    if y == 18 and x == 18:
        if isFinish(board):
            result = result + 1
            return
        else:
            return
    if board[x][y] == board[x + 1][y] == board[x][y + 1] == '.':
        putPiece(board, x, y, 3)
    if board[x][y] == board[x + 1][y] == board[x + 1][y + 1] == '.':
        putPiece(board, x, y, 2)
    if board[x][y] == board[x][y + 1] == board[x + 1][y + 1] == '.':
        putPiece(board, x, y, 1)
    if board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1] == '.':
        putPiece(board, x, y, 0)
    if x == 18:
        getResult(board, 0, y + 1)
    else:
        getResult(board, x + 1, y)
        
def isFinish(board):
    for i in range(20):
        for j in range(20):
            if(board[i][j] == '.'):
                return False
    return True

def putPiece(board, x, y, index):
    for i in range(2):
        for j in range(2):
            board[x+j][y+i] = '#'
    if x == 18:
        getResult(board, 0, y + 1)
    else:
        getResult(board, x + 1, y)
    for i in range(2):
        for j in range(2):
            board[x+j][y+i] = '.'

def init():
    global board, result
    board = [['#']* 20 for _ in range(20)]
    result = 0
    temp = input()
    H = int(temp[0])
    W = int(temp[1])
    for i in range(H):
        temp = input()
        for j in range(W):
            board[i][j] = temp[j]
    getResult()
    print(result)
    
for i in range(N):
    init()
'''

이런식으로 전체다 접근하면 풀수 있긴 하다.
하지만 자원을 너무 많이 먹기 때문에 다른 방식을 추천하기도 한다.
이는 내일 또 하겠다.

#Flutter
