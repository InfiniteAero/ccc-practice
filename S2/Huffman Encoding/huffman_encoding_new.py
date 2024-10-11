# CCC '10 S2
x = int(input())

letters = []
letter_codes = []

for i in range(x):
    a = input().split()
    letters.append(a[0])
    letter_codes.append(a[1])

bits = input()

output = ""
curr_check = ""
for b in bits:
    potentials = []
    curr_check += b
    for code_index in range(len(letter_codes)):
        if curr_check in letter_codes[code_index]:
            potentials.append(code_index)
    if len(potentials) == 1:
        output += letters[potentials[0]]
        curr_check = ""
        bits = bits.replace(letter_codes[potentials[0]], "", 1)
    if len(bits) == 0:
        break

print(output)