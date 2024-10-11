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
    curr_check += b
    for code_index in range(len(letter_codes)):
        if len(letter_codes[code_index]) == len(curr_check):
            if letter_codes[code_index] == curr_check:
                output += letters[code_index]
                curr_check = ""
                bits = bits.replace(letters[code_index], "", 1)
    if len(bits) == 0:
        break

print(output)