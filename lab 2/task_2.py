money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

_currentSpend = spend
_currentMoney = money_capital + salary - _currentSpend  # first month
_monthCounter = 0                                       # first month


while _currentMoney >= 0:
    _currentSpend = _currentSpend + _currentSpend * increase
    _currentMoney += salary - _currentSpend
    _monthCounter += 1

print("Количество месяцев, которое можно протянуть без долгов:", _monthCounter)
