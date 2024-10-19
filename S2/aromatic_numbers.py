# CCC '12 S2

a_num = input()
a_num_split = []

numerals = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000,
}

for i in range(0, len(a_num), 2):
    a_num_split.append(a_num[i:i+2])

total = 0

for block in range(len(a_num_split)):
    value = int(a_num_split[block][0])
    value *= numerals[a_num_split[block][1]]
    try:
        if numerals[a_num_split[block + 1][1]] > numerals[a_num_split[block][1]]:
            total -= value
            continue
    except IndexError: pass
    total += value

print(total)