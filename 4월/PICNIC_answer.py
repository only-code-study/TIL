N = int(input())


def pairing( finished ) :

    if all(finished) :
        return 1

    first_people = finished.index(False)
    count = 0

    for i in range(first_people+1, len(finished)) :

        if not finished[i] and areFriend[first_people][i] :

            finished[i] = True
            finished[first_people] = True
            count += pairing(finished)
            finished[i] = False
            finished[first_people] = False

    return count


for _ in range(N) :

    n,m = map(int, input().split())
    pairs = []
    line = list(map(int,input().split()))

    for i in range(0,m*2,2) :
        pairs.append(line[i:i+2])

    areFriend = [ [ False for _ in range(n)] for _ in range(n) ]

    for pair in pairs :
        areFriend[pair[0]][pair[1]] = True
        areFriend[pair[1]][pair[0]] = True

    finished = [False for _ in range(n)]

    print(pairing(finished))