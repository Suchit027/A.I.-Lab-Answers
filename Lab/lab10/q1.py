def wumpus(w_path, path, perf):
    for i in w_path:
        if i not in path:
            print(f'performance = {perf - 1000}')
            exit()
    return perf - 10


def pit(p_path, path, pit_pos, perf):
    for i in p_path[pit_pos]:
        if i not in path:
            print(f'performace = {perf - 1000}')
            exit()
    return True


def move(x, y, path, w_path, p_path):
    adList = []
    pits = []
    for i in p_path.values():
        pits = pits + i
    if x < 3:
        if (x + 1, y) in w_path or (x + 1, y) in pits:
            adList.append((x + 1, y))
        elif (x + 1, y) not in path:
            adList = adList[::-1]
            adList.append((x + 1, y))
            adList = adList[::-1]
        else:
            pass
    if x > 0:
        if (x - 1, y) in w_path or (x - 1, y) in pits:
            adList.append((x - 1, y))
        elif (x - 1, y) not in path:
            adList = adList[::-1]
            adList.append((x - 1, y))
            adList = adList[::-1]
        else:
            pass
    if y < 3:
        if (x, y + 1) in w_path or (x, y + 1) in pits:
            adList.append((x, y + 1))
        elif (x, y + 1) in path:
            adList = adList[::-1]
            adList.append((x, y + 1))
            adList = adList[::-1]
        else:
            pass
    if y > 0:
        if (x, y - 1) in w_path or (x, y - 1) in pits:
            adList.append((x, y - 1))
        elif (x, y - 1) in path:
            adList = adList[::-1]
            adList.append((x, y - 1))
            adList = adList[::-1]
        else:
            pass
    return adList


def dfs(adMat, x, y, p_path, w_path, path, perf):
    if adMat[x][y] == 'T':
        print(f'performance = {perf + 1000}')
        exit()
    if adMat[x][y] == 'W':
        perf = wumpus(w_path, path, perf)
        adList = move(x, y, path, w_path, p_path)
        for i in adList:
            if i not in path:
                path.append(i)
                dfs(adMat, i[0], i[1], p_path, w_path, path, perf)
                path.remove(i)
    if adMat[x][y] == 'P':
        if pit(p_path, path, (x, y), perf):
            return
    adList = move(x, y, path, w_path, p_path)
    for i in adList:
        if i not in path:
            path.append(i)
            dfs(adMat, i[0], i[1], p_path, w_path, path, perf)
            path.remove(i)
    return


if __name__ == '__main__':
    adMat = [['.'] * 4 for x in range(4)]
    w_path, p_path = [], {}
    w_x = int(input('enter x pos for wumpus '))
    w_y = int(input('enter y pos for wumpus '))
    adMat[w_x][w_y] = 'W'
    if w_x < 3:
        w_path.append((w_x + 1, w_y))
    if w_x > 0:
        w_path.append((w_x - 1, w_y))
    if w_y < 3:
        w_path.append((w_x, w_y + 1))
    if w_y > 0:
        w_path.append((w_x, w_y - 1))
    p = int(input('enter no. of pits '))
    for i in range(p):
        x = int(input('enter pit x pos '))
        y = int(input('enter pit y pos '))
        adMat[x][y] = 'P'
        if x < 3:
            p_path[(x, y)] = p_path.get((x, y), []) + [(x + 1, y)]
        if x > 0:
            p_path[(x, y)] = p_path.get((x, y), []) + [(x - 1, y)]
        if y < 3:
            p_path[(x, y)] = p_path.get((x, y), []) + [(x, y + 1)]
        if y > 0:
            p_path[(x, y)] = p_path.get((x, y), []) + [(x, y - 1)]
    t_x = int(input('enter treasure x pos '))
    t_y = int(input('enter treasure y pos '))
    adMat[t_x][t_y] = 'T'
    s_x = int(input('enter start x pos '))
    s_y = int(input('enter start y pos '))
    dfs(adMat, s_x, s_y, p_path, w_path, [(s_x, s_y)], 0)
