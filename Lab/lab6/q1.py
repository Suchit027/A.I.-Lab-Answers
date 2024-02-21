def value(equation, x):
    ans = 0
    for i in equation.keys():
        ans += equation[i] * (x ** i)
    return ans


def hill_climbing(equation, source, l_range, h_range):
    while True:
        if l_range < source < h_range:
            adList = [source - 1, source + 1]
        elif l_range == source:
            adList = [source + 1]
        else:
            adList = [source - 1]
        flag = True
        for i in adList:
            if value(equation, i) > value(equation, source):
                source = i
                flag = False
                break
        if flag:
            print(f'maximum value = {source}')
            return


if __name__ == '__main__':
    deg = int(input('enter degree of equation '))
    eq = {i: 0 for i in range(deg + 1)}
    for i in range(deg + 1):
        coeff = int(input(f'enter coeff of x^{i} '))
        eq[i] = coeff
    src = int(input('enter source '))
    l = int(input('enter lower range '))
    h = int(input('enter higher range '))
    hill_climbing(eq, src, l, h)