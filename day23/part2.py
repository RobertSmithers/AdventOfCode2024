from aocd import submit
from aoc.helpers import input_lines
from collections import defaultdict

EX_FILE = "example.txt"
FILE = "input.txt"

raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

adjacencies = defaultdict(set)

answer = 0
for line in lines:
    c1, c2 = line.split('-')
    adjacencies[c1].add(c2)
    adjacencies[c2].add(c1)

# Courtesy of https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def bron_kerbosch(potential_clique, candidates, excluded, graph):
    if not candidates and not excluded:
        yield potential_clique
        return
    
    pivot = next(iter(candidates | excluded))
    for node in candidates - graph[pivot]:
        # Add node to potential_clique, limit candidates and excluded to those
        # shared with this node's neighbors (otherwise violates clique definition -- fully connected)
        yield from bron_kerbosch(
            potential_clique | {node},  
            candidates & graph[node],
            excluded & graph[node],
            graph,
        )
        candidates.remove(node)
        excluded.add(node)

    
# the maximum possible size is bounded by the largest adjacency list size plus one (for source)
# this drastically reduces the search space, but still isn't optimal
# Graph theory to the rescue! The famous bron-kerbosch algorithm is the perfect solution 
# (by famous I mean I had no clue what this was until I google searched graph theory applications for identifying max fully-connected groupings AKA cliques)

all_cliques = list(bron_kerbosch(set(), set(adjacencies.keys()), set(), adjacencies))

largest_clique = max(all_cliques, key=len)
password = ",".join(sorted(largest_clique))

print("Password:", password)