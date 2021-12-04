from aocd import get_data, transforms
from collections import defaultdict


data = get_data(day=4, year=2021)
lines = transforms.lines(data)

drawn, _, *boards = lines
drawn = list(map(int, drawn.split(',')))

boards = [[int(c) for c in b.split(' ') if c] for b in boards if b]
boards = [boards[i: i + 5] for i in range(0, len(boards), 5)]

marked = defaultdict(lambda : defaultdict(lambda : defaultdict(set)))
unmarked = defaultdict(set)

for k, board in enumerate(boards):
    unmarked[k] = {c for row in board for c in row}
    
def update_board(k, board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                marked[k]['rows'][i].add(num)
                marked[k]['cols'][j].add(num)

def bingo(idx):
    return any(len(marked[idx]['rows'][i]) == 5 for i in range(5)) or any(len(marked[idx]['cols'][j]) == 5 for j in range(5))

def part_one():
    for num in drawn:
        for k, board in enumerate(boards):
            update_board(k, board, num)
            if num in unmarked[k]:
                unmarked[k].remove(num)
            if bingo(k):
                return sum(unmarked[k]) * num

def part_two():
    won = set()
    for num in drawn:
        for k, board in enumerate(boards):
            if k not in won:
                update_board(k, board, num)
                if num in unmarked[k]:
                    unmarked[k].remove(num)
                if bingo(k):
                    won.add(k)
                    last = sum(unmarked[k]) * num
    return last

print(part_one())
print(part_two())
