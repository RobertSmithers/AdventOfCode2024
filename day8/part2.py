import sys

EX_FILE = "example.txt"
FILE = "input.txt"

if len(sys.argv) > 1 and sys.argv[1] == '1':
    filename = EX_FILE
else:
    filename = FILE

raw_data = open(filename, 'r').read()
lines = raw_data.strip().splitlines()

arr = [list(line) for line in lines]
stored_antinodes = {}


def isInBounds(point):
    r, c = point
    return r >= 0 and c >= 0 and r < len(arr) and c < len(arr[0])


def addAntinodeOffset(target, p1, p2):
    tr, tc = target

    # Sanity check (I guess this means part 2 is "insane" :P)
    # assert (target not in [p1, p2])

    if target not in stored_antinodes:
        # Store antinodes with their src/dst antenna pairs (as set so order doesn't matter)
        stored_antinodes[target] = [{p1, p2}]
        # Update map with antinode
        if arr[tr][tc] == ".":
            arr[tr][tc] = "#"
        return 1

    # Did we already add this antinode from these antennae :)
    if ({p1, p2} in stored_antinodes[target]):
        return 0

    # Another antenna pair has already added this antinode, but we can too!
    stored_antinodes[target].append({p1, p2})

    # I NEED TO READ THE INSTRUCTIONS... this is what I failed to recognize
    # How many *unique* locations... this 1 number costed so much
    return 0


def drawAntinodeOffsetsLinear(p1, p2):
    diff = (p2[0] - p1[0], p2[1] - p1[1])
    counter = 0

    # p1.row is <= p2.row (since we traverse top down)
    curr_step = 0   # NOTE: This is the tricky change -- since it's linear, each antenna counts as a valid frequency, so we start at 0
    p1target = (p1[0] - curr_step * diff[0], p1[1] - curr_step * diff[1])
    while isInBounds(p1target):
        counter += addAntinodeOffset(p1target, p1, p2)
        p1target = (p1[0] - curr_step * diff[0], p1[1] - curr_step * diff[1])
        curr_step += 1

    # p2.row is >= p1.row, so we always add diff to p2
    curr_step = 0   # NOTE: This is the tricky change -- see above
    p2target = (p2[0] + curr_step * diff[0], p2[1] + curr_step * diff[1])
    while isInBounds(p2target):
        counter += addAntinodeOffset(p2target, p1, p2)
        p2target = (p2[0] + curr_step * diff[0], p2[1] + curr_step * diff[1])
        curr_step += 1

    return counter


def add_antinodes(r, c):
    total = 0
    curr_antinode = arr[r][c]
    for r2 in range(len(arr)):
        for c2 in range(len(arr[0])):
            if (r2, c2) == (r, c):
                continue
            # Match antinodes
            if arr[r2][c2] == curr_antinode:
                total += drawAntinodeOffsetsLinear((r, c), (r2, c2))
    return total


answer = 0
for r in range(len(arr)):
    for c in range(len(arr[0])):
        if arr[r][c] in ["#", "."]:
            continue
        answer += add_antinodes(r, c)

print(f"Total antinodes: {answer}")
print(f"Recursive total isn't even needed... {len(stored_antinodes)}")
