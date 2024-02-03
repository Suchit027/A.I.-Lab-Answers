def tsp(adList, visit, curr, cost, min_cost, to_gaal):
    if len(visit) == len(adList):
        if cost < min_cost:
            min_cost = cost
        min_cost += to_gaal[curr]
        return min_cost
    for x in adList[curr]:
        if x[1] not in visit:
            visit.append(x[1])
            min_cost = tsp(adList, visit, x[1], cost + x[0], min_cost, to_goal)
            visit.remove(x[1])
    return min_cost


if __name__ == '__main__':
    adList = [[[2, 1], [3, 2], [1, 3]], [[2, 0], [4, 2], [2, 3]], [[3, 0], [4, 1], [3, 3]], [[1, 0], [2, 1], [3, 2]]]
    to_goal = {1: 2, 2: 3, 3: 1}
    ans = tsp(adList, [0], 0, 0, 10000, to_goal)
    print(ans)
