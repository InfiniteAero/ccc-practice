# CCC '24 S2
strings = []
x = list(map(int, input().split()))
for i in range(x[0]):
    strings.append(input())
    
for stringy in strings:
    weights = {}
    for char in stringy:
        if char not in weights:
            weights[char] = 1
        else:
            weights[char] += 1
    bad = False
    if weights[stringy[0]] == 1: current = 1
    else: current = 2
    for char in stringy:
        if weights[char] == 1 and current != 1:
            bad = True
            break
        if weights[char] > 1 and current == 1:
            bad = True
            break
        if current == 1: current = 2
        else: current = 1
    if bad: print("F")
    else: print("T")