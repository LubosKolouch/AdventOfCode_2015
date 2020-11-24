#!/bin/env python
""" Day 4 Year 2015 """

import hashlib

input_str = 'iwrupvqb'

i = 0
while 1:
    i += 1
    test_str = input_str + str(i)
    hexd = hashlib.md5(test_str.encode()).hexdigest()
    if hexd.startswith('00000'):
        print(f"Part 1: {i}")

        if hexd.startswith('000000'):
            print(f"Part 2: {i}")
            break
