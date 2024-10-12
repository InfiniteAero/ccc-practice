# CCC '05 J4

import math

outline_width = int(input())
outline_height = int(input())
cutout_width = int(input())
cutout_height = int(input())
steps = int(input())

# 0 - unwalkable tile
# 1 - walkable tile

# define cross
grid = []
row = []
# top border
row += (outline_width + 2) * [0]
grid.append(row)
# rows with cutouts
for i in range(cutout_height):
    row = []
    for j in range(cutout_width + 1):
        row.append(0)
    for j in range(outline_width - (2 * cutout_width)):
        row.append(1)
    for j in range(cutout_width + 1):
        row.append(0)
    grid.append(row)
# rows without cutout
for i in range(outline_height - (2 * cutout_height)):
    row = []
    row.append(0)
    row += outline_width * [1]
    row.append(0)
    grid.append(row)
# rows with cutouts
for i in range(cutout_height):
    row = []
    for j in range(cutout_width + 1):
        row.append(0)
    for j in range(outline_width - (2 * cutout_width)):
        row.append(1)
    for j in range(cutout_width + 1):
        row.append(0)
    grid.append(row)
# bottom border
row = (outline_width + 2) * [0]
grid.append(row)


# debugging only
#for i in range(len(grid)):
#    print(grid[i])


current_pos = [1,cutout_width + 1]

# check each direction, move in the direction that's first available
# move priority: right, down, left, up (right half of grid)
#                left, up, right, dowm (left half of grid)
count = 0
while True:
    if count == steps:
        break
    # check if right half of grid
    if current_pos[1] > math.floor(outline_width/2):
        # check right
        if grid[current_pos[0]][current_pos[1] + 1] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0], current_pos[1] + 1]
        # check down
        elif grid[current_pos[0] + 1][current_pos[1]] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0] + 1, current_pos[1]]
        # check left
        elif grid[current_pos[0]][current_pos[1] - 1] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0], current_pos[1] - 1]
        # check up
        elif grid[current_pos[0] - 1][current_pos[1]] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0] - 1, current_pos[1]]
        else: break
        count += 1
    else:
        # check left
        if grid[current_pos[0]][current_pos[1] - 1] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0], current_pos[1] - 1]
        # check up
        elif grid[current_pos[0] - 1][current_pos[1]] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0] - 1, current_pos[1]]
        # check right
        elif grid[current_pos[0]][current_pos[1] + 1] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0], current_pos[1] + 1]
        # check down
        elif grid[current_pos[0] + 1][current_pos[1]] == 1:
            grid[current_pos[0]][current_pos[1]] = 0
            current_pos = [current_pos[0] + 1, current_pos[1]]
        else: break
        count += 1

print(str(current_pos[1]) + "\n" + str(current_pos[0]))