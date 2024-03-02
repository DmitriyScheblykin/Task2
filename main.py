import json


def squareArray(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        input_array = json.loads(file.read())

    # Определение минимального размера для квадратного массива
    min_size = min(len(row) for row in input_array)

    # Обрезка массива до квадратного вида
    square_array = [row[:min_size] for row in input_array[:min_size]]

    with open(output_filename, 'w') as file:
        for row in square_array:
            file.write(json.dumps(row))
            file.write('\n')

    print("Входной массив:")
    for row in input_array:
        print(row)

    print("Результат:")
    for row in square_array:
        print(row)


input_file = "input_array.txt"
output_file = "output_array.txt"

squareArray(input_file, output_file)