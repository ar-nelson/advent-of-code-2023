#!/usr/bin/env python3

# No bitarrays for this one, it's all list comprehensions.

import re

lines = []
with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        lines.append(line)

stars_re = re.compile("[*]")
numbers_re = re.compile(r"\d+")

stars = ((m.start(), y) for y, line in enumerate(lines) for m in stars_re.finditer(line))
numbers = [(m.start(), m.end(), y, int(m[0])) for y, line in enumerate(lines) for m in numbers_re.finditer(line)]
adjacent_numbers = ([n for nx0, nx1, ny, n in numbers if sx in range(nx0-1,nx1+1) and sy in range(ny-1,ny+2)] for (sx, sy) in stars)
gears = ((ns[0], ns[1]) for ns in adjacent_numbers if len(ns) == 2)

total = 0
for (a, b) in gears:
    total += a * b
print(total)
