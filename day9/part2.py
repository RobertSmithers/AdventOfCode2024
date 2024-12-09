from aocd import submit
from aoc.helpers import input_lines
from itertools import count


EX_FILE = "example.txt"
FILE = "input.txt"


id_gen = count()


def get_parsed_block(line):

    out_block = []
    for i, c in enumerate(line):
        if i % 2 == 0:
            next_block = [next(id_gen)] * int(c)
            out_block.append(next_block)
        else:
            if c != "0":
                out_block.append(["."] * int(c))
    return out_block


def move_file_blocks(li):
    p1 = 0
    p2 = len(li) - 1

    while p2 > 0:
        if p1 > p2:
            p1 = 0
            p2 -= 1
            continue
        if "." not in li[p1]:
            p1 += 1
            continue
        if "." in li[p2]:
            p2 -= 1
            continue

        free_len = len(li[p1])
        num_len = len(li[p2])

        if free_len == num_len:
            li[p1], li[p2] = li[p2], li[p1]
            p2 -= 1
            p1 = 0
        elif free_len > num_len:
            li[p1] = li[p2]
            li[p2] = ["."] * num_len
            p1 += 1
            li.insert(p1, ["."] * (free_len - num_len))
            if p1 > 0 and "." in li[p1 - 1]:
                li[p1] = li[p1 - 1] + li[p1]
                li.pop(p1 - 1)
                p2 -= 1
            while p1 < len(li) - 1 and "." in li[p1 + 1]:
                li[p1] = li[p1] + li[p1 + 1]
                li.pop(p1 + 1)
                p2 -= 1
            p1 = 0
        else:
            p1 += 1

    return li


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)

moved = None
for i, line in enumerate(lines):
    parsed = get_parsed_block(line)
    moved = move_file_blocks(parsed)

flattened = [item for sublist in moved for item in sublist]
result = sum(index * int(value)
             for index, value in enumerate(flattened) if value != ".")
print(result)

# 6377400869326 correct answer
