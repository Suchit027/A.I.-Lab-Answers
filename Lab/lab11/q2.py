def genlist(queens):
    adList = []
    for i in range(4):
        node = [x for x in queens]
        if node[i] < 3:
            node[i] += 1
        mat = [[0] * 4 for x in range(4)]
        for x in range(4):
            mat[node[x]][x] = 1
        adList.append((mat, node))
    return adList


def test(mat):
    count = 0
    for i in range(4):
        row = mat[i]
        for x in row:
            if x == 1:
                count += 1
            if count > 1:
                return False
        count = 0

    for i in range(4):
        for j in range(4):
            if mat[j][i] == 1:
                count += 1
            if count > 1:
                return False
        count = 0
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 1:
                for x, y in zip(range(i, 4), range(j, 4)):
                    if mat[x][y] == 1:
                        return False
    return True


def bfs():
    count = 0
    node = [[0, 0, 0, 0] for x in range(4)]
    for i in range(4):
        node[0][i] = 1
    queue = [(node, [0, 0, 0, 0])]
    visit = []
    while queue:
        queue = queue[::-1]
        curr = queue.pop()
        visit.append(curr[1])
        queue = queue[::-1]
        if curr[1] == [2, 0, 3, 1]:
            print(curr[1])
        if test(curr[0]):
            count += 1
            print(count)
        adList = genlist(curr[1])
        for x in adList:
            if x[1] in visit:
                continue
            queue.append(x)
    print(count)


if __name__ == '__main__':
    bfs()
