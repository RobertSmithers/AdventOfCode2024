from aocd import submit
from aoc.helpers import input_lines
import numpy as np
import bisect       # bisect.insort for insert + sort
from functools import lru_cache
from collections import Counter, defaultdict, deque
from copy import deepcopy
from heapq import heappop, heappush, heapify
from typing import List


EX_FILE = "example.txt"
FILE = "input.txt"


def gimme_2d_arr_np(lines: List[str], dtype) -> np.ndarray:
    return np.array([list(line.strip()) for line in lines], dtype=dtype)


block_files = []
free_space = []
count = -1


def get_next_id():
    global count
    count += 1
    return count


def get_parsed_block(line):

    out_block = []
    for i, c in enumerate(line):
        if i % 2 == 0:
            next_block = [get_next_id()] * int(c)
            out_block.extend(next_block)
        else:
            out_block.extend(["."] * int(c))
    return out_block


def move_file_blocks(li):
    p1 = 0
    p2 = len(li) - 1

    while p1 < p2:
        if li[p1] != ".":
            p1 += 1
            continue
        if li[p2] == ".":
            p2 -= 1
            continue

        # Swap the two blocks
        li[p1], li[p2] = li[p2], li[p1]

        p2 -= 1

    return li


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))

    return lines


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

moved = None
for i, line in enumerate(lines):
    parsed = get_parsed_block(line)
    moved = move_file_blocks(parsed)

total = 0
for i, c in enumerate(moved):
    if c != ".":
        total += i * int(c)
print(total)

# 89947706548 wrong

# 5669273231 wrong (if for every id > 10, you cut it off the correct size 3 10's = 101010 --> 101)

# 85457113448 wrong?? encoded every id into it's own number

# 5261752297793 wrong?? parsed each id as it's own number

# 6341711060162 right... converted to array instead
