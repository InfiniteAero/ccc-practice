import math

x = int(input())
y = int(input())

wholes = x // y

remainder = x - (y * wholes)

# illegal
factor = math.gcd(remainder, y)

remainder = int(remainder / factor)
y = int(y / factor)

if wholes == 0 and remainder != 0:
    print(str(remainder) + '/' + str(y))
elif wholes != 0 and remainder != 0:
    print(str(wholes) + ' ' + str(remainder) + '/' + str(y))
elif wholes != 0 and remainder == 0:
    print(wholes)
else:
    print(0)