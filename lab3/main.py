class Book(object):
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def get_name(self) -> str:
        return self.__name

    def get_author(self) -> str:
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    """ Класс бумажная книга (Наследник Book). """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, " \
               f"pages={self._pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        # print("pages::setter")
        if pages < 0:
            raise ValueError("Колличество страниц не может быть < 0")
        elif not isinstance(pages, int):
            raise TypeError
        self._pages = pages


class AudioBook(Book):
    """ Класс аудио книга (Наследник Book). """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}," \
               f" duration={self._duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        # print("duration::setter")
        if duration < 0:
            raise ValueError("Длительность не может быть < 0")
        elif not isinstance(duration, float):
            raise TypeError
        self._duration = duration


#                                   TEST START
BOOKS_DATABASE = [
    {
        "name": "test_name_1",
        "author": "a1",
        "pages": 200,
    },
    {
        "name": "test_name_2",
        "author": "a2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    pBook = PaperBook("pName", "pAuth", 10)
    print(pBook)
    print(pBook.pages, "\n")

    aBook = AudioBook("aName", "aAuth", 10.)
    print(aBook)
    print(aBook.duration, "\n")

    list_books = [
        PaperBook(name=book_dict["name"], author=book_dict["author"], pages=book_dict["pages"]) for book_dict in
        BOOKS_DATABASE
    ]
    print(list_books)
#                                     TEST END
