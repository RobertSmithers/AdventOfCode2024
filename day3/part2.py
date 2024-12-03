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

def get_next_largest_idx(largest_val, lst):
    return max([i for i in lst if i < largest_val], default=None)

# Do mul is enabled at the start
def parse_line(line, is_enabled=True):
    valid_muls = [m for m in re.finditer("mul\(\d*?,\d*?\)", line)]
    enabled_idxs = [m.start() for m in re.finditer("do\(\)", line)]
    disabled_idxs = [m.start() for m in re.finditer("don\'t\(\)", line)]

    # Ideally, I wanted to have a moving pointer for each list of indices for efficient lookup
    # but ultimately, just using max and another linear search is good enough for this problem

    line_mul = 0
    for mul in valid_muls:
        curr_idx = mul.start()

        # Determine if this mul is enabled or not
        enabled_p = get_next_largest_idx(curr_idx, enabled_idxs)
        disabled_p = get_next_largest_idx(curr_idx, disabled_idxs)

        # Only two options (there's either no index before this "largest value" or there is and it's smaller)
        assert(enabled_p is None or enabled_p < curr_idx)
        assert(disabled_p is None or disabled_p < curr_idx)

        if enabled_p is not None and disabled_p is not None:
            if enabled_p > disabled_p:
                is_enabled = True
            else:
                is_enabled = False
        elif enabled_p is not None:
            is_enabled = True
        elif disabled_p is not None:
            is_enabled = False

        # If both none, then is_enabled is carried over from the last line

        if is_enabled:
            # Because what ever goes wrong with eval on untrusted input :)
            line_mul += exec_mul_group(mul.group())

    return line_mul, is_enabled

data = get_data(day=3, year=2024)
lines = input_lines(data)

total = 0
is_enabled = True
for line in lines:
    mul_sum, is_enabled = parse_line(line, is_enabled)
    total += mul_sum

print(total)
# submit(answer)