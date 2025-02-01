# CCC '18 S2

data = []

x = int(input())
for i in range(x):
    row = list(map(int, input().split()))
    data.append(row)

while True:
    # check if table is rotated properly by checking the rows
    # left to right and the columns top to bottom for an 
    # ascending order of values

    bad = False

    for row in data:
        if sorted(row) != row:
            bad = True
            break

    if not bad:
        for x in range(len(data[0])):
            col = []
            for i in range(len(data)):
                col.append(data[i][x])
            if sorted(col) != col:
                bad = True
                break
    
    if bad:
        # rotate data
        new_data = []
        for col in range(len(data) - 1, -1, -1):
            new_row = []
            for row in range(len(data[0])):
                new_row.append(data[row][col])
            new_data.append(new_row)
        data = new_data

    if not bad:
        # print data
        for row in data:
            row = list(map(str, row))
            print(' '.join(row))
        break