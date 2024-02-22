def gen_states(queens, n):
    adList = []
    for i in range(n):
        if queens[i] < n - 1:
            node = queens[:i] + [queens[i] + 1] + queens[i + 1:]
            adList.append(node)
    return adList


def value(state, n):
    ans = 0
    board = [[0] * n for x in range(n)]
    for i in range(n):
        board[state[i]][i] = 1
    for i in range(n):
        for i in board[state[i]][i + 1:]:
            if i == 1:
                ans += 1
        for x, y in zip(range(state[i] + 1, n), range(i + 1, n)):
            if board[x][y] == 1:
                ans += 1
        for x, y in zip(range(state[i] - 1, 0, -1), range(i + 1, n)):
            if board[x][y] == 1:
                ans += 1
    return ans


def hill_climbing(n):
    state = [0] * n
    iterations = 0
    while True:
        adList = gen_states(state, n)
        flag = True
        for i in adList:
            if value(i, n) <= value(state, n):
                flag = False
                state = i
                break
        if flag:
            print(f'solution found = {state}, value = {value(state, n)}')
            return


if __name__ == '__main__':
    hill_climbing(4)
