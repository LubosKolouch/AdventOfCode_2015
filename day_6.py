#!/bin/env python
""" Day 6 Year 2015 """

grid = {}
grid_part2 = {}

with open("input6", "r") as in_file:
    for line in in_file:
        instr = line.strip().split(' ')

        if instr[0] == 'toggle':
            start_x, start_y = list(map(int, instr[1].split(",")))
            end_x, end_y = list(map(int, instr[3].split(",")))

            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    grid[(i, j)] = 0 if grid.get((i, j), 0) else 1
                    grid_part2[(i, j)] = grid_part2.get((i, j), 0)+2
        else:
            start_x, start_y = list(map(int, instr[2].split(",")))
            end_x, end_y = list(map(int, instr[4].split(",")))

            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    if instr[1] == 'off':
                        grid[(i, j)] = 0
                        grid_part2[(i, j)] = max(0, grid_part2.get((i, j), 0)-1)
                    else:
                        grid[(i, j)] = 1
                        grid_part2[(i, j)] = grid_part2.get((i, j), 0)+1

total_lights = 0

for v in grid.values():
    total_lights += v

print(f"Part 1: {total_lights}")

total_lights = 0

for v in grid_part2.values():
    total_lights += v

print(f"Part 2: {total_lights}")



