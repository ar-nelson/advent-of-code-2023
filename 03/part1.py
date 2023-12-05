#!/usr/bin/env python3

# Build a bitmask of adjacent-to-symbol coordinates,
# then compare the coordinates of each number against them.
#
# This uses a third-party library, to practice using pip and venv.

import re
from bitarray import bitarray

lines = []
with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        lines.append(line)

# The adjacency table is a list of bitarrays.
# To simplify the algorithm, it contains one cell of horizontal padding.
# So, to check (x, y), you must check adjacency[y][x + 1].

adjacency = []
for line in lines:
    if len(adjacency) == 0:
        adjacency.append(bitarray(len(line) + 2))
        adjacency.append(bitarray(len(line) + 2))
        adjacency[-1][:] = 0 # have to initialize these or they're garbage
        adjacency[-2][:] = 0
    adjacency.append(bitarray(len(line) + 2))
    adjacency[-1][:] = 0
    for i, c in enumerate(line):
        if c != "." and not c.isdigit():
            # Mark a 3x3 square as adjacent
            adjacency[-1][i:i+3] = 1
            adjacency[-2][i:i+3] = 1
            adjacency[-3][i:i+3] = 1
adjacency.pop() # chop off the top and bottom padding lines
adjacency.pop(0)

# Now, iterate numbers and find numbers overlapping the adjacency table

number_regex = re.compile(r"\d+")
total = 0
for y, line in enumerate(lines):
    for match in number_regex.finditer(line):
        if adjacency[y][match.start()+1:match.end()+1].any():
            total += int(match[0])

print(total)

