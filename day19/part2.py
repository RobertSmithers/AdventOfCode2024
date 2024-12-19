from aocd import submit
from aoc.helpers import input_lines

EX_FILE = "example.txt"
FILE = "input.txt"


def _design_possibility_helper(patterns, design, memo, i):
    if i == len(design):
        return 1

    if i in memo:
        return memo[i]

    total = 0
    for pattern in patterns:
        if design[i:i + len(pattern)] == pattern:
            total += _design_possibility_helper(patterns,
                                                design, memo, i + len(pattern))

    memo[i] = total
    return total


def is_design_possible(patterns, design):
    memo = {}
    return _design_possibility_helper(patterns, design, memo, 0)


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

patterns = [line.strip() for line in lines[0].split(',')]

total = 0
for i, line in enumerate(lines[2:]):
    design = line.strip()
    total += is_design_possible(patterns, design)

print(total)
# submit(total)
