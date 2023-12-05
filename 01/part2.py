#!/usr/bin/env python3

import re

# The naive solution is to just use a regex for digits and use re.findall().
# But that doesn't work, because digits can overlap!
# A separate regex for "first digit" and "last digit" works, though.
first_digit = re.compile(r"^.*?(\d|one|two|three|four|five|six|seven|eight|nine).*$")
last_digit = re.compile(r"^.*(\d|one|two|three|four|five|six|seven|eight|nine).*?$")

def parse_digit(n):
    if n == "one":
        return "1"
    elif n == "two":
        return "2"
    elif n == "three":
        return "3"
    elif n == "four":
        return "4"
    elif n == "five":
        return "5"
    elif n == "six":
        return "6"
    elif n == "seven":
        return "7"
    elif n == "eight":
        return "8"
    elif n == "nine":
        return "9"
    else:
        return n

total = 0

with open('input', 'r', encoding='UTF-8') as file:
    while line := file.readline().rstrip():
        first = first_digit.fullmatch(line)
        last = last_digit.fullmatch(line)
        total += int(parse_digit(first[1]) + parse_digit(last[1]))

print(total)
