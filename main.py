def check_pattern(field):
    rows = len(field)
    cols = len(field[0])

    # горизонтальная проверка
    for row in range(rows):
        for col in range(cols - 4):
            if field[row][col:col + 5] == [1] * 5:
                return 1
            elif field[row][col:col + 5] == [0] * 5:
                return -1

    # вертикальная
    for col in range(cols):
        for row in range(rows - 4):
            column_values = [field[row + i][col] for i in range(5)]
            if column_values == [1] * 5:
                return 1
            elif column_values == [0] * 5:
                return -1

    # диагональ вправо вниз
    for row in range(rows - 4):
        for col in range(cols - 4):
            diagonal_values = [field[row + i][col + i] for i in range(5)]
            if diagonal_values == [1] * 5:
                return 1
            elif diagonal_values == [0] * 5:
                return -1

    # диагональ влево вниз
    for row in range(rows - 4):
        for col in range(4, cols):
            diagonal_values = [field[row + i][col - i] for i in range(5)]
            if diagonal_values == [1] * 5:
                return 1
            elif diagonal_values == [0] * 5:
                return -1

    return 0


def read_file_to_array(input_file):
    array = []
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            row = line.split(', ')
            row = [int(value) if value.isdigit() else None for value in row]
            array.append(row)
    return array


filename = 'input5.txt'
output_arr = read_file_to_array(filename)
res = check_pattern(output_arr)
print(res, output_arr)

# field_1 = [
#     [None, None, None, None, None, 0, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None],
#     [None, None, 0, None, None, None, None, None, None, None],
#     [None, None, None, None, None, 0, None, None, None, None],
#     [1, None, None, None, 0, 1, 1, 1, 1, 1],
#     [None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, 0, None, None, None, None, None, None]
# ]  # Наличие пяти единиц подряд по горизонтали (размер 10 на 10)
#
# result_1 = check_pattern(field_1)
# print(result_1)
#
# field_2 = [
#     [None, 1, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, 1, None, None, None, None, None, None, None, None, None],
#     [None, None, 0, None, None, 1, None, None, None, None, None, None],
#     [None, None, 0, None, None, None, None, None, None, None, None, None],
#     [None, None, 0, 1, None, None, None, None, None, None, None, None],
#     [None, None, 0, None, None, None, None, None, None, None, None, None],
#     [None, None, 0, None, None, None, None, None, None, None, None, None],
#     [None, 1, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None]
# ]  # Наличие пяти нулей подряд по вертикали (размер 10 на 12)
#
# result_2 = check_pattern(field_2)
# print(result_2)
#
# field_3 = [
#     [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, 0, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, 0, None, None, None, None, None, None, None, None, None, None],
#     [1, None, None, None, None, None, None, None, None, None, None, None, None, None],
#     [None, 1, 0, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, 1, None, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, 1, None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, 1, None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, 0, None, None, None, None, None, None, None, None]
# ]  # Наличие пяти единиц подряд по диагонали (вправо и вниз) (размер 15 на 14)
#
# result_3 = check_pattern(field_3)
# print(result_3)
#
# field_4 = [
#     [None, None, None, None, None, None, None, None, None, None],
#     [None, 1, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None, None],
#     [None, None, None, 1, None, None, None, 1, None, None],
#     [None, None, None, None, None, 1, 0, None, None, None],
#     [None, None, None, None, None, 0, None, None, None, None],
#     [None, None, None, None, 0, None, None, None, None, None],
#     [None, None, None, 0, None, None, None, None, None, None],
#     [None, None, 0, None, None, None, None, 1, None, None],
#     [None, None, None, None, None, 0, None, None, None, None]
# ]  # Наличие пяти нулей подряд по диагонали (влево и вниз) (размер 10 на 10):
#
# result_4 = check_pattern(field_4)
# print(result_4)
#
# field_5 = [
#     [1, None, None, None, None],
#     [None, 0, None, None, None],
#     [None, None, None, None, 1],
#     [None, 1, None, None, 0],
#     [0, None, None, None, None]
# ]  # ничего
#
# result_5 = check_pattern(field_5)
# print(result_5)
