# TODO  Напишите функцию count_letters

def __calcLetters(str):
    _count = 0
    for ch in str:
        if ch.isalpha():
            _count += 1
    return _count


def count_letters(str):
    _dirOut = {}

    if str == "":
        return {}
    for ch in str:
        if ch.isalpha():
            _key = ch.lower()
            if _key not in _dirOut:
                _dirOut[ch.lower()] = 1
            else:
                _dirOut[ch.lower()] += 1
    return _dirOut


# TODO Напишите функцию calculate_frequency


def calculate_frequency(dir, _simbolCount):
    _dirOut = {}

    if dir == {}:
        return {}
    for key, value in dir.items():
        _dirOut[key] = round(value/_simbolCount, 2)
    return _dirOut


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
for key, value in calculate_frequency(count_letters(main_str), __calcLetters(main_str)).items():
    print("%s: %.2f" % (key, value))
