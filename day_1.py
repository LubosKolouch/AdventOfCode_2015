#!/bin/env python
""" Solution Day 1 Advent of code 2005 """

with open("input1", "r") as in_file:
    data = in_file.read()

santa_level = 0
for x, item in enumerate(data):
    if item == "(":
        santa_level += 1
    else:
        santa_level -= 1

    if santa_level == -1:
        print(f"Part Two: {x+1}")

print(f"Part One: {santa_level}")
