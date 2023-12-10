# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Car:
    def __init__(self, model: str, year: int, color: str, price: int):
        """
               Создание и подготовка к работе объекта "Стакан"

               :param capacity_volume: Объем стакана
               :param occupied_volume: Объем занимаемой жидкости

               Примеры:
               >>> car = Car("BMW", 2010, "black", 1000000)  # инициализация экземпляра класса
               """
        self.model = model
        if not isinstance(year, int):
            raise TypeError("год должен быть типа int")
        if year <= 1800:
            raise ValueError("Слишком старый автомобиль")
        if price < 0:
            raise ValueError("Цена автомобиля не может быть отрицательной")
        self.year = year
        self.color = color
        self.price = price

    def GetPrice(self) -> int:
        """
            Функция получения цены авто

            :return: цента автомобиля

            Примеры:
            >>> car = Car("BMW", 2010, "black", 1000000)  # инициализация экземпляра класса
            >>> car.GetPrice()
        """
        # return self.price

    def ResetPrice(self, newPrice: int):

        """
          Функция для установки новой цены автомобиля

          :return: None

          Примеры:
          >>> car = Car("BMW", 2010, "black", 1000000)  # инициализация экземпляра класса
          >>> car.ResetPrice(1500000)
        """

        self.price = newPrice

    def GetYear(self):
        """
            Функция получения года авто

            :return: год автомобиля

            Примеры:
            >>> car = Car("BMW", 2010, "black", 1000000)  # инициализация экземпляра класса
            >>> car.GetYear()
        """
        # return self.year



class GameCharacter:
    ...

    def __init__(self, x: int, y: int, hp: int):
        """
        Создание и подготовка к работе объекта "GameCharacter"

            :param x: x координата объекта
            :param y: y координата объекта
            :param HP: здоровье персонажа.

            Примеры:
             >>> gc= GameCharacter(0,0,10)
        """
        self.x = x
        self.y = y
        if hp <= 0:
            raise ValueError("Здоровье создоваемой сущности не может быть отрицательным или равняться 0!")
        self.hp = hp
        self.speed = 5
        self.alive = True

    def Move(self, directionOrt: int) -> None:

        """
        Перемещение персонажа
        :param directionOrt: орт оси направления (-1 или 1)

        Пример:
             >>> gc= GameCharacter(0,0,10)# инициализация экземпляра класса
             >>> gc.Move(-1)    # движение в отрицательном направлении оси ОХ
        """
        self.x += (directionOrt * self.speed)
        ...

    def Damage(self, damage: int) -> None:
        """
        Получение урона
        :param damage: урон наносимый персонажу
        Пример:
             >>> gc= GameCharacter(0,0,10)# инициализация экземпляра класса
             >>> gc.Damage(6)
        """
        if self.hp - damage <= 0:
            self.hp = 0
            self.alive = False
        ...

    def Alive(self) -> bool:
        """
        Проверка живой ли персонаж

        Пример:
            >>> gc = GameCharacter(0, 0, 10)  # инициализация экземпляра класса
            >>> gc.Alive()
        """
        ...
        # return self.alive


class Fridge:
    def __init__(self, capacity_volume: float, content: dict):

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем холодильника должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем холодильника должен быть положительным числом")
        self.capacity_volume = capacity_volume
        self.content = content
        # self.temperatureMode = -4

    def PutProducts(self, content: dict) -> None:
        """
                Функция которая добавляет продукты в холодильник

                :return: None

                Примеры:
                >>> fridge = Fridge(500, {})
                >>> fridge.PutProducts({"apple": 1})
                """
        # self.content += content

    def PutProduct(self, product: str, count: int) -> None:
        """
                Добавление продуктов в холодильник.
                :param product: название продукта
                :param count: количество этого продукта

                :return: None

                Примеры:
                >>> fridge = Fridge(500, {})
                >>> fridge.PutProduct("apple", 2)
                """

        if count <= 0:
            raise ValueError("Количество добавленного продукто должно быть больше 0!")
        if not isinstance(count, int):
            raise TypeError("Количество добавляемоего продукто дожно иметь тип int!")
        if product in self.content:
            self.content[product] += count
            return
        self.content[product] = count

    def TakeProduct(self, product: str) -> int:
        """
                Извлечение продуктов из холодильника.

                :param product: название продукта


                :return: Количество извлеченного продукта

                Примеры:
                >>> fridge = Fridge(500, {"apple": 2})
                >>> fridge.TakeProduct("apple")
                """
        # if product not in self.content:
        #     return 0
        # return self.content[product]

    def IsEmpty(self) -> bool:
        """
                Функция которая проверяет является ли холодильник пустым

                :return: является ли холодильник пустым

                Примеры:
                >>> fridge = Fridge(500, {})
                >>> fridge.IsEmpty()
                """
        ...
        # return len(self.content) == 0


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
