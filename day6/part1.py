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


def drawGuardPath(arr, i, j, direction="up"):
    unique_steps = 0
    while isInBounds(arr, i, j) and arr[j][i] != '#':
        if arr[j][i] != 'X':
            unique_steps += 1
            arr[j][i] = 'X'
        dx, dy = steps[direction]
        i += dx
        j += dy
    # Now we either hit a wall or left the "map"
    if isInBounds(arr, i, j) and arr[j][i] == '#':
        return unique_steps + drawGuardPath(arr, i - dx, j - dy, rotate_90(direction))

    return unique_steps


# Solve
arr = [list(line) for line in lines]
answer = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[j][i] == '^':
            answer = drawGuardPath(arr, i, j)

print("Num unique steps", answer)
