# CCC 09 S2

def xor(bottom: list, top: list, y: int):
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
rows.reverse()

possible_rows = []
for i in range(1, len(rows)):
    possible_rows.append(rows[i])
    for row in possible_rows:
        temp_rows = []
        temp_rows.append(xor(rows[i], row, y))
    possible_rows.append(temp_rows)

final = []
for i in possible_rows:
    if i not in final:
        final.append(i)

print(final)