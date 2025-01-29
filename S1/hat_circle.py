# CCC '24 S1
x = int(input())
seats = []
for i in range(x):
    seats.append(int(input()))

# print(seats)
count = 0


for index in range(len(seats)):
    opposite = index + (len(seats) // 2)
    if opposite >= len(seats):
        opposite -= len(seats)
    if seats[index] == seats[opposite]:
        count += 1

print(count)