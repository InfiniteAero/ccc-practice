messages = []
x = int(input())
for i in range(x): messages.append(input())

for message in messages:
    temp_message = message
    split_message = []
    current_char = ''
    temp_string = ''
    for index in range(len(temp_message)):
        if current_char == '':
            current_char = temp_message[index]
        if temp_message[index] != current_char:
            split_message.append(temp_string)
            temp_string = ''
        current_char = temp_message[index]
        temp_string += current_char
    split_message.append(temp_string)
    
    print(split_message)