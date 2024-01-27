class Puzzle:
    def __init__(self, i, j, goal, source=None):
        if source is None:
            source = [[0] * 3 for i in range(3)]
        self.matrix = source
        self.h = 0
        self.blank_i = i
        self.blank_j = j
        self.goal = goal

    def matrix_gen(self, src):
        for i in range(3):
            for j in range(3):
                self.matrix[i][j] = src.matrix[i][j]
        self.matrix[src.blank_i][src.blank_j], self.matrix[self.blank_i][self.blank_j] = \
            self.matrix[self.blank_i][self.blank_j], self.matrix[src.blank_i][src.blank_j]

    def heuristic(self):
        heu = 0
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] != self.goal[i][j]:
                    heu += 1
        self.h = heu
        return


class Heap:
    def __init__(self):
        self.heapsize = 0
        self.array = [[]]

    def heapify(self):
        for i in range(self.heapsize // 2, 0, -1):
            parent, val = i, self.array[i]
            heap = False
            while not heap and parent * 2 <= self.heapsize:
                child = parent * 2
                if child < self.heapsize and self.array[child][0] > self.array[child + 1][0]:
                    child += 1
                if self.array[parent][0] > self.array[child][0]:
                    self.array[parent] = self.array[child]
                else:
                    heap = True
                parent = child
            self.array[parent] = val
        return

    def heappush(self, ele):
        self.heapsize += 1
        self.array.append([])
        i = self.heapsize
        while i > 1 and self.array[i // 2][0] > ele[0]:
            self.array[i] = self.array[i // 2]
            i //= 2
        self.array[i] = ele
        return

    def heappop(self):
        ans = self.array[1]
        temp = self.array[self.heapsize]
        self.heapsize -= 1
        parent, child = 1, 2
        while child <= self.heapsize:
            if child < self.heapsize and self.array[child][0] > self.array[child + 1][0]:
                child += 1
            if temp[0] <= self.array[child][0]:
                break
            self.array[parent] = self.array[child]
            parent, child = child, child * 2
        self.array[parent] = temp
        return ans


def is_safe(pos):
    if 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2:
        return True
    return False


def generate(curr, goal):
    possible_pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    lis = []
    for x in possible_pos:
        if is_safe([curr.blank_i + x[0], curr.blank_j + x[1]]):
            i, j = curr.blank_i + x[0], curr.blank_j + x[1]
            ob = Puzzle(i, j, goal, None)
            ob.matrix_gen(curr)
            ob.heuristic()
            lis.append(ob)
    return lis


def a_star(src, goal):
    queue = Heap()
    queue.heappush([src.h, src, [src.matrix]])
    visit = []
    frontier = []
    while queue.heapsize > 0:
        curr = queue.heappop()
        if curr[1].matrix == goal:
            for i in curr[2]:
                for j in i:
                    print(j)
                print()
            return
        if curr[1].matrix not in visit:
            visit.append(curr[1].matrix)
        adList = generate(curr[1], goal)
        for x in adList:
            if x.matrix not in visit and x.matrix not in frontier:
                path = [i for i in curr[2]]
                g = len(path)
                path.append(x.matrix)
                queue.heappush([x.h + g, x, path])
                frontier.append(x.matrix)
            elif x.matrix in frontier:
                for i in range(1, queue.heapsize + 1):
                    if x.matrix == queue.array[i][1].matrix:
                        if x.h < queue.array[i][0]:
                            del queue.array[i]
                            queue.heapsize -= 1
                            queue.heapify()
                            path = [i for i in curr[2]]
                            g = len(path)
                            path.append(x.matrix)
                            queue.heappush([x.h + g, x, path])
        del curr
        del adList


if __name__ == '__main__':
    s = [[1, 2, 3],
         [5, 6, 0],
         [7, 8, 4]]
    g = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]
    src = Puzzle(1, 2, g, s)
    src.heuristic()
    a_star(src, g)
