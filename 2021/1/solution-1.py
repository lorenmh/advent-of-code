#!/usr/local/bin/python3

import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir}/input', 'r') as f:
    input = f.read().splitlines()

prev = None
counter = 0
for line in input:
    value = int(line)
    if prev is not None:
        if value > prev:
            counter += 1
    prev = value

print(counter)