numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим


_pos = -1
_sum = 0
_numLen = len(numbers)
for i in range(_numLen):
    if (numbers[i] == None):
        _pos = i
        continue
    _sum += numbers[i]

if _pos != -1:
    numbers[_pos] = _sum / _numLen


print("Измененный список:", numbers)
