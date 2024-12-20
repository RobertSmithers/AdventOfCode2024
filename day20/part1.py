from aocd import submit
from aoc.helpers import input_lines
import numpy as np
from collections import deque
from typing import List


EX_FILE = "example.txt"
FILE = "input.txt"


def gimme_2d_arr_np(lines: List[str], dtype) -> np.ndarray:
    return np.array([list(line.strip()) for line in lines], dtype=dtype)


def get_start_end(grid: np.ndarray):
    start = None
    end = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "E":
                end = (i, j)
    return start, end


def get_fastest_path_values(grid: np.ndarray, start: tuple, end: tuple):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Start from the end so we get a value of "cost remaining" at each position
    queue = deque([(end, 0)])
    visited = set()
    visited.add(end)
    path_values = np.full(grid.shape, np.inf)
    path_values[end] = 0

    while queue:
        (current, running_total) = queue.popleft()

        for direction in directions:
            new_row, new_col = current[0] + \
                direction[0], current[1] + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if grid[new_row, new_col] != '#':
                    new_total = running_total + 1
                    if new_total < path_values[new_row, new_col]:
                        path_values[new_row, new_col] = new_total
                        queue.append(((new_row, new_col), new_total))
                        visited.add((new_row, new_col))

    return path_values


def is_in_bounds(grid: np.ndarray, row: int, col: int) -> bool:
    rows, cols = grid.shape
    return 0 <= row < rows and 0 <= col < cols


def get_unique_skips_below_threshold(grid: np.ndarray, start: tuple, end: tuple, path_values: np.ndarray, threshold: int):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # (position, running_total)
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    unique_skips = set()
    base_cost = path_values[start]

    while queue:
        (current, running_total) = queue.popleft()
        if current == end:
            continue

        for direction in directions:
            new_row, new_col = current[0] + \
                direction[0], current[1] + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[new_row, new_col] != '#':
                    new_total = running_total + 1
                    if (new_row, new_col) not in visited:
                        queue.append(((new_row, new_col), new_total))
                        visited.add((new_row, new_col))

        for skip_direction in directions:
            skip_row, skip_col = current[0] + 2 * \
                skip_direction[0], current[1] + 2 * skip_direction[1]
            if is_in_bounds(grid, skip_row, skip_col):
                if grid[skip_row, skip_col] != '#':
                    new_total = running_total + 1
                    if (skip_row, skip_col) not in visited and new_total + path_values[skip_row, skip_col] < base_cost - threshold:
                        unique_skips.add(
                            (current[0], current[1], skip_row, skip_col, base_cost - (new_total + path_values[skip_row, skip_col] + 1)))

    return unique_skips


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

grid = gimme_2d_arr_np(lines, dtype=str)

start, end = get_start_end(grid)

path_vals = get_fastest_path_values(grid, start, end)
print(path_vals)

valid_skips = get_unique_skips_below_threshold(
    grid, start, end, path_vals, threshold=100)
print(len(valid_skips))
# 1208 wrong
# 1367 right!
