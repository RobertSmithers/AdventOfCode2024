from aocd import submit
from aoc.helpers import input_lines
import numpy as np
from collections import Counter, defaultdict, deque
from typing import List


EX_FILE = "example.txt"
FILE = "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def do_rules(stone_counts):
    def do_rule(num):
        str_num = str(num)
        if num == 0:
            return [1]
        if len(str_num) % 2 == 0:
            return [int(str_num[:len(str_num)//2]), int(str_num[len(str_num)//2:])]
        else:
            return [num * 2024]

    new_counts = Counter()
    for stone, count in stone_counts.items():
        results = do_rule(stone)
        for res in results:
            new_counts[res] += count

    return new_counts


lines = read_lines_to_list()
line = list(map(int, lines[0].split(" ")))
blinks = 75
stone_counts = Counter(line)
for blink in range(blinks):
    stone_counts = do_rules(stone_counts)

total_stones = sum(stone_counts.values())
print(total_stones)
