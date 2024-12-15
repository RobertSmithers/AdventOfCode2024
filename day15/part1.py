from aocd import submit
from aoc.helpers import input_lines
import numpy as np

EX_FILE = "example.txt"
FILE = "input.txt"


def get_starting_pos(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '@':
                return (x, y)
    return None


def can_move_o(warehouse, x, y, dir):
    dx, dy = dir
    if warehouse[y + dy][x + dx] == 'O':
        return can_move_o(warehouse, x + dx, y + dy, dir)
    elif warehouse[y + dy][x + dx] == '.':
        return True
    elif warehouse[y + dy][x + dx] == '#':
        return False
    print("ERROR: Unknown move condition?")
    return False


def move_o(warehouse, x, y, dir):
    dx, dy = dir
    box_new_x, box_new_y = x + dx, y + dy
    if warehouse[box_new_y][box_new_x] == '.':
        warehouse[y][x] = '.'
        warehouse[box_new_y][box_new_x] = 'O'
    elif warehouse[box_new_y][box_new_x] == 'O':
        move_o(warehouse, box_new_x, box_new_y, dir)
        warehouse[y][x] = '.'
        warehouse[box_new_y][box_new_x] = 'O'
    return warehouse


def move_robot(warehouse, robot_pos, moves):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    for move in moves:
        dx, dy = directions[move]
        new_x, new_y = robot_pos[0] + dx, robot_pos[1] + dy
        if warehouse[new_y][new_x] == '.':
            warehouse[robot_pos[1]][robot_pos[0]] = '.'
            robot_pos = (new_x, new_y)
            warehouse[new_y][new_x] = '@'
        elif warehouse[new_y][new_x] == 'O' and can_move_o(warehouse, new_x, new_y, (dx, dy)):
            warehouse[robot_pos[1]][robot_pos[0]] = '.'
            warehouse = move_o(warehouse, new_x, new_y, (dx, dy))
            robot_pos = (new_x, new_y)
            warehouse[new_y][new_x] = '@'

    return warehouse, robot_pos


def calculate_gps_sum(warehouse):
    gps_sum = 0
    for y, row in enumerate(warehouse):
        for x, char in enumerate(row):
            if char == 'O':
                gps_sum += 100 * y + x
    return gps_sum


# Load and parse
raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)
line = lines[0]

grid_lines = []
while line.startswith('#') and line.endswith('#'):
    grid_lines.append(list(line))
    lines.pop(0)
    line = lines[0]

grid_lines = np.array(grid_lines)

moves = []
for line in lines:
    if not line:
        continue
    line = line.strip()

    moves += list(line)

robot_pos = get_starting_pos(grid_lines)
new_grid, new_pos = move_robot(grid_lines, robot_pos, moves)
gps_sum = calculate_gps_sum(new_grid)

print(gps_sum)
# submit(gps_sum)
