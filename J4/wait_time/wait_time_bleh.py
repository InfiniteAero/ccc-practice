# CCC '15 J4

friends = []
messages = []

x = int(input())
for _ in range(x):
    message = input().split()
    message[1] = int(message[1])
    messages.append(message)
    if [message[1], 0] not in friends and message[0] != "W":
        friends.append([message[1], 0])

for friend in friends:
    friend_messages = []
    inner_friend_messages = []
    record = False
    for message in messages:
        if friend[0] == message[1] and message[0] == "R":
            record = True
        if record: inner_friend_messages.append(message)
        if friend[0] == message[1] and message[0] == "S":
            record = False
            friend_messages.append(list(inner_friend_messages))
            inner_friend_messages = []
    if record == True:
        friend[1] = -1
        continue
    friend_messages = list(filter(None, friend_messages))
    # print(friend_messages)
    for inner_messages in friend_messages:
        if len(inner_messages) == 2:
            friend[1] += 1
        else:
            for inner in inner_messages:
                if friend[0] != inner[1]:
                    if inner[0] == "W":
                        friend[1] += inner[1]
                    else: friend[1] += 1

for friend in friends:
    print(friend[0], friend[1])