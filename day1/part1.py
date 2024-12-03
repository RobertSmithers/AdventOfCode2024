
lines = open('input.txt').readlines()

left = []
right = []

for line in lines:
    line = line.replace("\n", "")
    num1, num2 = tuple(map(int, line.split("   ")))
    left.append(num1)
    right.append(num2)

# Order
left.sort()
right.sort()

# Get min distance
print(sum(list(map(lambda vals: abs(vals[0] - vals[1]), zip(left, right)))))