#!/usr/bin/env python3

import re
game = re.compile("^Game (\d+):")
handful = re.compile("(\d+) (red|green|blue)(?:, (\d+) (red|green|blue)(?:, (\d+) (red|green|blue))?)?")

total = 0

max_cubes = { "red": 12, "green": 13, "blue": 14 }

with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        g = game.match(line)
        id = int(g[1])
        valid = True
        for h in handful.finditer(line):
            for (cubes, color) in [(h[1], h[2]), (h[3], h[4]), (h[5], h[6])]:
                if cubes is not None and int(cubes) > max_cubes[color]:
                    valid = False
            if not valid:
                break
        if valid:
            total += id

print(total)
