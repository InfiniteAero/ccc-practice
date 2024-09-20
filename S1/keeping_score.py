hand = input()

# processing input string
hand = hand.strip("C")
clubs = hand.split("D")[0]
hand = hand.split("D")[1]
diamonds = hand.split("H")[0]
hand = hand.split("H")[1]
hearts = hand.split("S")[0]
hand = hand.split("S")[1]
hand = hand.strip("S")
spades = hand


# process clubs
clubs_score = 0

# check for suit count
if len(clubs) == 0:
    clubs_score += 3
elif len(clubs) == 1:
    clubs_score += 2
elif len(clubs) == 2:
    clubs_score += 1

# check cards
for char in clubs:
    if char == "A":
        clubs_score += 4
    elif char == "K":
        clubs_score += 3
    elif char == "Q":
        clubs_score += 2
    elif char == "J":
        clubs_score += 1
    else:
        continue


# process diamonds
diamonds_score = 0

# check for suit count
if len(diamonds) == 0:
    diamonds_score += 3
elif len(diamonds) == 1:
    diamonds_score += 2
elif len(diamonds) == 2:
    diamonds_score += 1

# check cards
for char in diamonds:
    if char == "A":
        diamonds_score += 4
    elif char == "K":
        diamonds_score += 3
    elif char == "Q":
        diamonds_score += 2
    elif char == "J":
        diamonds_score += 1
    else:
        continue


# process hearts
hearts_score = 0

# check for suit count
if len(hearts) == 0:
    hearts_score += 3
elif len(hearts) == 1:
    hearts_score += 2
elif len(hearts) == 2:
    hearts_score += 1

# check cards
for char in hearts:
    if char == "A":
        hearts_score += 4
    elif char == "K":
        hearts_score += 3
    elif char == "Q":
        hearts_score += 2
    elif char == "J":
        hearts_score += 1
    else:
        continue


# process spades
spades_score = 0

# check for suit count
if len(spades) == 0:
    spades_score += 3
elif len(spades) == 1:
    spades_score += 2
elif len(spades) == 2:
    spades_score += 1

# check cards
for char in spades:
    if char == "A":
        spades_score += 4
    elif char == "K":
        spades_score += 3
    elif char == "Q":
        spades_score += 2
    elif char == "J":
        spades_score += 1
    else:
        continue


total_score = clubs_score + diamonds_score + hearts_score + spades_score


# produce final output
output = "Cards Dealt Points\n"

output += "Clubs "
for char in clubs:
    output += char + " "
output += str(clubs_score)
output += "\n"

output += "Diamonds "
for char in diamonds:
    output += char + " "
output += str(diamonds_score)
output += "\n"

output += "Hearts "
for char in hearts:
    output += char + " "
output += str(hearts_score)
output += "\n"

output += "Spades "
for char in spades:
    output += char + " "
output += str(spades_score)
output += "\n"

output += "Total " + str(total_score)
print(output)
