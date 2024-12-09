from aocd import submit
from aoc.helpers import input_lines
import numpy as np
from typing import List


EX_FILE = "example.txt"
FILE = "input.txt"


def gimme_2d_arr_np(lines: List[str], dtype) -> np.ndarray:
    return np.array([list(line.strip()) for line in lines], dtype=dtype)


count = -1


def get_next_id():
    global count
    count += 1
    return count


def get_parsed_block(line):

    out_block = []
    for i, c in enumerate(line):
        if i % 2 == 0:
            next_block = [get_next_id()] * int(c)
            out_block.append(next_block)
        else:
            if c != "0":
                out_block.append(["."] * int(c))
    return out_block


def move_file_blocks(blocks):
    """
    Move files from the rightmost position to the leftmost free space large enough to fit the file.
    Process files in decreasing order of their ID, ensuring each file moves only once.
    """
    file_idx = len(blocks) - 1  # Start from the rightmost block

    while file_idx >= 0:
        current_block = blocks[file_idx]

        # If this is a free space block (not a file), skip it
        if "." in current_block:
            file_idx -= 1
            continue

        file_len = len(current_block)  # The size of the file to move

        # Try to find the leftmost space where this file can fit
        # Loop backwards from file_idx-1 to 0
        for free_idx in range(file_idx - 1, -1, -1):
            free_block = blocks[free_idx]

            if "." in free_block and len(free_block) >= file_len:
                # We found enough free space; move the file there
                blocks[free_idx] = current_block + free_block[file_len:]
                blocks[file_idx] = ["."] * file_len
                break  # Move the next file after this one is placed

        file_idx -= 1

    # Optionally, compact free spaces at the end of the list for cleaner output (not mandatory)
    compacted_blocks = []
    for block in blocks:
        if compacted_blocks and "." in block and "." in compacted_blocks[-1]:
            compacted_blocks[-1] += block  # Merge consecutive free blocks
        else:
            compacted_blocks.append(block)

    return compacted_blocks


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

moved = None
for i, line in enumerate(lines):
    parsed = get_parsed_block(line)
    moved = move_file_blocks(parsed)

flattened_moved = [item for sublist in moved for item in sublist]
total = 0
for i, c in enumerate(flattened_moved):
    if c != ".":
        total += i * int(c)
print(total)

# 6377400869326 correct answer
