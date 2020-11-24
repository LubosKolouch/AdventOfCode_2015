#!/bin/env python
""" Day 5 Year 2015 """
import re

nice_strings = 0

with open("input5", "r") as in_file:
    for line in in_file:
        if not re.search(r'[aeiou].*?[aeiou].*?[aeiou]', line):
            continue

        if not re.search(r'(.)\1', line):
            continue

        if re.search(r'(ab|cd|pq|xy)', line):
            continue

        nice_strings += 1

print(f"Part 1: {nice_strings}")

nice_strings = 0
with open("input5", "r") as in_file:
    for line in in_file:
        if not re.search(r'(..).*\1', line):
            continue

        if not re.search(r'(.).\1', line):
            continue

        nice_strings += 1

print(f"Part 2: {nice_strings}")
