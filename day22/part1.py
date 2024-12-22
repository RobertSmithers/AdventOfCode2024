from aocd import submit
from aoc.helpers import input_lines


EX_FILE = "example.txt"
FILE = "input.txt"


def mix(num, num2):
    return num ^ num2

def prune(num):
    return num % 16777216

def get_secret_number(num):
    v1 = prune(mix(num, num * 64))
    v2 = prune(mix(v1, v1 // 32))
    return prune(mix(v2, v2 * 2048))


raw_data = open(FILE, 'r').read()
lines = input_lines(raw_data)
NUM_SECRETS = 2000 

answer = 0
for line in lines:
    number = int(line.strip())
    val = number
    for i in range(NUM_SECRETS):
        val = get_secret_number(val)
    # print(number, val)
    answer += val

print(answer)
