#!/usr/bin/env python3

import re
game = re.compile("^Game (\d+):")
handful = re.compile("(\d+) (red|green|blue)(?:, (\d+) (red|green|blue)(?:, (\d+) (red|green|blue))?)?")

total = 0

with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        g = game.match(line)
        id = int(g[1])
        max_cubes = { "red": 0, "green": 0, "blue": 0 }
        for h in handful.finditer(line):
            for (cubes, color) in [(h[1], h[2]), (h[3], h[4]), (h[5], h[6])]:
                if cubes is not None:
                    max_cubes[color] = max(int(cubes), max_cubes[color])
        total += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

print(total)
