#!/usr/local/bin/python3

import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir}/input', 'r') as f:
    input = f.read().splitlines()

def forward(x, aim):
    return [x, aim * x], aim

def up(x, aim):
    return [0, 0], aim - x

def down(x, aim):
    return [0, 0], aim + x

movements = {
    'forward ': forward,
    'up ': up,
    'down ': down,
}

position = [0, 0]
aim = 0

for line in input:
    x,y = position
    for s,movement in movements.items():
        if line.startswith(s):
            magnitude = int(line.split(s)[1])
            [dx,dy],new_aim = movement(magnitude, aim)
            break
    x += dx
    y += dy
    position = [x, y]
    aim = new_aim

print(position[0] * position[1])