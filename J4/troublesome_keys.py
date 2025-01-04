# CCC '24 J4
pressed = input()
displayed = input()
pressed_keys = []
displayed_keys = []
suspicious = []
silly = ""
quiet = ""
wrong = ""

for char in pressed:
    if char not in pressed_keys:
        pressed_keys.append(char)

for char in displayed:
    if char not in displayed_keys:
        displayed_keys.append(char)

for char in pressed_keys:
    if char not in displayed_keys:
        suspicious.append(char)

for char in displayed_keys:
    if char not in pressed_keys:
        wrong = char

# compare
if len(suspicious) == 2:
    pressed_recon = str(pressed)
    pressed_recon = pressed_recon.replace(suspicious[0], wrong)
    pressed_recon = pressed_recon.replace(suspicious[1], "")
    if displayed == pressed_recon:
        silly = suspicious[0]
        quiet = suspicious[1]
    else:
        silly = suspicious[1]
        quiet = suspicious[0]
else:
    silly = suspicious[0]

print(silly, wrong)
if quiet:
    print(quiet)
else:
    print("-")