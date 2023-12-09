#!/usr/bin/env python3

import re

line_re = re.compile(r"Card\s+(\d+):\s*([\d\s]+)\s*\|\s*([\d\s]+)\s*")

total = 0

with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        match = line_re.fullmatch(line)
        winning_numbers = frozenset((int(n) for n in re.split(r"\s+", match[3])))
        card_value = 0
        for my_number in re.split(r"\s+", match[2]):
            if my_number == "":
                continue
            if int(my_number) in winning_numbers:
                card_value += card_value if card_value > 0 else 1
        total += card_value

print(total)


