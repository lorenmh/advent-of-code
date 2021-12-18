#!/usr/local/bin/python3

import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir}/input', 'r') as f:
    input = f.read().splitlines()

movements = {
    'forward ': lambda x: [x, 0],
    'up ': lambda x: [0, -x],
    'down ': lambda x: [0, x],
}

position = [0, 0]

for line in input:
    x,y = position
    for s,movement in movements.items():
        if line.startswith(s):
            magnitude = int(line.split(s)[1])
            dx,dy = movement(magnitude)
            break
    x += dx
    y += dy
    position = [x, y]

print(position[0] * position[1])