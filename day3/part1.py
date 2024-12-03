from aocd import get_data, submit
from aoc.helpers import input_lines
import re 

def mul(a, b):
    return a * b

def exec_mul_group(str):
    func_name, args = str.split("(")
    args = args.rstrip(")").split(",")
    result = globals()[func_name](*map(int, args))
    return result

def parse_line(line):
    valid_muls = [m for m in re.finditer("mul\(\d*?,\d*?\)", line)]
    line_mul = 0
    for mul in valid_muls:
        # Because what ever goes wrong with eval on untrusted input :)
        line_mul += exec_mul_group(mul.group())

    return line_mul 

data = get_data(day=3, year=2024)
lines = input_lines(data)

total = 0
for line in lines:
    # print("line is", repr(line))
    total += parse_line(line)

print(total)
# submit(answer)