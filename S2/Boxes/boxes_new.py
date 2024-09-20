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
    for j in range(length-i-1):
        if boxes_vol[j] > boxes_vol[j+1]:
            boxes_vol[j], boxes_vol[j+1] = boxes_vol[j+1], boxes_vol[j]
            boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

for i in range(len(items)):
    for j in range(len(boxes)):
        item = items[i]
        box = boxes[j]
        matched = False
        rotated = 0
        while rotated != 4:
            if item[0] > box[0] or item[1] > box[1] or item[2] > box[2]:
                rotated += 1
                if rotated != 4:
                    temp1 = item[0]
                    temp2 = item[1]
                    temp3 = item[2]
                    item[0], item[1], item[2] = temp3, temp1, temp2
                else:
                    temp1 = item[0]
                    temp2 = item[1]
                    item[0], item[1] = temp2, temp1
            else:
                matched = True
                print(boxes_vol[j])
                break
        if matched:
            break
    if not matched:
        print("Item does not fit.")
