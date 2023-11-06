# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    _jsonData = []

    with open(INPUT_FILENAME, 'r') as file:
        for r in csv.DictReader(file):
            _jsonData.append(r)
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(_jsonData, file, indent=4, ensure_ascii=True)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
