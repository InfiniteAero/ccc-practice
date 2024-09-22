# this is the most big-brain code I've ever written
# took five minutes to think up anyway
import math

list_points = []
while True:
    r = int(input())
    points = 1
    if r != 0:
        for i in range(-r, r):
            y = math.floor(math.sqrt((r**2) - (abs(i) ** 2)))
            points += y * 2 + 1
    else: break
    list_points.append(points)

for point in list_points:
    print(point)
