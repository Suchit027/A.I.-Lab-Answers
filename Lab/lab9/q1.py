def genlist(x, y):
    adList = []
    if x < 4:
        adList.append((4, y))
    if y < 3:
        adList.append((x, 3))
    if x > 0:
        adList.append((0, y))
    if y > 0:
        adList.append((x, 0))
    if x + y >= 4 and y > 0:
        adList.append((4, x + y - 4))
    if x + y >= 3 and x > 0:
        adList.append((x + y - 3, 3))
    if x + y <= 4 and y > 0:
        adList.append((x + y, 0))
    if x + y <= 3 and x > 0:
        adList.append((0, x + y))
    if x == 0 and y == 2:
        adList.append((2, 0))
    return adList


def bfs():
    queue, source = [[(0, 0), [(0, 0)]]], (0, 0)
    while queue:
        queue = queue[::-1]
        curr = queue.pop()
        queue = queue[::-1]
        if curr[0] == (2, 0):
            print(curr[1])
            return
        adList = genlist(curr[0][0], curr[0][1])
        for x in adList:
            path = [x for x in curr[1]]
            path.append(x)
            node = [x, path]
            queue.append(node)
    return


if __name__ == '__main__':
    bfs()
