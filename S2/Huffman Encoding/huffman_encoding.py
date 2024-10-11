# CCC '10 S2 (wrong)
x = int(input())

letters = []
letter_codes = []

for i in range(x):
    a = input().split()
    letters.append(a[0])
    letter_codes.append(a[1])

bits = input()

output = ""
potentials = []
index = 0
for b in bits:
    used_list = []
    if index == 0:
        for i in range(len(letter_codes)):
            used_list.append(i)
    else: used_list = potentials
    potentials = []
    for code_index in used_list:
        try:
            if letter_codes[code_index][index] == b and code_index in used_list:
                potentials.append(code_index)
        except IndexError:
            continue
    if len(potentials) == 1:
        output += letters[potentials[0]]
        bits = bits.replace(letter_codes[potentials[0]], "", 1)
        potentials = []
        index = 0
        continue
    index += 1
    if len(bits) == 0:
        break


print(output)
