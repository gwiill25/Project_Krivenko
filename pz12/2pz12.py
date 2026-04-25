#В матрице элементы последнего столбца заменить на -1.
def replace_last_column(matrix):

    return [row[:-1] + [-1] for row in matrix]

matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matr = replace_last_column(matr)

print("Исходная матрица:")
for row in matr:
    print(row)

print("\nРезультат (последний столбец заменён на -1):")
for row in new_matr:
    print(row)