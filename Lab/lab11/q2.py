def genlist(mat):
    adList = []
    for i in range(8):
        node = [[0, 0, 0, 0, 0, 0, 0, 0] for x in range(8)]
        for x in range(7):
            for y in range(8):
                if mat[x][i] == 1:
                    node[x + 1][i] = 1
                else:
                    node[x][y] = mat[x][y]
        adList.append(node)
    return adList


def test(mat):
    count = 0
    for i in range(8):
        row = mat[i]
        for x in row:
            if x == 1:
                count += 1
        if count > 1:
            return False
        count = 0

    for i in range(8):
        for j in range(8):
            if mat[j][i] == 1:
                count += 1
        if count > 1:
            return False
        count = 0
    for i in range(8):
        for j in range(8):
            if mat[i][j] == 1:
                for x, y in zip(range(i, -1, -1), range(j, -1, -1)):
                    if mat[x][y] == 1:
                        return False
    return True


def bfs():
    count = 0
    node = [[0, 0, 0, 0, 0, 0, 0, 0] for x in range(8)]
    for i in range(8):
        node[0][i] = 1
    queue = [node]
    while queue:
        queue = queue[::-1]
        curr = queue.pop()
        queue = queue[::-1]
        if test(curr):
            count += 1
        adList = genlist(curr)
        for x in adList:
            queue.append(x)
    print(count)


if __name__ == '__main__':
    bfs()
