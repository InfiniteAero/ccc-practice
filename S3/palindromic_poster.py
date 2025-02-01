# CCC '23 S3

# solution for subtask 1
vals = list(map(int, input().split()))
n = vals[0]
m = vals[1]
r = vals[2]
c = vals[3]

x = 1
while x <= n:
    if x == 1:
        row = ['a'] * n
    else:
        row = ['a'] + ['b'] * (n - 1)

    print(''.join(row))

    x += 1

