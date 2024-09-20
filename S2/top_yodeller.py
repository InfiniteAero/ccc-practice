import math

_in = input().split()
n = int(_in[0])
k = int(_in[1])

scores = n * [0]
lowest_rank = n * [0]
winner = n * [False]

for i in range(k):
    round = input().split()
    for j in range(len(round)):
        round[j] = int(round[j])
    # add scores
    for j in range(len(round)):
        scores[j] += round[j]
    # find rank
    for j in range(len(scores)):
        rank = 1
        for l in range(len(scores)):
            if scores[j] < scores[l]:
                rank += 1
        if lowest_rank[j] == 0 or rank > lowest_rank[j]:
            lowest_rank[j] = rank

# find winner
highest = -math.inf
for j in range(len(scores)):
    for l in range(len(scores)):
        if scores[j] >= scores[l] and scores[j] > highest:
            highest = scores[j]
win_indexes = []
for j in range(len(scores)):
    if scores[j] == highest:
        win_indexes.append(j)


for contestant in win_indexes:
    print("Yodeller " + str(contestant + 1) + " is the TopYodeller: score " + str(scores[contestant]) + ", worst rank " + str(lowest_rank[contestant]))
