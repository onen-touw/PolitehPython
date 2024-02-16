class CarBase(object):
    """
        Класс автомобиль
    """

    def __init__(self, model: str = "", power: int = 0, price: int = 0, maxSpeed: int = 0):
        """
        :param model: модель автомобиля
        :param power: мощность автомобиля
        :param price: цена автомобиля (целое число)
        :param maxSpeed: максимальная скорость развиваемая автомобилем

        для всех этих полей написаны гетеры, сеттеры
        также все эти поля создаются как защищенные, объесняется это тем,
        что они будут использоваться только для чтения(getter) в большинстве задач,
        однако предусмартивается, что они могут быть изменены
        (для этого разработчику придется осознанно вызвать ф-цию setter)
        """

        self.power = power
        self.model = model
        self.price = price
        self.maxSpeed = maxSpeed
        pass

    @property
    def model(self) -> str:
        """ возвращает параметр model """
        return self._model

    @model.setter
    def model(self, model: str) -> None:
        """ устанавливает параметр model """
        if not isinstance(model, str):
            raise TypeError
        self._model = model

    @property
    def power(self) -> int:
        """ возвращает параметр power """
        return self._power

    @power.setter
    def power(self, power: int) -> None:
        """ устанавливает параметр power """
        if power < 0:
            raise ValueError("Power не может быть < 0")
        elif not isinstance(power, int):
            raise TypeError
        self._power = power

    @property
    def price(self) -> int:
        """ возвращает параметр price """
        return self._price

    @price.setter
    def price(self, price: int) -> None:
        """ устанавливает параметр price """
        if price < 0:
            raise ValueError("Price не может быть < 0")
        elif not isinstance(price, int):
            raise TypeError
        self._price = price

    @property
    def maxSpeed(self) -> int:
        return self._maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, maxSpeed: int) -> None:
        """ устанавливает параметр maxSpeed """
        if maxSpeed < 0:
            raise ValueError("Price не может быть < 0")
        elif not isinstance(maxSpeed, int):
            raise TypeError
        self._maxSpeed = maxSpeed

    def __str__(self):
        return f"Машина {self._model}. Цена {self.price} Мощность двигателя {self.power}."

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, power={self.power!r}, price={self.price!r})"


class PassengerCar(CarBase):
    """ Класс легкового автомобиля"""

    def __init__(self, model: str = "", power: int = 0, price: int = 0, maxSpeed: int = 0, placeCount: int = 5):
        """
        :param placeCount: количество мест для пассажиров
        """
        super().__init__(model, power, price, maxSpeed)
        self.placeCount = placeCount

    @property
    def placeCount(self) -> int:
        """ возвращает параметр placeCount """
        return self._placeCount

    @placeCount.setter
    def placeCount(self, placeCount: int) -> None:
        """ устанавливает параметр placeCount """
        if placeCount < 0:
            raise ValueError
        elif not isinstance(placeCount, int):
            raise TypeError
        self._placeCount = placeCount

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, power={self.power!r}, price={self.price!r}, " \
               f"maxSpeed={self.maxSpeed!r}, placeCount={self.placeCount!r})"


class Truck(CarBase):
    """ Класс грузового автомобиля"""

    """ ограничение скорости для грузовых автомобилей на дорогах РФ """
    MAX_SPEED_K = 90

    def __init__(self, model: str = "", power: int = 0, price: int = 0, cap: int = 0):
        """
               :param cap: объем грузовой полости
        """
        super().__init__(model, power, price, self.MAX_SPEED_K)
        self.cap = cap

    @property
    def cap(self) -> int:
        """ возвращает параметр cap """
        return self._cap

    @cap.setter
    def cap(self, cap: int) -> None:
        """ устанавливает параметр cap """
        if cap < 0:
            raise ValueError
        elif not isinstance(cap, int):
            raise TypeError
        self._cap = cap

    @property
    def maxSpeed(self) -> int:
        """
        возвращает параметр maxSpeed
        """
        return self.MAX_SPEED_K

    @maxSpeed.setter
    def maxSpeed(self, val) -> None:
        """ всегда установится значение MAX_SPEED_K """
        self._maxSpeed = self.MAX_SPEED_K

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model!r}, power={self.power!r}, price={self.price!r}, " \
               f"maxSpeed={self.MAX_SPEED_K!r}, placeCount={self.cap!r})"


if __name__ == "__main__":

    tr = Truck("SCANIA", 400, 5_000_000, 12_000_000)
    tr.maxSpeed = 10
    print(tr.maxSpeed)
