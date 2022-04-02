C = int(input())

def solve(start, count):
    signCount = (int(start/3), int((start + count * 2) / 3))
    signChar = []
    ret = ''
    startChar = start % 6
    
    for i in range(signCount[0], signCount[1]):
        root = 0
        for j in range(51): 
            if (i - root) % ((root + 1) * 4) == 0:
                signChar.append('+')
                break
            elif (i - root + (root + 1) * 2) % ((root + 1) * 4 ) == 0:
                signChar.append('-')
                break
            root += j + 1
    print(signChar)

    for i in range(startChar, startChar + count):
        i = i % 6
        if i == 3 or i == 0: ret += signChar.pop(0)
        if i == 1 or i == 5: ret += 'F'
        if i == 2: ret += 'X'
        if i == 4: ret += 'Y'
    return ret

for i in range(C):
    n, p, l = map(int, input().split())
    print(solve(p, l))