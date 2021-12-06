from aocd import get_data, transforms
from collections import *
from itertools import *



data = get_data(day=6, year=2021)

def lanternfish(days):
    nums = Counter(list(map(int, data.split(',')))) + Counter({i : 0 for i in range(9)})
    for _ in range(days):
        next_nums = nums.copy()
        for num, count in nums.items():
            if num == 0:
                next_nums[6] += count
                next_nums[0] -= count
                next_nums[8] += count
            else:
                next_nums[num - 1] += count
                next_nums[num] -= count
        nums = next_nums
    return sum(nums.values())


print(lanternfish(80))
print(lanternfish(256))
