N = int(input())
M = 0
areFriends = [[False]*10]*10
taken = [False]*10
def countPairings(taken):
	firstFree = -1
	for i in range(M) :
		if taken[i] == True :
			firstFree = i
			break
		if firstFree == -1:
			return 1
		ret = 0
		for j in range(firstFree + 1, M):
			if taken[firstFree] and areFriends[firstFree][j]:
				taken[firstFree] = True
				taken[j] = True
				print(taken)
				ret += countPairings(taken)
				taken[firstFree]=False
				taken[j] = False
		return ret
def getRelation():
	temp = input().split()
	a = int(temp[0])
	b = int(temp[1])
	areFriends[a][b] = True
def getResult():
	temp = input().split()
	M = int(temp[0])
	K = int(temp[1])
	for i in range(K):
		getRelation()
	print(countPairings(taken))

for i in range(N):
	areFriends = [[False]*10]*10
	taken = [False]*10
	getResult()
