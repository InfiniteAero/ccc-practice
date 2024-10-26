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
    batch = []
    batch_count = 0
    add_time = 1
    done = False
    for part in range(len(messages_copy)):
        batch.append(messages_copy[part])
        batch_count += 1
        if batch_count == 2: break
    for item in batch:
        messages_copy.remove(item)
    if len(messages_copy) == 0: done = True
    for message in batch:
        # count wait time
        if message[0] == "W":
            for i in range(len(friends)):
                if friend_status[i] == 1:
                    friends[i][1] += message[1]
            continue
        if len(friends) == 0:
            friends.append([message[1], -1])
            friend_status.append(0)
        else:
            exists = False
            for friend in friends:
                if friend[0] == message[1]: exists = True
            if not exists:
                friends.append([message[1], -1])
                friend_status.append(0)
        # find friend index
        for friend in friends:
            if friend[0] == message[1]:
                friend_index = friends.index(friend)
        # mark friend as waiting or not waiting
        if message[0] == "R":
            friend_status[friend_index] = 1
        else:
            friends[friend_index][1] += 1
            friend_status[friend_index] = 0
    # count time
    for i in range(len(friends)):
        if friend_status[i] == 1:
            friends[i][1] += add_time
    
    if done: break

# mark still waiting friends as -1
for i in range(len(friends)):
    if friend_status[i] == 1:
        friends[i][1] = -1

for friend in friends:
    print(friend[0], friend[1])