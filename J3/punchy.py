import math

a, b = 0, 0

output = ""
while True:
    command = input().split()
    if len(command) == 1: break
    for part in range(len(command)):
        try: command[part] = int(command[part])
        except ValueError: continue
    match command[0]:
        case 1:
            if command[1] == "A": a = command[2]
            else: b = command[2]
        case 2:
            if command[1] == "A": output += str(a) + "\n"
            else: output += str(b) + "\n"
        case 3:
            if command[1] == "A" and command[2] == "A": a = a + a
            elif command[1] == "B" and command[2] == "B": a = b + b
            elif command[1] == "A": a = a + b
            else: b = a + b
        case 4:
            if command[1] == "A" and command[2] == "A": a = a * a
            elif command[1] == "B" and command[2] == "B": a = b * b
            elif command[1] == "A": a = a * b
            else: b = a * b
        case 5:
            if command[1] == "A" and command[2] == "A": a = a - a
            elif command[1] == "B" and command[2] == "B": a = b - b
            elif command[1] == "A": a = a - b
            else: b = a - b
        case 6:
            if command[1] == "A" and command[2] == "A": a = 1
            elif command[1] == "B" and command[2] == "B": a = 1
            elif command[1] == "A": a = math.floor(a/b)
            else: b = math.floor(b/a)

print(output)