class heap:
    def __init__(self, vertices):
        self.heapsize = 0
        self.array = [[] for x in range(vertices)]

    def heapify(self):
        n = self.heapsize
        for i in range(n // 2, 0, -1):
            parent, child = i, i * 2
            heaped = False
            while not heaped and child <= self.heapsize:
                if child < self.heapsize and self.array[child] > self.array[child + 1]:
                    child += 1
                if self.array[parent] > self.array[child]:
                    self.array[parent], self.array[child] = self.array[child], self.array[parent]
                else:
                    heaped = True
        return

    def heap_push(self, ele):
        self.heapsize += 1
        self.array[self.heapsize] = ele
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
    visit = []
    frontier = [src]
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
    adList = [[[2, 1], [5, 3]], [[1, 6]], [[4, 1]], [[5, 1], [6, 6], [2, 4]], [[4, 2], [3, 5]], [[3, 6], [6, 2]],
              [[7, 4]]]
    vertices = 7
    uniform_cost(adList, vertices, 0, 6)
