from aocd import submit
from aoc.helpers import input_lines
import numpy as np
from collections import defaultdict, deque
from typing import List, Tuple

EX_FILE = "example.txt"
FILE = "input.txt"

directions = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}


def gimme_2d_arr_np(lines: List[str], dtype) -> np.ndarray:
    return np.array([list(line.strip()) for line in lines], dtype=dtype)


def isInBounds(arr, i, j):
    return 0 <= i < len(arr) and 0 <= j < len(arr[0])


start_and_end = defaultdict(list)


def get_trail_rating(arr, start_r, start_c):
    queue = deque([((start_r, start_c), [(start_r, start_c)])])
    total = 0
    while queue:
        (r, c), path = queue.popleft()
        curr_num = arr[r][c]
        for direction in directions.values():
            new_r, new_c = r + direction[1], c + direction[0]
            if isInBounds(arr, new_r, new_c) and arr[new_r][new_c] - curr_num == 1:
                new_path = path + [(new_r, new_c)]
                if arr[new_r][new_c] == 9:
                    if new_path not in start_and_end[(start_r, start_c)]:
                        start_and_end[(start_r, start_c)].append(new_path)
                        total += 1
                else:
                    queue.append(((new_r, new_c), new_path))
    return total


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

answer = 0
arr = gimme_2d_arr_np(lines, dtype=int)
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] == 0:
            if (r, c) not in start_and_end:
                start_and_end[(r, c)] = []
            answer += get_trail_rating(arr, r, c)

print(answer)
# submit(answer)
