#!/usr/bin/env python3

import re

line_re = re.compile(r"Card\s+(\d+):\s*([\d\s]+)\s*\|\s*([\d\s]+)\s*")

card_copies = [0]
total = 0

with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        match = line_re.fullmatch(line)
        card_ix = int(match[1])
        while len(card_copies) <= card_ix:
            card_copies.append(1)
        copies = card_copies[card_ix]
        winning_numbers = frozenset((int(n) for n in re.split(r"\s+", match[3])))
        matching_numbers = sum((1 for n in re.split(r"\s+", match[2]) if n != "" and int(n) in winning_numbers), 0)
        for next_ix in range(card_ix + 1, card_ix + 1 + matching_numbers):
            while len(card_copies) <= next_ix:
                card_copies.append(1)
            card_copies[next_ix] += copies
        total += copies

print(total)
