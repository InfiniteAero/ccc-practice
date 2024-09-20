x = int(input())
boxes = []
for i in range(x):
    bboxes = list(map(int, input().split()))
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
    matched = False
    for j in range(len(boxes)):
        item = sorted(items[i])
        box = sorted(boxes[j])
        if item[0] <= box[0] and item[1] <= box[1] and item[2] <= box[2]:
            if not matched:
                vol = box[0] * box[1] * box[2]
            matched = True
    if matched:
        print(vol)
    else:
        print("Item does not fit.")

            
