#!/usr/bin/env python3

from bisect import insort, bisect
from math import inf
import re

class RangeMap:
    def __init__(self):
        self.ranges = []

    def add_range(self, dest_start, src_start, length):
        insort(self.ranges, (src_start, dest_start, length))

    def lookup(self, n):
        after_range = bisect(self.ranges, (n, inf, 0));
        if after_range == 0:
            return n
        src_start, dest_start, length = self.ranges[after_range - 1]
        offset = n - src_start
        if offset < length:
            return dest_start + offset
        else:
            return n

seeds = None
seed_to_soil = RangeMap()
soil_to_fertilizer = RangeMap()
fertilizer_to_water = RangeMap()
water_to_light = RangeMap()
light_to_temperature = RangeMap()
temperature_to_humidity = RangeMap()
humidity_to_location = RangeMap()

with open('input', 'r', encoding='UTF-8') as file:
    current = seed_to_soil
    while full_line := file.readline():
        line = full_line.rstrip()
        if line.startswith("seeds:"):
            seeds = [int(n) for n in re.split(r"\s+", line)[1:]]
        elif line.startswith("seed-to-soil"):
            current = seed_to_soil
        elif line.startswith("soil-to-fertilizer"):
            current = soil_to_fertilizer
        elif line.startswith("fertilizer-to-water"):
            current = fertilizer_to_water
        elif line.startswith("water-to-light"):
            current = water_to_light
        elif line.startswith("light-to-temperature"):
            current = light_to_temperature
        elif line.startswith("temperature-to-humidity"):
            current = temperature_to_humidity
        elif line.startswith("humidity-to-location"):
            current = humidity_to_location
        else:
            ns = re.split(r"\s+", line)
            if len(ns) >= 3:
                current.add_range(int(ns[0]), int(ns[1]), int(ns[2]))

# This is a brute force approach. It's not a real solution, but I left it to run
# overnight and it produced the right answer, so… 🤷‍♂️

least = inf
for start, length in zip(*(iter(seeds),) * 2):
    for seed in range(start, start + length):
        least = min(least, humidity_to_location.lookup(temperature_to_humidity.lookup(light_to_temperature.lookup(water_to_light.lookup(fertilizer_to_water.lookup(soil_to_fertilizer.lookup(seed_to_soil.lookup(seed))))))))
print(least)
