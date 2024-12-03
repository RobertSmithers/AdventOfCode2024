# Also not optimal, but it was a challenge to finish it with dampening -- good practice for future problems
def is_valid(levels, dampen):
    if len(levels) <= 1:
        return True

    is_increasing = all(levels[i] > levels[i - 1] for i in range(1, len(levels)))
    is_decreasing = all(levels[i] < levels[i - 1] for i in range(1, len(levels)))

    if not (is_increasing or is_decreasing):
        if dampen > 0:
            for i in range(len(levels)):
                if is_valid(levels[:i] + levels[i + 1:], dampen-1):
                    return True
        return False

    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i-1])
        if diff < min_step or diff > max_step:
            if dampen > 0:
                for j in range(len(levels)):
                    if is_valid(levels[:j] + levels[j+1:], dampen-1):
                        return True
            return False
    return True

lines = open('input.txt').readlines()

total_safe = 0

min_step = 1
max_step = 3

for line in lines:
    line = line.strip()
    levels = list(map(int, line.split(" ")))

    if is_valid(levels, dampen=1):
        total_safe += 1

print("Total safe =", total_safe)