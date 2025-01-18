# CCC '05 S3

matrices = []

matrices_count = int(input())
for i in range(matrices_count):
    matrix = []
    row_count, column_count = list(map(int, input().split()))
    for j in range(row_count):
        row = list(map(int, input().split()))
        matrix.append(row)
    matrices.append(matrix)

# print matrix list for debug purposes
# print(matrices)

# create tensor product
while len(matrices) != 1:
    grid1 = matrices[0]
    grid2 = matrices[1]

    output = []

    for row in grid1:
        for small_row in grid2:
            output_row = []
            for val in range(len(row)):
                for small_val in range(len(small_row)):
                    output_row.append(row[val] * small_row[small_val])
            output.append(output_row)

    matrices[1] = output
    matrices.pop(0)

tensor_product = matrices[0]

# print tensor product for debug purposes
# for final_row in tensor_product:
#     final_row = list(map(str, final_row))
#     print(' '.join(final_row))

# find max and min value for whole tensor product
max_min_list = []
for final_row in tensor_product:
    max_min_list += final_row
max = float('-inf')
min = float('inf')
for val in max_min_list:
    if max < val:
        max = val
    if min > val:
        min = val
print(max)
print(min)

# find max and min row sums of tensor product
row_max = float('-inf')
row_min = float('inf')
for row in tensor_product:
    row_sum = sum(row)
    if row_max < row_sum:
        row_max = row_sum
    if row_min > row_sum:
        row_min = row_sum
print(row_max)
print(row_min)

# find max and min column sums of tensor product
col_max = float('-inf')
col_min = float('inf')
col_count = len(tensor_product[0])
for i in range(col_count):
    col_sum = 0
    for row in tensor_product:
        col_sum += row[i]
    if col_max < col_sum:
        col_max = col_sum
    if col_min > col_sum:
        col_min = col_sum
print(col_max)
print(col_min)