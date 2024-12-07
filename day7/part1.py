from aocd import submit
from aoc.helpers import input_lines


operators = ["+", "*"]


def do_operator(operator, total, val):
    if operator == "+":
        return total + val
    if operator == "*":
        return total * val


def is_valid(target, vals, total):
    if not len(vals):
        if total == target:
            return True
        return False

    for operator in operators:
        if is_valid(target, vals[1:], do_operator(operator, total, vals[0])):
            return True
    return False


raw_data = open("input.txt", 'r').read()
lines = input_lines(raw_data)

total = 0
for i, line in enumerate(lines):
    vals = line.split(' ')
    first = vals[0].replace(':', '')
    rest = list(map(int, vals[1:]))
    if (is_valid(int(first), rest, 0)):
        total += int(first)

print("Total", total)
