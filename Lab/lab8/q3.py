def cryptic(values, stored):
    if -1 not in stored.values():
        summing = []
        for val in values:
            num = 0
            for x in val:
                num = (10 * num) + stored[x]
            summing.append(num)
        data = summing[:len(summing) - 1]
        if sum(data) == 0:
            return
        if sum(data) == summing[-1]:
            print('yes')
            exit()
        else:
            return
    for i in range(0, 10):
        keys = sorted(stored.keys())
        x = ''
        for x in keys:
            if stored[x] == -1:
                stored[x] = i
                break
        cryptic(values, stored)
        stored[x] = -1
    return


if __name__ == '__main__':
    n = int(input('enter no. of values '))
    test = []
    for i in range(n):
        test.append(input(f'enter value {i + 1} '))
    test.append(input('enter final value '))
    keys = ''.join(test)
    keys = set(keys)
    keys = {x: -1 for x in keys}
    cryptic(test, keys)
