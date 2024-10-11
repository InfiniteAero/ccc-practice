# CCC '09 S2

def xor(bottom: list, top: list, y: int) -> list:
    out = []
    for t in range(y):
        if bottom[t] != top[t]:
            out.append(1)
        else:
            out.append(0)
    return out

rows = []

x = int(input())
y = int(input())
for i in range(x):
    rows.append(list(map(int, input().split())))

possible_rows = []
for i in range(1, len(rows)):
    if i == 1: possible_rows.append(rows[i-1])
    temp_rows = []
    for row in possible_rows:
        temp_rows.append(xor(row, rows[i], y))
    temp_rows.append(rows[i])
    possible_rows = temp_rows

final = []
for i in possible_rows:
    if i not in final:
        final.append(i)

print(len(final))