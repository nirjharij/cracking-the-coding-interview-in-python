row_has_zero = False
col_has_zero = False

mat = [[1, 2, 3, 4], [5, 6, 7, 0], [3, 9, 0, 1]]


def nullify_row_matrix(row):
    for j in range(len(mat[0])):
        mat[row][j] = 0


def nullify_col_matrix(col):
    for i in range(len(mat)):
        mat[i][col] = 0


for j in range(len(mat[0])):
    if mat[0][j] == 0:
        row_has_zero = True
        break

for i in range(len(mat)):
    if mat[i][0] == 0:
        col_has_zero = True
        break

for i in range(1, len(mat)):
    for j in range(1, len(mat[0])):
        if mat[i][j] == 0:
            mat[i][0] = 0
            mat[0][j] = 0

for i in range(1, len(mat)):
    if mat[i][0] == 0:
        nullify_row_matrix(i)

for j in range(1, len(mat[0])):
    if mat[0][j] == 0:
        nullify_col_matrix(j)

if row_has_zero:
    nullify_row_matrix(0)
if col_has_zero:
    nullify_col_matrix(0)

print(mat)
