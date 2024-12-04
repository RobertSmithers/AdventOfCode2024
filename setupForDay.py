from aocd import get_data, submit
from aoc.helpers import input_lines
import argparse
import os

parser = argparse.ArgumentParser(description='Advent of Code Day Setup')
parser.add_argument('day', type=int, help='Day of the Advent of Code')
args = parser.parse_args()

day = args.day

data = get_data(day=day, year=2024, block=True)

directory = f'day{day}'
if not os.path.exists(directory):
    os.makedirs(directory)

with open(os.path.join(directory, 'input.txt'), 'w') as f:
    f.write(data)
