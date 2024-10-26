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
        