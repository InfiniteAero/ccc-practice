# CCC '04 S3

def convert_cell_to_index(cell: str):
    row_index = ord(cell[0]) - 65
    return [row_index, int(cell[1])]

spreadsheet = []
for i in range(10):
    row = input().split()
    spreadsheet.append(row)

for row in range(len(spreadsheet)):
    for cell in range(len(spreadsheet[row])):
        done = True
        try: spreadsheet[row][cell] = int(spreadsheet[row][cell])
        except: done = False
        if not done:
            loop = 0
            visited_cells = [str(chr(row + 65) + str(cell + 1))] # adds spreadsheet notation of current cell
            cur_cell_value = 0
            cells_to_check = [str(chr(row + 65) + str(cell + 1))]
            warn = False
            while not done:
                loop += 1
                check_cell = convert_cell_to_index(cells_to_check[0])
                if loop != 1:
                    visited_cells.append(cells_to_check[0])
                try:
                    new_check_cells = spreadsheet[check_cell[0]][check_cell[1] - 1].split("+")
                    if new_check_cells == ["*"]:
                        warn = True
                        break
                    for new_cell in new_check_cells:
                        if new_cell in visited_cells:
                            warn = True
                            break
                        cells_to_check.append(new_cell)
                except: # if cell only contains a numerical value
                    cur_cell_value += int(spreadsheet[check_cell[0]][check_cell[1] - 1])
                # if infinitely looping break loop
                if warn: break
                # remove evaluated cell from list of possibilities
                cells_to_check.pop(cells_to_check.index(str(chr(check_cell[0] + 65) + str(check_cell[1])))) # ValueError
                if len(cells_to_check) == 0:
                    done = True
            if warn: spreadsheet[row][cell] = "*"
            else: cell = cur_cell_value

print(spreadsheet)