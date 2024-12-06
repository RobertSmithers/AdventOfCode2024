from aocd import get_data, submit
from aoc.helpers import input_lines
import argparse
import os

parser = argparse.ArgumentParser(description='Advent of Code Day Setup')
parser.add_argument('day', type=int, help='Day of the Advent of Code')
args = parser.parse_args()

day = args.day

directory = f'day{day}'
template_path_out = os.path.join(directory, 'part1.py')

if not os.path.exists(directory):
    os.makedirs(directory)

data = get_data(day=day, year=2024, block=True)

with open(os.path.join(directory, 'input.txt'), 'w') as f:
    f.write(data)

with open(os.path.join(directory, 'example.txt'), 'w') as f:
    pass


if os.path.exists('template.py') and not os.path.exists(template_path_out):
    with open('template.py', 'r') as src, open(template_path_out, 'w') as dst:
        dst.write(src.read())
