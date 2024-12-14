from aocd import submit
from aoc.helpers import input_lines
import numpy as np
from typing import List

USE_EXAMPLE = False

EX_FILE = "example.txt"
FILE = "input.txt"

ARR_WIDTH = 101
ARR_HEIGHT = 103
EX_ARR_WIDTH = 11
EX_ARR_HEIGHT = 7

if USE_EXAMPLE:
    FILE = EX_FILE
    WIDTH = EX_ARR_WIDTH
    HEIGHT = EX_ARR_HEIGHT
else:
    FILE = FILE
    WIDTH = ARR_WIDTH
    HEIGHT = ARR_HEIGHT


def get_new_pos(p, v, seconds):
    p_x, p_y = p
    v_x, v_y = v
    new_p_x = (p_x + v_x * seconds) % WIDTH
    new_p_y = (p_y + v_y * seconds) % HEIGHT

    if new_p_x < 0:
        new_p_x += WIDTH
    if new_p_y < 0:
        new_p_y += HEIGHT
    return int(new_p_x), int(new_p_y)


def get_arr_after_seconds(arr, ps, vs, seconds):
    for (p, v) in zip(ps, vs):
        new_p_x, new_p_y = get_new_pos(p, v, seconds)
        if 0 <= new_p_y < HEIGHT and 0 <= new_p_x < WIDTH:
            arr[new_p_y, new_p_x] += 1
        else:
            print(f"Invalid position: {(new_p_x, new_p_y)}")

    return arr


def get_p_and_v(line):
    line = line.replace("p=", "").replace("v=", "")
    p, v = line.split()
    p_x, p_y = map(int, p.split(","))
    v_x, v_y = map(int, v.split(","))
    return (p_x, p_y), (v_x, v_y)


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

# Load and parse
ps = []
vs = []
for i, line in enumerate(lines):
    # print(f"Line {i}: {line}")
    p, v = get_p_and_v(line)
    ps.append(p)
    vs.append(v)

# Calculate
arr = np.zeros((HEIGHT, WIDTH), dtype=int)
arr_final = get_arr_after_seconds(arr, ps, vs, seconds=100)

mid_x, mid_y = WIDTH // 2, HEIGHT // 2

q1_sum = np.sum(arr[:mid_y, :mid_x])
q2_sum = np.sum(arr[:mid_y, mid_x + 1:])
q3_sum = np.sum(arr[mid_y + 1:, :mid_x])
q4_sum = np.sum(arr[mid_y + 1:, mid_x + 1:])

total = q1_sum * q2_sum * q3_sum * q4_sum

print(total)
# submit(total)
