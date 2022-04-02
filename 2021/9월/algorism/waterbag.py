C = int(input())
arr = [[0]*1500 for i in range(1500)]
tmp = []
for i in range(C):
    tmp.append(list(map(int, input().split())))

for j in tmp:
    half1 = int(j[2] / 2)
    for k in range(j[0] - half1, j[0] + half1):
        half2 = int(j[3] / 2)
        for l in range(j[1] - half2, j[1] + half2):
            arr[k][l] = 1

count = 0
for i in arr:
    for j in i:
        if j != 0:
            count = count + 1
print('#', count)

if int(input()) == -1:
    print("끝!")