# TODO решите задачу
import json


def task() -> float:
    _sum = 0
    _data = []
    with open("input.json") as file:
        _data = json.load(file)
    for item in _data:
        _sum += item["score"] * item["weight"]
    return _sum.__round__(3)


print(task())
