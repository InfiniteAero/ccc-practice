# CCC '11 J4
# horizontal coordinates should be subtracted by 200 when displayed
# vertical coordinates are to be displayed as negative, not positive
# format: (vertical, horizontal)

dug_coords = [
    [1, 200], [2, 200], [3, 200], [3, 201], [3, 202], [3, 203], [4, 203], [5, 203], [5, 204], [5, 205],
    [4, 205], [3, 205], [3, 206], [3, 207], [4, 207], [5, 207], [6, 207], [7, 207], [7, 206], [7, 205],
    [7, 204], [7, 203], [7, 202], [7, 201], [7, 200], [7, 199], [6, 199], [5, 199]
]

output = ""
move = ""
warn = False
coord = [5, 199]
while "q" not in move:
    move = input().split()
    if "q" in move: break
    move[1] = int(move[1])
    for i in range(move[1]):
        if move[0] == "l": coord[1] -= 1
        if move[0] == "r": coord[1] += 1
        if move[0] == "u": coord[0] -= 1
        if move[0] == "d": coord[0] += 1
        if coord in dug_coords:
            warn = True
        dug_coords.append(list(coord))
    if not warn:
        output += str(coord[1] - 200) + " -" + str(coord[0]) + " safe\n"
    else:
        break

if warn: output += str(coord[1] - 200) + " -" + str(coord[0]) + " DANGER\n"

print(output)