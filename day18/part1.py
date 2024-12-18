from aocd import submit
from aoc.helpers import input_lines
import numpy as np
from collections import Counter, defaultdict, deque
from typing import List

IS_EXAMPLE = False

EX_FILE = "example.txt"
FILE = "input.txt"
if IS_EXAMPLE:
    FILE = EX_FILE

grid_sz = 71
if IS_EXAMPLE:
    grid_sz = 7


def is_in_bounds(x, y):
    return 0 <= x < grid_sz and 0 <= y < grid_sz


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

grid = np.zeros((grid_sz, grid_sz), dtype=int)

for i, line in enumerate(lines):
    x, y = list(map(int, line.split(',')))
    grid[y, x] = 1
    if i == 1023:
        break

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque([(0, 0, 0)])
visited = set()
min_steps = 0
while queue:
    x, y, steps = queue.popleft()
    if x == grid_sz - 1 and y == grid_sz - 1:
        # Since we're doing bfs, min_steps is naturally first time we reach the end
        min_steps = steps
        break

    if (x, y) in visited:
        continue

    visited.add((x, y))

    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if is_in_bounds(new_x, new_y) and grid[new_x, new_y] == 0:
            queue.append((new_x, new_y, steps + 1))

print(min_steps)
# submit(total)
