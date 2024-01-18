class Edge:
    def __init__(self, s, d):
        self.s = s
        self.d = d


def create():
    a = int(input('enter no. of vertices '))
    adjacencyList = [[] for x in range(a)]
    while True:
        b = input('enter 1 to enter edge 2 to break ')
        if b == '1':
            s = int(input('enter source '))
            d = int(input('enter destination '))
            ob = Edge(s, d)
            adjacencyList[s].append(ob)
        if b == '2':
            break
    return adjacencyList


if __name__ == '__main__':
    l1 = create()
    for i in l1:
        for j in i:
            print(f'{j.s} {j.d}', end=' ')
        print()