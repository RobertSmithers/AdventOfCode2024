raw_data = open('input.txt').read()
lines = raw_data.strip().splitlines()

steps = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}


def rotate_90(direction):
    if direction == 'up':
        return 'right'
    if direction == 'right':
        return 'down'
    if direction == 'down':
        return 'left'
    if direction == 'left':
        return 'up'


def isInBounds(arr, i, j):
    return i >= 0 and j >= 0 and i < len(arr[0]) and j < len(arr)


def doesGuardLoop(arr, i, j, direction="up"):
    while isInBounds(arr, i, j) and arr[j][i] != '#':
        dx, dy = steps[direction]
        i += dx
        j += dy
    if isInBounds(arr, i, j) and arr[j][i] == '#':
        # Check if we've been here before (loop)
        if (i, j, direction) in loop_cache:
            return True
        # Otherwise we add it
        loop_cache.add((i, j, direction))
        return doesGuardLoop(arr, i - dx, j - dy, rotate_90(direction))
    return False


# Load/parse
arr = [list(line) for line in lines]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[j][i] == '^':
            start_coord = (i, j)
            break

# Solve
total = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[j][i] in ['#', '^']:
            continue

        # Check if we loop when we add a wall here
        # Not an efficient solution by any means, but still not too slow (yet)
        arr[j][i] = "#"
        loop_cache = set()
        if doesGuardLoop(arr, start_coord[0], start_coord[1]):
            total += 1
        arr[j][i] = "."

print("Unique time paradoxes", total)
