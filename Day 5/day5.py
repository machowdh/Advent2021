from aocd import get_data, transforms
from collections import defaultdict
from itertools import *

data = get_data(day=5, year=2021)
lines = transforms.lines(data)
lines = [list(chain(*[list(map(int, s.split(','))) for s in line.split(' ') if s != '->'])) for line in lines]

def fill(points, line, diag=False):
    x1, y1, x2, y2 = line
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for y in range(y1, y2 + 1):
            points[(x1, y)] += 1
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for x in range(x1, x2 + 1):
            points[(x, y1)] += 1
    elif diag:
        dx = 1 if x1 < x2 else -1
        dy = 1 if y1 < y2 else -1
        points[(x1, y1)] += 1
        while y1 != y2 and x1 != x2:
            points[(x1 + dx, y1 + dy)] += 1
            x1 += dx
            y1 += dy

def find_overlaps(points):
    return sum(v > 1 for v in points.values())

def part_one():
    points = defaultdict(int)
    for line in lines:
        fill(points, line)
    return find_overlaps(points)

def part_two():
    points = defaultdict(int)
    for line in lines:
        fill(points, line, True)
    return find_overlaps(points)


print(part_one())
print(part_two())
