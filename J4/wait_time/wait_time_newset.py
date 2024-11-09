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
    batches = []
    friend_time = 0
    counting = False
    started = False
    for message in messages:
        if message[1] == friend[0] and message[0] != "W":
            started = True
        if (message[0] == "W" or message[0] == "R") and started:
            friend_messages.append(message)
        if message[0] == "S" and message[1] == friend[0]:
            friend_messages.append(message)
    batch = []
    for friend_message in friend_messages:
        batch.append(friend_message)
        if friend_message[0] == "R" and friend_message[1] == friend[0]:
            counting = True
        if friend_message[0] == "S":
            counting = False
            batches.append(list(batch.copy()))
            batch = []
    for group in batches:
        waited = False
        waited_time = 0
        other = 1
        for part in group:
            if part[0] == "W":
                waited = True
                waited_time += part[1]
            if part[1] != friend[0] and part[0] == "R":
                other += 1
        if waited: friend_time += waited_time
        friend_time += other
        #for part in group:
        #    if part[1] != friend[0] and part[0] == "R":
        #        friend_time += 1
    if counting: friend_time = -1
    friend[1] = friend_time
    
    print(batches)

for friend in friends:
    print(friend[0], friend[1])