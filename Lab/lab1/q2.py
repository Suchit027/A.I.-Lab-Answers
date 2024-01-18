if __name__ == '__main__':
    adjacencyList = {}
    adjacencyMat = []
    while True:
        b = input('enter 1 to enter edges 2 to print')
        if b == '1':
            s = input('enter source')
            d = input('enter destination')
            w = input('enter weight')
            if s not in adjacencyList.keys():
                adjacencyList[s] = []
            adjacencyList[s].append([d, w])
            adjacencyMat[s][d] = w
        if b == '2':
            print(adjacencyList)
            print()
            print(adjacencyMat)
            break


