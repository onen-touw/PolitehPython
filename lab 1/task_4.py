users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

_dir = {"Общее количество": 0, "Уникальные посещения": 0}

def __GetUniqVisitors():
    _uniqueVisitCount = 0

    for user in users:
        _VisitCount = 0
        for uniqueUser in users:
            if user == uniqueUser:
                _VisitCount += 1
        if _VisitCount > 1:
            _uniqueVisitCount += 1
    return _uniqueVisitCount


_dir["Общее количество"] = len(users)
_dir["Уникальные посещения"] = __GetUniqVisitors()

print(_dir)
