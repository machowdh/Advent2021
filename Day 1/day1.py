
with open('1.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]
count = 0

for i in range(1, len(lines)):
    if lines[i] > lines[i - 1]:
        count += 1

pt2 = 0
prev_sum = None
for i in range(1, len(lines) - 1):
    window_sum = lines[i - 1] + lines[i] + lines[i + 1]
    if prev_sum and window_sum > prev_sum:
        pt2 += 1
    prev_sum = window_sum
print(pt2)
