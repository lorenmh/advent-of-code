#!/usr/local/bin/python3

import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir}/input', 'r') as f:
    input = f.read().splitlines()

for line in input:
    pass
