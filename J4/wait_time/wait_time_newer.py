# CCC '15 J4

friends = []
friend_status = [] # 1 = waiting, 0 = complete
messages = []

x = int(input())
for _ in range(x):
    message = input().split()
    message[1] = int(message[1])
    messages.append(message)

messages_copy = messages.copy()

while True:
    