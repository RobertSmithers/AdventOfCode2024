from aocd import get_data
import argparse
import os
import time

parser = argparse.ArgumentParser(description='Advent of Code Day Setup')
parser.add_argument('day', type=int, help='Day of the Advent of Code')
args = parser.parse_args()

day = args.day

directory = f'day{day}'
template_path_out = os.path.join(directory, 'part1.py')

if not os.path.exists(directory):
    os.makedirs(directory)

if os.path.exists('template.py') and not os.path.exists(template_path_out):
    with open('template.py', 'r') as src, open(template_path_out, 'w') as dst:
        dst.write(src.read())

with open(os.path.join(directory, 'example.txt'), 'w') as f:
    pass

try:
    data = get_data(day=day, year=2024, block=True)
    with open(os.path.join(directory, 'input.txt'), 'w') as f:
        f.write(data)
except KeyboardInterrupt:
    print('\nExiting...')
except Exception as e:
    # Catch the time-based failure and repull
    time.sleep(1)
    data = get_data(day=day, year=2024, block=True)
    with open(os.path.join(directory, 'input.txt'), 'w') as f:
        f.write(data)
