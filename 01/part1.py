#!/usr/bin/env python3

total = 0

with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline():
        digits = [c for c in line if c.isdigit()]
        total += int(digits[0] + digits[-1])

print(total)
