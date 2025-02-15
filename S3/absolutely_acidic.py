# CCC '12 S3

# create dictionary and gather data
freqs = {}

n = int(input())
for i in range(n):
    reading = int(input())
    if reading not in freqs.keys():
        freqs[reading] = 1
    else: freqs[reading] += 1

num_max = []
num_next_max = []
max = float("-inf")
next_max = float("-inf")

# find max
for reading in freqs:
    if freqs[reading] > max:
        max = freqs[reading]
# find second max
for reading in freqs:
    if freqs[reading] > next_max and freqs[reading] < max:
        next_max = freqs[reading]

# gather all readings of max and second max
for reading in freqs:
    if freqs[reading] == max:
        num_max.append(reading)
    elif freqs[reading] == next_max:
        num_next_max.append(reading)

# case 1: more than one max number
if len(num_max) > 1:
    diff = float("-inf")
    for i in num_max:
        for j in num_max:
            potential_diff = abs(i - j)
            if potential_diff > diff:
                diff = potential_diff
# case 2: only 1 max number
elif len(num_max) == 1:
    diff = float("-inf")
    # case 2.1: only one largest freq and one second largest freq
    if len(num_next_max) == 1:
        diff = abs(num_max[0] - num_next_max[0])
    # case 2.2: more than one second largest freq
    elif len(num_next_max) > 1:
        for i in num_next_max:
            potential_diff = abs(num_max[0] - i)
            if potential_diff > diff:
                diff = potential_diff

print(diff)


# old code to count first and second maximums
"""
first = float("-inf")
second = float("-inf")
first_count = 0
second_count = 0
for key in freqs:
    if freqs[key] > first:
        first = freqs[key]
        first_count = 1
    elif freqs[key] == first:
        first_count += 1
for key in freqs:
    if freqs[key] > second and freqs[key] < first:
        second = freqs[key]
        second_count = 1
    elif freqs[key] == second and freqs[key] < first:
        second_count += 1
"""