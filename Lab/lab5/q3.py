class heap:
    def __init__(self, vertices):
        self.heapsize = 0
        self.array = [[] for x in range(vertices)]

    def heapify(self):
        for i in range(self.heapsize // 2, 0, -1):
            parent, val = i, self.array[i]
            heaped = False
            while not heaped and parent * 2 <= self.heapsize:
                child = parent * 2
                if child < self.heapsize and self.array[child][0] > self.array[child + 1][0]:
                    child += 1
                if self.array[parent][0] > self.array[child][0]:
                    self.array[parent] = self.array[child]
                else:
                    heaped = True
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


def uniform_cost(adList, vertices, src, goal):
    queue = heap(vertices)
    queue.heap_push([0, src])
    frontier, visit = [], [src]
    while queue.heapsize > 0:
        curr = queue.heap_pop()
        if curr[1] == goal:
            print(f'cost = {curr[0]}')
            return
        if curr[1] not in visit:
            visit.append(curr[1])
        for x in adList[curr[1]]:
            if x[1] not in visit and x[1] not in frontier:
                queue.heap_push([x[0] + curr[0], x[1]])
                frontier.append(x[1])
            elif x[1] in frontier:
                for i in range(1, queue.heapsize + 1):
                    if x[1] == queue.array[i][1]:
                        if x[0] + curr[0] < queue.array[i][0]:
                            del queue.array[i]
                            queue.heapsize -= 1
                            queue.heapify()
                            queue.heap_push([x[0] + curr[0], x[1]])


if __name__ == '__main__':
    adList = [[[8, 2]], [[40, 0], [17, 4]], [[29, 1], [3, 3]], [[11, 0], [46, 5]], [[31, 2], [40, 5], [53, 6]],
              [[15, 6]], [[17, 5]]]
    vertices = 7
    uniform_cost(adList, vertices, 0, 6)