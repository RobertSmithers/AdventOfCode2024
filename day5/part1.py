raw_data = open('input.txt').read()
lines = raw_data.strip().splitlines()

order_map = {}


def isOrdered(page_nums):
    for i in range(len(page_nums)):
        page_num = int(page_nums[i])
        for other_nums in page_nums[i+1:]:
            other_num = int(other_nums)
            # Check that page_num before other_num is valid
            if page_num in order_map and other_num in order_map[page_num]:
                continue
            elif other_num in order_map and page_num in order_map[other_num]:
                # Invalid -- this num should be before page_num
                return False
    return True


total = 0

# Load orders
c = 0
for line in lines:
    if line == '':
        break
    X, Y = tuple(map(int, line.split('|')))
    if X in order_map:
        order_map[X].append(Y)
    else:
        order_map[X] = [Y]
    c += 1

# Load page tests
for line in lines[c+1:]:
    split_line = list(map(int, line.split(',')))
    if isOrdered(split_line):
        total += split_line[len(split_line)//2]

print(total)
