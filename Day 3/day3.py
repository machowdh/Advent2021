from aocd import get_data, transforms

from collections import Counter

data = get_data(day=3, year=2021)
lines = transforms.lines(data)
columns = list(zip(*lines))

def part_one():
    '''
    Pass in each column of the binary numbers into a Counter to quickly retrieve
    the most common and least common bits per index.
    Convert using builtin int(str, base=10) with base 2 to convert to decimal
    '''
    bits = [Counter(c) for c in columns]
    gamma, epsilon = '', ''
    for freq in bits:
        gamma += freq.most_common()[0][0]
        epsilon += freq.most_common()[1][0]
    
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon

def part_two():
    '''
    Iterate over the total number of columns,
    each time building the respective count of bits for that particular element.

    Filter using a list comprehension based on which one is more common.
    Guard using the length of the lists (oxy, carbon)
    '''
    oxy = lines.copy()
    carbon = lines.copy()
    for i in range(12):
        bits = Counter(num[i] for num in oxy)
        if len(oxy) > 1:
            if bits['1'] >= bits['0']:
                oxy = [num for num in oxy if num[i] == '1']
            else:
                oxy = [num for num in oxy if num[i] != '1']
    
    for i in range(12):
        bits = Counter(num[i] for num in carbon)
        if len(carbon) > 1:
            if bits['1'] < bits['0']:
                carbon = [num for num in carbon if num[i] == '1']
            else:
                carbon = [num for num in carbon if num[i] != '1']


    oxygen_rating = int(''.join(oxy[0]), 2)
    co2_rating = int(''.join(carbon[0]), 2)

    return oxygen_rating * co2_rating

print(f'The power consumption of the submarine is : {part_one()}')
print(f'The life support rating of the submarine is: {part_two()}')