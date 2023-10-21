salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

_currentSpend = spend
_money_capital = abs(salary - _currentSpend)        # includes first month

for i in range(months - 1):
    _currentSpend = _currentSpend + _currentSpend * increase
    _money_capital += abs(salary - _currentSpend)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(_money_capital))
