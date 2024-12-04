'''
### What I learned from this -- My Mistake ###
So it turns out, I misread the question. I wrongly interpreted the word search problem as one allowing snaking paths.
Because of this, I implemented a DFS and spent a while debugging it...
The correct solution is to simply search for the word XMAS in a straight line, not allowing snaking.
'''

steps = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def search(letter_arr, i, j, direction, remaining_letters="XMAS"):
    # Check bounds
    if i < 0 or j < 0 or i >= len(letter_arr[0]) or j >= len(letter_arr):
        return 0

    # Check letter
    if letter_arr[j][i] != remaining_letters[0]:
        return 0

    # Check if we've found the word
    if len(remaining_letters) == 1:
        return 1

    return search(letter_arr, i + direction[0], j + direction[1], direction, remaining_letters[1:])


raw_data = open('input.txt').read()
lines = raw_data.strip().splitlines()
letter_arr = [list(line) for line in lines]

total = 0
for j in range(len(letter_arr)):
    for i in range(len(letter_arr[0])):
        if letter_arr[j][i] == 'X':
            for direction in steps:
                total += search(letter_arr, i, j, direction)

print(total)
