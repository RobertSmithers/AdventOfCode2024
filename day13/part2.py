from aocd import submit
from aoc.helpers import input_lines
import re


EX_FILE = "example.txt"
FILE = "input.txt"

A_BUTTON_COST = 3
B_BUTTON_COST = 1


# def find_intersection(m1, b1, y2, m2, x2):
#     assert m1 != m2  # parallel lines

#     # First need to solve for b2 given m2, y2, x2
#     # y2 = m2x2 + b2
#     b2 = y2 - m2 * x2

#     # Now we can combine these system of equations and solve for x
#     # At the intersection, y1 = y2
#     x = (b2 - b1) / (m1 - m2)

#     # Now we solve for y using either equation
#     y = m1 * x + b1

#     return x, y


def solve_machine(dA, dB, prize):
    dxA, dyA = dA
    dxB, dyB = dB
    targetX, targetY = prize

    # Now we have two lines:
    # dxA * B + dxB * A = targetX
    # dyA * B + dyB * A = targetY
    # At first I thought that we could solve this by finding the intersection of
    # these two lines expressed as y = m_A * x + 0 and targetY = m_B * targetX + b (and solve for b to get the actual equation)
    # that intersection would be the optimal solution. However, this is not always the case, so we could instead reduce targetX by one in the A equation
    # meaning that we would be working backwards. The first solution that we find would be the optimal one. -- This is a slightly optimized brute-force solution
    # but ultimately won't be satisfactory because we DO NOT have a guarantee that the solution will be found at all
    # m1 = dxA / dyA
    # m2 = dxB / dyB

    # x, y = find_intersection(m1, 0, targetY, m2, targetX)

    # Soo... instead we go with the direct approach of just solving the system of equations (the first two listed above)

    # Golly gee, latex would be so nice here
    # I will skip the math here, but we have all the values we need to isolate A and B
    A = ((dyB * targetX) - (dxB * targetY)) / (dxA * dyB - dyA * dxB)
    B = ((dyA * targetX) - (dxA * targetY)) / (dyA * dxB - dxA * dyB)

    # Check for integer solutions
    if A.is_integer() and B.is_integer():
        return A_BUTTON_COST * A + B_BUTTON_COST * B

    return 0


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

# This is a problem of slopes
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
        # Part 2: add 10000000000000 to x and y
        prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
        assert (dA is not None and dB is not None)
        answer = solve_machine(dA, dB, prize)
        total += answer

print(int(total))
