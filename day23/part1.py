from aocd import submit
from aoc.helpers import input_lines
from collections import defaultdict
from itertools import combinations


EX_FILE = "example.txt"
FILE = "input.txt"


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

adjacencies = defaultdict(set)

for line in lines:
    c1, c2 = line.split('-')
    adjacencies[c1].add(c2)
    adjacencies[c2].add(c1)

# Sets of 3 computers
s3 = set()
for node in adjacencies:
    neighbors = adjacencies[node]
    for a, b in combinations(neighbors, 2):
        if b in adjacencies[a]:
            s = tuple(sorted([node, a, b]))
            s3.add(s)

valid_sets = [s for s in s3 if any(c.startswith('t') for c in s)]

print("Answer:", len(valid_sets))