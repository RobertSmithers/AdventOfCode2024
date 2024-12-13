from aocd import submit
from aoc.helpers import input_lines
import re


EX_FILE = "example.txt"
FILE = "input.txt"

A_BUTTON_COST = 3
B_BUTTON_COST = 1


def solve_machine(dA, dB, prize) -> int:
    dxA, dyA = dA
    dxB, dyB = dB
    targetX, targetY = prize

    min_cost = float('inf')

    # < 100? Say less
    for a in range(101):
        for b in range(101):
            if a * dxA + b * dxB == targetX and a * dyA + b * dyB == targetY:
                cost = A_BUTTON_COST * a + B_BUTTON_COST * b
                if cost < min_cost:
                    min_cost = cost

    if min_cost == float('inf'):
        return 0
    return min_cost


def get_x_y_from_button(line: str) -> tuple:
    match = re.search(r'.*X\+(\d+), Y\+(\d+)', line)
    if match:
        x = int(match.group(1))
        y = int(match.group(2))
        return x, y
    return None


def get_x_y_from_prize(line: str) -> tuple:
    match = re.search(r'Prize: X=(\d+), Y=(\d+)', line)
    if match:
        x = int(match.group(1))
        y = int(match.group(2))
        prize = (x, y)
        return prize
    return None


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

total = 0
dA, dB = None, None

# This is almost certainly a problem of slopes
for i, line in enumerate(lines):
    if not line:
        continue
    if vals := get_x_y_from_button(line):
        x, y = vals
        if line.startswith("Button A"):
            dA = (x, y)
        elif line.startswith("Button B"):
            dB = (x, y)
    elif prize := get_x_y_from_prize(line):
        assert (dA is not None and dB is not None)
        answer = solve_machine(dA, dB, prize)
        if answer:
            total += answer

print(total)
