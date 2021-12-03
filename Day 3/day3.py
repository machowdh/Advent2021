from collections import Counter, defaultdict

with open('3.txt') as f:
    data = [list(line.strip()) for line in f.readlines()]


# gamma rate epsilon rate
#

bits = {}
i = 0
for d in zip(*data):
    bits[i] = Counter(d)
    i += 1

gamma = [''] * 12
epsilon = [''] * 12
for i in range(12):
    gamma[i] = bits[i].most_common()[0][0]
    epsilon[i] = bits[i].most_common()[1][0]

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)

# print(gamma * epsilon)

def part_two(bits):
    obits = bits.copy()
    cbits = bits.copy()

    oxygen = [''] * 12
    C02 = [''] * 12
    o, c = data.copy(), data.copy()
    for i in range(12):
        if len(o) > 1:
            ones, zeros = obits[i]['1'], obits[i]['0']
            if ones >= zeros:
                o = [num for num in o if num[i] == '1']
            elif ones < zeros:
                o = [num for num in o if num[i] == '0']
            j = 0
            for x in zip(*o):
                obits[j] = Counter(x)
                j += 1

    for i in range(12):
        if len(c) > 1:
            ones, zeros = cbits[i]['1'], cbits[i]['0']
            if ones < zeros:
                c = [num for num in c if num[i] == '1']
            else:
                c = [num for num in c if num[i] == '0']
            j = 0
            for x in zip(*c):
                cbits[j] = Counter(x)
                j += 1

    print(o, c)        
    oxygen = int(''.join(o[0]), 2)
    C02 = int(''.join(c[0]), 2)
    print(oxygen, C02)
    print(oxygen * C02)

part_two(bits)
