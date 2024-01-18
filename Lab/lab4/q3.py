class heap:
    def __init__(self, vertices):
        self.array = [[] for x in range(vertices)]
        self.heapsize = 0
        self.size = vertices

    def hpush(self, ele):
        self.heapsize += 1
        i = self.heapsize
        while i > 1 and self.array[i // 2][0] < ele[0]:
            self.array[i] = self.array[i // 2]
            i //= 2
        self.array[i] = ele
        return

    def hpop(self):
        ans = self.array[1]
        parent, child = 1, 2
        temp = self.array[self.heapsize]
        self.heapsize -= 1
        while child <= self.heapsize:
            if child < self.heapsize and self.array[child][0] < self.array[child + 1][0]:
                child += 1
            if temp[0] >= self.array[child][0]:
                break
            self.array[parent] = self.array[child]
            parent, child = child, child * 2
        self.array[parent] = temp
        return ans


def bfs(adList, src, vertices):
    distance = [1000000] * vertices
    distance[src] = 0
    queue = heap(vertices)
    queue.hpush([0, src])
    visit = []
    while queue.heapsize > 0:
        curr = queue.hpop()
        if curr[1] not in visit:
            visit.append(curr[1])
            for x in adList[curr[1]]:
                if distance[curr[1]] + x[1] < distance[x[0]]:
                    distance[x[0]] = x[1] + distance[curr[1]]
                    queue.hpush([distance[x[0]], x[0]])
    print(distance)


if __name__ == '__main__':
    adList = [[[1, 2], [2, 3], [3, 1]], [[0, 2], [2, 4], [3, 2]], [[0, 3], [1, 4], [3, 3]], [[0, 1], [1, 2], [2, 3]]]
    bfs(adList, 0, 4)
