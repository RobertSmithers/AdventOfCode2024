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


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(EX_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def flatten(t):
    return [item for sublist in t for item in (sublist if isinstance(sublist, tuple) else [sublist])]


def do_rules(arr):
    def do_rule(num):
        str_num = str(num)
        if num == 0:
            return [1]
        if len(str_num) % 2 == 0:
            return [int(str_num[:len(str_num)//2]), int(str_num[len(str_num)//2:])]
        else:
            return [int(num) * 2024]

    vals = list(map(do_rule, arr))

    # Flatten vals to clear tuples
    return flatten(vals)


lines = read_lines_to_list()
line = list(map(int, lines[0].split(" ")))
blinks = 25
for blink in range(blinks):
    line = do_rules(line)

print(len(line))
