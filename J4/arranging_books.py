# test input!
# SSMLMMMLSLLMSLMS

shelf = input()
shelf = list(shelf)

swap_count = 0

lr, lrr, ml, mr, sl, sll = 0, 0, 0, 0, 0, 0
L, M, S = 0, 0, 0

for i in range(len(shelf)):
    if shelf[i] == 'L':
        L += 1
    if shelf[i] == 'M':
        M += 1
    if shelf[i] == 'S':
        S += 1

g1 = shelf[:L]
x = shelf[L:]
g2 = x[:M]
g3 = x[M:]

for i in g1:
    if i == 'M':
        lr += 1
    elif i == 'S':
        lrr += 1
for i in g2:
    if i == 'L':
        ml += 1
    elif i == 'S':
        mr += 1
for i in g3:
    if i == 'M':
        sl += 1
    elif i == 'L':
        sll += 1

# print("lr: " + str(lr))
# print("lrr: " + str(lrr))
# print("ml: " + str(ml))
# print("mr: " + str(mr))
# print("sl: " + str(sl))
# print("sll: " + str(sll))

# count single swaps
diff_lrr = abs(lrr - sll)
if lrr >= sll:
    swap_count += lrr - diff_lrr
else:
    swap_count += sll - diff_lrr

diff_lr = abs(lr - ml)
if lr >= ml:
    swap_count += lr - diff_lr
else:
    swap_count += ml - diff_lr

diff_mr = abs(mr - sl)
if mr >= sl:
    swap_count += mr - diff_mr
else:
    swap_count += sl - diff_mr

# print("single swaps: " + str(swap_count))

# count double swaps
swap_count += ((diff_lr + diff_lrr + diff_mr) // 3) * 2

# print("total swaps: " + str(swap_count))

print(swap_count)