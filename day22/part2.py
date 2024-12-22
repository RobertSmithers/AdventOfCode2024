from aocd import submit
from aoc.helpers import input_lines
from collections import defaultdict, deque


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
all_seqs = defaultdict(int)
for line in lines:
    number = int(line.strip())
    val = number
    last_price = int(str(number)[-1])
    # The idea I am going for is that we will have a sliding window of size 4
    # we continue to add that sequence to the dict of all_seqs to get what the profit would be
    # then we need to mark it as 'visited' in the set because it would be first time we sell
    already_sold = set()
    curr_seq = deque(maxlen=4)
    for i in range(NUM_SECRETS):
        val = get_secret_number(val)
        # Get first digit of num
        price = int(str(val)[-1])

        diff = price - last_price
        curr_seq.append(diff)
        if len(curr_seq) == 4 and tuple(curr_seq) not in already_sold:
            # Valid window and we didn't sell yet
            # Sell now and add to our seq counter
            all_seqs[tuple(curr_seq)] += price
            already_sold.add(tuple(curr_seq))

        last_price = price 

print(max(all_seqs.values()))