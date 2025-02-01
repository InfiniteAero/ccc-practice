# CCC '23 S1
x = int(input())
rows = []
rows.append(list(map(int, input().split())))
rows.append(list(map(int, input().split())))

length = 0

for row in range(len(rows)):
    if row == 0: other_row = 1
    else: other_row = 0

    for triangle in range(len(rows[row])):
        potential_length = 3
        if rows[row][triangle] == 1:
            if triangle != 0:
                if rows[row][triangle - 1] == 1:
                    potential_length -= 1
            if triangle != x - 1:
                if rows[row][triangle + 1] == 1:
                    potential_length -= 1
            if triangle % 2 == 0:
                if rows[other_row][triangle] == 1:
                    potential_length -= 1

            length += potential_length

print(length)