diag_left = [
    (1, 1),    # Diagonal Down-Right
    (-1, -1)   # Diagonal Up-Left
]

diag_right = [
    (-1, 1),   # Diagonal Up-Right
    (1, -1)    # Diagonal Down-Left
]


def is_in_bounds(letter_arr, i, j):
    return i >= 0 and j >= 0 and i < len(letter_arr[0]) and j < len(letter_arr)


def check_for_xmas(letter_arr, i, j):
    # Only look at the A (middle) and draw an X from there
    if letter_arr[j][i] != 'A':
        return False

    def check_diagonal(diagonal_dirs):
        missing_chars = {'M', 'S'}
        for dx, dy in diagonal_dirs:
            if not is_in_bounds(letter_arr, i + dx, j + dy):
                return False

            if letter_arr[j + dy][i + dx] not in missing_chars:
                return False

            missing_chars.remove(letter_arr[j + dy][i + dx])
        return not missing_chars

    return check_diagonal(diag_left) and check_diagonal(diag_right)


# Load data into lines
raw_data = open('input.txt').read()
lines = raw_data.strip().splitlines()
letter_arr = [list(line) for line in lines]

total = 0
for j in range(len(letter_arr)):
    for i in range(len(letter_arr[0])):
        if check_for_xmas(letter_arr, i, j):
            total += 1
print(f"Total occurrences: {total}")
