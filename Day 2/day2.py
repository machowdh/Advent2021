
with open('2.txt') as f:
    data = [line.split() for line in f.readlines()]

position, depth, aim = 0, 0, 0

for direction, amount in data:
    if direction == 'forward':
        position += int(amount)
        depth += aim * int(amount)
    elif direction ==  'up':
        aim -= int(amount)
    else:
        aim += int(amount)
        

print(position * depth)
