# CCC '18 S2

data = []

x = int(input())
for i in range(x):
    row = list(map(int, input().split()))
    data.append(row)

# print(data)

fine = False

while not fine:
    # check if table is rotated properly by checking the rows
    # left to right and the columns top to bottom for an 
    # ascending order of values
    