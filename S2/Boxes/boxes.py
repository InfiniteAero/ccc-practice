x = int(input())
boxes = []
for i in range(x):
    box_dime = input().split()
    boxes.append(box_dime)
for box in boxes:
    for i in range(len(box)):
        box[i] = int(box[i])

x = int(input())
items = []
for i in range(x):
    item = input().split()
    items.append(item)
for item in items:
    for i in range(len(item)):
        item[i] = int(item[i])

boxes_vol = []
for box in boxes:
    vol = box[0] * box[1] * box[2]
    boxes_vol.append(vol)

# sort
length = len(boxes_vol)
for i in range(length):
    swap = False
    for j in range(length-i-1):
        if boxes_vol[j] > boxes_vol[j+1]:
            boxes_vol[j], boxes_vol[j+1] = boxes_vol[j+1], boxes_vol[j]
            boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

for i in range(len(items)):
    check_count = 0
    for j in range(len(boxes)):
        no_fits = False
        while not no_fits:
            for k in range(3):
                if items[i][k] > boxes[j][k]:
                    check_count += 1
                    break
                print(boxes_vol[j])
                no_fits = True
            if check_count == 3:
                no_fits = True
                print("Item does not fit")
            else:
                temp = items[i][0]
                items[i][0] = items[i][-1]
                items[i][-1] = temp
        if no_fits:
            break
            