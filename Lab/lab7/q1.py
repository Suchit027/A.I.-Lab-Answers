class Heap:
    def __init__(self, vertices):
        self.heapsize = 0
        self.array = [[] for x in range(vertices)]

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

    def heap_push(self, ele):
        self.heapsize += 1
        i = self.heapsize
        while i > 1 and self.array[i // 2][0] > ele[0]:
            self.array[i] = self.array[i // 2]
            i //= 2
        self.array[i] = ele
        return

    def heap_pop(self):
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


def a_star(adList, vertices, heuristic, src, goal):
    queue = Heap(vertices)
    queue.heap_push([heuristic[src], src, [src]])
    frontier, visit = [], []
    while queue.heapsize > 0:
        curr = queue.heap_pop()
        if curr[1] == goal:
            print(f'path = {curr[2]}')
            return
        if curr[1] not in visit:
            visit.append(curr[1])
        for x in adList[curr[1]]:
            if x[1] not in visit and x[1] not in frontier:
                path = [i for i in curr[2]]
                path.append(x[1])
                queue.heap_push([heuristic[x[1]] + x[0] + curr[0] - heuristic[curr[1]], x[1], path])
                frontier.append(x[1])
            elif x[1] in frontier:
                for i in range(1, queue.heapsize + 1):
                    if x[1] == queue.array[i][1]:
                        if x[0] + heuristic[x[1]] + curr[0] - heuristic[curr[1]] < queue.array[i][0]:
                            del queue.array[i]
                            queue.heapsize -= 1
                            queue.heapify()
                            path = [i for i in curr[2]]
                            path.append(x[1])
                            queue.heap_push([x[0] + heuristic[x[1]] + curr[0] - heuristic[curr[1]], x[1], path])


if __name__ == '__main__':
    vertices = 10
    heuristic = {i: 0 for i in range(vertices)}
    heuristic[0], heuristic[1], heuristic[2], heuristic[3], heuristic[4], heuristic[5], heuristic[6], heuristic[7], \
        heuristic[8], heuristic[9] = 10, 8, 5, 7, 3, 6, 5, 3, 1, 0
    adList = [[[6, 1], [3, 5]], [[6, 0], [3, 2], [2, 3]], [[3, 1], [1, 3], [5, 4]], [[2, 1], [1, 2], [8, 4]],
              [[5, 2], [8, 3], [5, 8], [5, 9]], [[1, 6], [3, 0], [7, 7]], [[1, 5], [3, 8]], [[7, 5], [2, 8]],
              [[3, 6], [2, 7], [5, 4], [3, 9]], [[3, 8], [5, 4]]]
    a_star(adList, vertices, heuristic, 0, 9)
