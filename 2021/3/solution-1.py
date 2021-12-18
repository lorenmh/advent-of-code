#!/usr/local/bin/python3

import math
import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir}/input', 'r') as f:
    input = f.read().splitlines()

counts = list(map(int, input[0]))

for line in input[1:]:
    for i,c in enumerate(line):
        counts[i] += int(c)

input_midpoint = math.ceil(len(input) / 2)

gamma_bits = ['1' if x>=input_midpoint else '0' for x in counts]
epsilon_bits = ['0' if x>=input_midpoint else '1' for x in counts]

gamma = int(''.join(gamma_bits), 2)
epsilon = int(''.join(epsilon_bits), 2)

print(gamma * epsilon)