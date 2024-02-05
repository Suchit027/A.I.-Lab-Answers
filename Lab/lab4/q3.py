class Heap:
    def __init__(self):
        self.array = [[]]
        self.heapsize = 0

    def hpush(self, ele):
        self.heapsize += 1
        # dynamically increase array size
        self.array.append([])
        i = self.heapsize
        while i > 1 and self.array[i // 2][0] > ele[0]:
            self.array[i] = self.array[i // 2]
            i //= 2
        self.array[i] = ele
        return

    def hpop(self):
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
            parent = child
            child *= 2
        self.array[parent] = temp
        return ans


def tsp(adList, value, src):
    vertices = len(adList)
    lb = vertices * value[src]
    # first index for lower bound, second for index, third for path, fourth for value
    source = [lb, src, [src], 0]
    queue = Heap()
    queue.hpush(source)
    while queue.heapsize > 0:
        curr = queue.hpop()
        if len(curr[2]) == vertices:
            last = curr[2][-1]
            # finding the cost to reach the starting position
            for x in adList[src]:
                if x[1] == last:
                    curr[3] += x[0]
            print(f'cost = {curr[3]} and path = {curr[2]}')
            return
        for x in adList[curr[1]]:
            if x[1] in curr[2]:
                continue
            # new cost
            new_val = x[0] + curr[3]
            # lower bound
            lb = (vertices - len(curr[2])) * (value[x[1] + 1]) + new_val
            # new path
            path = [i for i in curr[2]]
            path.append(x[1])
            queue.hpush([lb, x[1], path, new_val])
    return


if __name__ == '__main__':
    adList = [[[2, 1], [3, 2], [1, 3]], [[2, 0], [4, 2], [2, 3]], [[3, 0], [4, 1], [3, 3]], [[1, 0], [2, 1], [3, 2]]]
    # Value list can be made using for loop. It contains minimum edge value from the current vertice
    # The last 0 is to avoid index out of range when calculating lower bound of last vertice
    value = [1, 2, 3, 1, 0]
    src = 0
    tsp(adList, value, src)
