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


def dfs(x, y, path):
    if len(path) >= 10:
        return
    if x == 2 and y == 0:
        print(path)
        exit()
    adList = genlist(x, y)
    for x in adList:
        n_path = [x for x in path]
        n_path.append((x[0], x[1]))
        dfs(x[0], x[1], n_path)

if __name__ == '__main__':
    dfs(0, 0, [])