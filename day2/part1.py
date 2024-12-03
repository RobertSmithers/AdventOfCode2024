# Definitely not the optimal way to do this... will come back to this later
def is_valid(levels):
    is_increasing = levels[1] > levels[0]

    last_level = levels[0]
    for level in levels[1:]:
        diff = level - last_level
        if diff < 0 and is_increasing:
            return False

        if diff > 0 and not is_increasing:
            return False
        
        if abs(diff) < min_step or abs(diff) > max_step:
            return False
        last_level = level
    return True

lines = open('input.txt').readlines()

total_safe = 0

min_step = 1
max_step = 3

for line in lines:
    line = line.replace("\n", "")
    levels = list(map(int, line.split(" ")))

    if is_valid(levels):
        total_safe += 1

print("Total safe =", total_safe)