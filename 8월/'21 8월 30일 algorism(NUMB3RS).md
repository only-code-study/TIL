# NUMB3RS
출처: [알고스팟](https://algospot.com/judge/problem/read/NUMB3RS)

## 문제
위험한 살인마 두니발 박사가 감옥에서 탈출했습니다. 수배지를 붙이고 군경이 24시간 그를 추적하고 있지만 용의주도한 두니발 박사는 쉽사리 잡히지 않았습니다. d일이 지난 후에야 경찰은 프로그래밍의 천재인 찰리 교수)를 찾아왔습니다. 찰리 교수는 두니발 박사가 감옥에 남겨둔 노트를 분석해 다음과 같은 가설을 세웠습니다.

두니발 박사는 검문을 피해 산길로만 이동한다.
두니발 박사는 교도소를 탈출한 당일, 교도소와 인접한 마을 하나로 도망쳐 은신한다.
두니발 박사는 수색을 피하기 위해 그 후 매일 인접한 마을로 움직여 은신한다.

![dunibal.png](http://algospot.com/media/judge-attachments/298903b8a37b6938ae6915ce1cab80fd/dunibal.png)

이 가설을 검증하기 위해 교도소로부터 산길로 연결된 n 개 마을들의 지도를 위 그림과 같이 구했습니다. 두니발 박사가 이 가설에 맞춰 행동하고, 움직일 수 있는 마을이 여러 개 있을 경우 그 중의 하나를 임의로 선택한다고 합시다. d 일 후에 두니발 교수가 각 마을에 있을 확률을 계산하는 프로그램을 작성하세요.

예를 들어 위 지도에서 3번 마을에 교도소가 있다고 합시다. 탈옥 직후 두니발 교수는 0번, 1번, 2번, 4번, 5번 중의 한 도시를 임의로 골라 도망칩니다. 따라서 1일 후에 두니발 교수가 0번 마을에 숨어 있을 확률은 1/5이고, 2일 후에 1번 마을에 숨어 있을 확률은 1/15입니다.

## 입력
입력의 첫 줄에는 테스트 케이스의 수 c (1 <= c <= 50) 가 주어집니다. 그 후 각 줄에 지도에 포함된 마을의 수 n (2 <= n <= 50) 과 탈출 후 지금까지 지난 일수 d (1 <= d <= 100), 그리고 교도소가 있는 마을의 번호 p (0 <= p < n) 가 주어집니다. 마을은 0번부터 n-1 번까지 순서대로 번호가 매겨져 있습니다. 그 후 n 줄에는 각각 n 개의 정수로 행렬 A 가 주어집니다. i 번 행의 j 번 숫자 A[i][j] 가 1인 경우 i 번 마을에서 j 번 마을을 잇는 산길이 있다는 것을 의미하며, 0인 경우 길이 없다는 것을 의미합니다. 그 다음 줄에 확률을 계산할 마을의 수 t (1 <= t <= n) 가 주어지고, 그 다음 줄에 t 개의 정수로 확률을 계산할 마을의 번호 q (0 <= q < n) 가 주어집니다.

한 마을에서 다른 마을로 길이 있으면 반대 방향으로도 항상 있으며, 한 마을에서 자기 자신으로 연결되는 길은 없다고 가정해도 좋습니다.

## 출력
각 테스트 케이스마다 t 개의 실수로 각 마을에 두니발 박사가 숨어 있을 확률을 출력합니다. 10-7 이하의 절대/상대 오차가 있는 경우 정답으로 처리됩니다.

## 예제 입력
```
2
5 2 0
0 1 1 1 0
1 0 0 0 1
1 0 0 0 0
1 0 0 0 0
0 1 0 0 0
3
0 2 4
8 2 3
0 1 1 1 0 0 0 0
1 0 0 1 0 0 0 0
1 0 0 1 0 0 0 0
1 1 1 0 1 1 0 0
0 0 0 1 0 0 1 1
0 0 0 1 0 0 0 1
0 0 0 0 1 0 0 0
0 0 0 0 1 1 0 0
4
3 1 2 6
```
## 예제 출력
```
0.83333333 0.00000000 0.16666667
0.43333333 0.06666667 0.06666667 0.06666667
```

## 풀이

오래간만에 혼자 힘으로 풀어보았다.(전혀 답지를 보지 않았다!!)
크게 2가지로 볼 수 있다. 

1. 첫번째는 각 지역데서 다른 지역으로 갈 확률을 구하는 것, 
1. 두번째는 다음날 그 지역으로 갈 수 있다면, 자기 자신이 가지고 있는 확률에 첫번째로 구햇던 다른 지역으로 갈 수 있는 확률을 곱하면 되는 것이다.

```python
def search(day):
    global homePercentage, goPercentage, arr
    if day == 0: return putResArr()
    length = len(homePercentage)
    tmpArr = [0] * length
    for i in range(length):
        for j in range(length):
            if goPercentage[j] == 0: continue
            elif arr[i][j] == 1:
                tmpArr[i] = tmpArr[i] + homePercentage[j] / goPercentage[j]
    homePercentage = tmpArr
    return search(day - 1)

def putResArr():
    tmpArr = []
    for i in resArr:
        tmpArr.append(homePercentage[i])
    return tmpArr

def getGoPercentage():
    global goPercentage, arr
    pls = 0
    for i in range(len(arr)):
        for j in arr[i]:
            if j == 1:
                pls = pls + 1
        goPercentage[i] = pls
        pls = 0


C = int(input())
arr = []
for i in range(C):
    home, day, prison = map(int, input().split())
    arr.clear()
    for i in range(home):
        arr.append(list(map(int, input().split())))
    case = int(input())
    resArr = list(map(int, input().split()))
    # 현재 자신의 퍼센티지
    homePercentage = [0] * home
    # 다른 지역으로 갈 수 있는 확률
    goPercentage = [0] * home
    getGoPercentage()
    homePercentage[prison] = 1

    print()
    for i in search(day):
        print(i, end=" ")
    print()
```
