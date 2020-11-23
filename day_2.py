""" Solution Day 2 Advent of code 2005 """

with open("input2", "r") as in_file:
    data = in_file.readlines()

total_paper = total_ribbon = 0

for x, item in enumerate(data):
    values = sorted(list(map(int, item.strip().split('x'))))

    total_paper += 2*(values[0]*values[1] + values[1]*values[2] + values[0]*values[2])
    total_paper += values[0]*values[1]

    total_ribbon += 2*values[0] + 2*values[1] + values[0]*values[1]*values[2]

print(f"Part 1: {total_paper}")
print(f"Part 2: {total_ribbon}")
