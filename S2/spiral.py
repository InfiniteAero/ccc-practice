start_num = int(input())
end_num = int(input())

# create grid
grid = []
for i in range(11):
    row = 11 * ["  "]
    grid.append(row)

pos = [4, 4]

# tracks the distance to move and if we should increase the distance
current_dir = "DOWN"
steps = 1
dir_count = 0

current_num = start_num
grid[pos[0]][pos[1]] = current_num

while current_num < end_num:
    # repeat by number of steps needed to move
    for i in range(steps):
        current_num += 1
        if current_dir == "DOWN":
            pos[0] += 1
        elif current_dir == "UP":
            pos[0] -= 1
        elif current_dir == "LEFT":
            pos[1] -= 1
        elif current_dir == "RIGHT":
            pos[1] += 1
        grid[pos[0]][pos[1]] = current_num
        # stop printing numbers right now!!!
        if current_num == end_num:
            break

    # update move variables
    if current_dir == "DOWN":
        current_dir = "RIGHT"
    elif current_dir == "RIGHT":
        current_dir = "UP"
    elif current_dir == "UP":
        current_dir = "LEFT"
    elif current_dir == "LEFT":
        current_dir = "DOWN"
    
    dir_count += 1
    if dir_count == 2:
        dir_count = 0
        steps += 1

for row in grid:
    for char in row:
        if len(str(char)) == 1:
            char = ' ' + str(char)
        print(str(char) + ' ', end='')
    print('\n', end='')
    