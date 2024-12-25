from typing import List


def calculate_heights(lines, is_key):
    check = "." if is_key == "lock" else "#"
    heights = [-1 for _ in range(len(lines[0]))]

    for line in lines:
        for i, c in enumerate(line):
            if c == check:
                heights[i] += 1
    return heights


def is_overlapping(lock_heights, key_heights):
    valid_height = len(lock_heights)
    return any(lh + kh > valid_height for lh, kh in zip(lock_heights, key_heights))


def parse_input(lines: List[str]):
    locks, keys, curr = [], [], []
    for line in lines:
        if line.strip() == "":
            if curr:
                (locks if curr[0].startswith("#") else keys).append(curr)
            curr = []
        else:
            curr.append(line)
    if curr:
        (locks if curr[0].startswith("#") else keys).append(curr)
    return locks, keys


EX_FILE = "example.txt"
FILE = "input.txt"
with open(FILE, 'r') as file:
    raw_data = file.readlines()

locks, keys = parse_input(raw_data)

lock_heights = [calculate_heights(lock, is_key=False) for lock in locks]
key_heights = [calculate_heights(key, is_key=True) for key in keys]

answer = sum(
    not is_overlapping(lock, key)
    for lock in lock_heights
    for key in key_heights
)

print(answer)
