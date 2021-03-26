N = int(input())
M = 0
areFriends = [[False]*10]*10
taken = [False]*10

def countPairings(taken, start):
	global M
	if all(taken):
		return 1
	ret = 0
	for i in range(start, M):
		for j in range(i+1, M):
			if not taken[i] and areFriends[i][j]:
				taken[i] = True
				taken[j] = True
				ret += countPairings(taken, i)
				taken[i] = False
				taken[j] = False
	return ret

def getRelation(K):
	temp = input().split()
	for i in range(K):
		a = int(temp[2 * i])
		b = int(temp[2 * i + 1])
	areFriends[a][b] = True

def getResult():
	temp = input().split()
	global M 
	M = int(temp[0])
	K = int(temp[1])
	getRelation(K)
	for i in range(M, 10-M):
		taken[i] = True
	print(countPairings(taken, 0))

for i in range(N):
	areFriends = [[False]*10]*10
	taken = [False]*10
	getResult()
