_in = input()
_in = _in.split()
day = int(_in[0]) - 1
day_count = int(_in[1])

grid = []
for i in range(5):
    row = 7 * ["   "]
    grid.append(row)

pos = [0, day]
cur_day = 1

while cur_day <= day_count:
    if cur_day <= 9:
        cur_day = '  ' + str(cur_day)
    else:
        cur_day = ' ' + str(cur_day)

    try:
        grid[pos[0]][pos[1]] = cur_day
    except IndexError:
        try:
            pos[0] += 1
            pos[1] = 0
            grid[pos[0]][pos[1]] = cur_day
        except IndexError:
            row = 7 * ["   "]
            grid.append(row)
            grid[pos[0]][pos[1]] = cur_day
    
    pos[1] += 1
    cur_day = int(cur_day)
    cur_day += 1

print("Sun Mon Tue Wed Thr Fri Sat")
calendar = ""
for i in grid:
    calendar += ' '.join(i) + '\n'

calendar = calendar.rstrip()
print(calendar)