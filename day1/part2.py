lines = open('input.txt').readlines()

left = []
right = []

for line in lines:
    line = line.replace("\n", "")
    num1, num2 = tuple(map(int, line.split("   ")))
    left.append(num1)
    right.append(num2)

# Order (no longer necessary, but keeping it for simplicity)
left.sort()
right.sort()

similarity = 0
for num in left:
    similarity += num * right.count(num)

print(similarity)