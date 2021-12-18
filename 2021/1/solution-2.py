#!/usr/local/bin/python3

import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir}/input', 'r') as f:
    input = f.read().splitlines()

input = list(map(int, input))

counter = 0
sliding_window = sum(input[:3])
for i, line in enumerate(input[3:]):
    new_window = sliding_window - input[i] + input[3 + i]
    if new_window > sliding_window:
        counter += 1
    sliding_window = new_window

print(counter)