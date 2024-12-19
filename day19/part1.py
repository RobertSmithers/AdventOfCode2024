from aocd import submit
from aoc.helpers import input_lines

EX_FILE = "example.txt"
FILE = "input.txt"


def _design_possibility_helper(patterns, design, failed_indices, i):
    if i == len(design):
        return True

    if i in failed_indices:
        return False

    for pattern in patterns:
        if design[i:i + len(pattern)] == pattern and _design_possibility_helper(patterns, design, failed_indices, i + len(pattern)):
            return True

    failed_indices.add(i)
    return False


def is_design_possible(patterns, design):
    failed_indices = set()
    return _design_possibility_helper(patterns, design, failed_indices, 0)


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

patterns = [line.strip() for line in lines[0].split(',')]

total = 0
for i, line in enumerate(lines[2:]):
    design = line.strip()
    if is_design_possible(patterns, design):
        total += 1

print(total)
# submit(total)
