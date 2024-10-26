friends = []
friend_status = [] # 1 = waiting, 0 = complete

x = int(input())
for _ in range(x):
    message = input().split()
    message[1] = int(message[1])
    # wait specified time
    if message[0] == "W":
        for i in range(len(friends)):
            if friend_status[i] == 1:
                friends[i][1] += message[1]
        continue
    # add friends to both lists
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
        friend_status[friend_index] = 0
    # count time
    for i in range(len(friends)):
        if friend_status[i] == 1:
            friends[i][1] += 1
    
# mark still waiting friends as -1
for i in range(len(friends)):
    if friend_status[i] == 1:
        friends[i][1] = -1

for friend in friends:
    print(friend[0], friend[1])