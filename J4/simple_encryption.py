key = input()
message = input()

new_message = []
message = list(message)
for i in range(len(message)):
    if ord(message[i]) < 65 or ord(message[i]) > 90:
        continue
    new_message.append(message[i])
new_message = ''.join(new_message)


sep_message = []
for i in range(0, len(new_message), len(key)):
    sep_message.append(new_message[i:i+len(key)])

output = []
for section in sep_message:
    section = list(section)
    for i in range(len(section)):
        char_diff = ord(key[i]) - 65 # 'A' ASCII code is 65
        if not char_diff: continue
        new = ord(section[i]) + char_diff
        if new > 90:
            new = new - 91 + 65
        section[i] = chr(new)
    section = ''.join(section)
    output.append(section)

output = ''.join(output)
print(output)