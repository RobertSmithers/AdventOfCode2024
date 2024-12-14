from aocd import submit
from aoc.helpers import input_lines
import numpy as np
from typing import List
import sys

USE_EXAMPLE = False

EX_FILE = "example.txt"
FILE = "input.txt"

ARR_WIDTH = 101
ARR_HEIGHT = 103
EX_ARR_WIDTH = 11
EX_ARR_HEIGHT = 7

SYMMETRY_THRESHOLD = 15
RATIO_THRESHOLD = 0.5

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
    new_ps = []
    for (p, v) in zip(ps, vs):
        new_p_x, new_p_y = get_new_pos(p, v, seconds)
        new_ps.append([new_p_x, new_p_y])
        if 0 <= new_p_y < HEIGHT and 0 <= new_p_x < WIDTH:
            arr[new_p_y, new_p_x] += 1
        else:
            print(f"Invalid position: {(new_p_x, new_p_y)}")

    new_ps = np.array(new_ps)
    return arr, new_ps


def get_p_and_v(line):
    line = line.replace("p=", "").replace("v=", "")
    p, v = line.split()
    p_x, p_y = map(int, p.split(","))
    v_x, v_y = map(int, v.split(","))
    return (p_x, p_y), (v_x, v_y)


def is_symmetric_horizontal(arr):
    for i in range(HEIGHT // 2):
        for j in range(WIDTH):
            if arr[i, j] != arr[HEIGHT - i - 1, j]:
                return False
    return True


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

# Load and parse
ps = []
vs = []
for i, line in enumerate(lines):
    p, v = get_p_and_v(line)
    ps.append(p)
    vs.append(v)

# Calculate
# Remove np print restrictions
np.set_printoptions(threshold=sys.maxsize)
seconds = 0
while True:
    seconds += 1
    arr = np.zeros((HEIGHT, WIDTH), dtype=int)
    arr_final, new_ps = get_arr_after_seconds(arr, ps, vs, seconds=seconds)

    x_coords = new_ps[:, 0]
    symmetry_score = np.abs(x_coords - x_coords.mean()).mean()

    # Height width ratio of bounding box
    y_coords = new_ps[:, 1]
    height = y_coords.max() - y_coords.min()
    width = x_coords.max() - x_coords.min()
    height_width_ratio = height / width

    if seconds % 10000 == 0:
        print(f"Seconds: {seconds}, Symmetry score: {
            symmetry_score}, Height/Width ratio: {height_width_ratio}")

    if symmetry_score < SYMMETRY_THRESHOLD:
        print(f"Seconds: {seconds}")
        print(f"Seconds: {seconds}, Symmetry score: {
            symmetry_score}, Height/Width ratio: {height_width_ratio}")
        with open(f"output.txt", "w") as f:
            for row in arr_final:
                f.write(
                    "".join(map(lambda v: " " if v == 0 else str(v), row)) + "\n")
        next = input("Continue? (enter)")
        break

print(seconds)

# 108 is weird
# 209 is weird
# 310 is weird... I'm noticing a pattern here. (And 101 is the width... interesting)

# LOL 8087 is the answer, hit enter maybe 100 times while thinking
# While thinking, I've come to the conclusion that my next steps would be to narrow down
# the search space by looking for at least 5 consecutive elements in a left and right diagonal symmetric
# Ex:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# Because there were a weird pattern of veritcal 1's building up (every 101 seconds (width)), I thought that could be the base or something
# so, I planned to reduce my search space to that section and then perform those computations on every second's array
# to find a match. This would prevent manually clicking enter
