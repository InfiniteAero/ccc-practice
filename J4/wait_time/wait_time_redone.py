# CCC '15 J4
time = 0
friend_index = []
sent_n = []
receive_n = []
sent_t = []
receive_t = []

x = int(input())
for _ in range(x):
    message = input().split()
    message[1] = int(message[1])
    if message[1] not in friend_index and message[0] != "W":
        friend_index.append(message[1])
        sent_n.append(0)
        receive_n.append(0)
        sent_t.append(0)
        receive_t.append(0)
    if message[0] == "W":
        time += message[1] - 1
    elif message[0] == "R":
        i = friend_index.index(message[1])
        receive_n[i] += 1
        receive_t[i] += time
    elif message[0] == "S":
        i = friend_index.index(message[1])
        sent_n[i] += 1
        sent_t[i] += time
    if message[0] != "W":
        time += 1

friend_wait_times = []
for j in range(len(friend_index)):
    pair = [friend_index[j], 0]
    if receive_n[j] != sent_n[j]:
        pair[1] = -1
    else:
        pair[1] = sent_t[j] - receive_t[j]
    friend_wait_times.append(list(pair))

friend_wait_times.sort()
for friend in friend_wait_times:
    print(friend[0], friend[1])