# 여행 짐 싸기
출처: [알고스팟](https://algospot.com/judge/problem/read/PACKING)

## 문제
여행을 떠나기 전날까지 절대 짐을 싸지 않는 버릇이 있는 재훈이는 오늘도 비행기 타기 전날에야 가방을 싸기 위해 자리에 앉았습니다. 비행기 규정상 재훈이는 캐리어를 하나만 가지고 갈 수 있는데, 아무래도 가져가고 싶은 물건들이 캐리어 안에 다 들어가지 않을 것 같습니다. 재훈이는 가져가고 싶은 각 물건들의 부피와 얼마나 필요한지를 나타내는 절박도를 조사해 다음과 같은 목록을 만들었습니다.

|물건|노트북 컴퓨터|카메라|XBOX365|커피그라인더|아령|백과사전|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|부피|4|2|6|4|2|10|
|절박도|7|10|6|7|5|4|

캐리어의 용량이 정해져 있기 때문에 가져갈 수 있는 물건들의 부피 합은 캐리어의 용량 w 이하여야 합니다. 이때 절박도를 최대화할 수 있는 물건들의 목록을 계산하는 프로그램을 작성하세요.

## 입력
입력의 첫 줄에는 테스트 케이스의 수 C (1≤C≤50)가 주어집니다. 각 테스트 케이스의 첫 줄에는 가져가고 싶은 물건의 수 N (1≤N≤100)과 캐리어의 용량 W (1≤W≤1000)가 주어집니다. 그 이후 N줄에 순서대로 각 물건의 정보가 주어집니다. 한 물건에 대한 정보는 물건의 이름, 부피, 절박도 순서대로 주어지며, 이름은 공백 없는 알파벳 대소문자 1글자 이상 20글자 이하의 문자열, 부피와 절박도는 1000 이하의 자연수입니다.

## 출력
각 테스트 케이스별 출력의 첫 줄에는 가져갈 수 있는 물건들의 최대 절박도 합과 가져갈 물건들의 개수를 출력합니다. 이후 한 줄에 하나씩 각 물건들의 이름을 출력합니다. 만약 절박도를 최대화하는 물건들의 조합이 여럿일 경우 아무 것이나 출력해도 좋습니다.

## 예제 입력
```
2
6 10
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4
6 17
laptop 4 7
camera 2 10
xbox 6 6
grinder 4 7
dumbell 2 5
encyclopedia 10 4
```
## 예제 출력
```
24 3
laptop
camera
grinder
30 4
laptop
camera
xbox
grinder
```
# 풀이
결국 이것도 답지 보고 풀게 되었다.
접근방식이 매우 비슷한데, 나는 0에서부터 차근차근 더했지만, 답지에서는 위에서부터 밑으로 깎아 내리는 식으로 풀었다.
```python
import sys
sys.setrecursionlimit(10**7)

C = int(input())

cache = [[-1]*1001 for _ in range(101)]
# 가장 많은 절박도를 뽑아 내는 것
def solve(weight, itemIndex):
    if itemIndex == N: return 0
    ret = cache[weight][itemIndex]
    if ret != -1: return ret
    ret = cache[weight][itemIndex] = solve(weight, itemIndex + 1)
    if weight >= int(thingInfoArr[itemIndex][1]):
        ret = cache[weight][itemIndex] = max(ret, solve(weight - int(thingInfoArr[itemIndex][1]), itemIndex + 1) + int(thingInfoArr[itemIndex][2]))
    return ret

def reconstruct(weight, item):
    if item == N: return
    if solve(weight, item) == solve(weight, item + 1):
        reconstruct(weight, item+1)
    else:
        items.append(thingInfoArr[item][0])
        reconstruct(weight - int(thingInfoArr[item][1]), item + 1)
    return

for i in range(C):
    # N 가져가고 싶은 물건의 수
    # W 케리어의 용량
    N, W = map(int, input().split())
    # 이름[0], 무게[1], 절박도[2]
    thingInfoArr = []
    for j in range(N):
        thingInfoArr.append(input().split())
        # w이하이면서 최대의 물건
    items = []
    reconstruct(W, 0)
    # 값 나올때는 절박도의 합, 물건 개수 그다음 물건 이름 들
    print(solve(W, 0), len(items))
    for i in items:
        print(i)

```