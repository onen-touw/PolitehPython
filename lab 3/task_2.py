# TODO Напишите функцию find_common_participants

def __SeparateStr(str, separator):
    if str == "":
        return []

    _out = []
    _tempStr = ""
    _i = 0

    while _i < len(str):
        if str[_i] == separator:
            _out.append(_tempStr)
            _tempStr = ""
        else:
            _tempStr += str[_i]
        _i += 1
    else:                       # for last name in str (after last separator)
        _out.append(_tempStr)
    return _out


def find_common_participants(str1, str2, separator=","):
    _itemList1 = __SeparateStr(str1, separator)
    _itemList2 = __SeparateStr(str2, separator)
    _listOut = []

    for it1 in _itemList1:
        for it2 in _itemList2:
            if it1 == it2:
                _listOut.append(it1)
    _listOut.sort()
    return _listOut

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

find_common_participants(participants_first_group, participants_second_group, separator='|')

