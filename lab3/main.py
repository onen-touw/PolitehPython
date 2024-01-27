class Book(object):
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        if pages < 0:
            raise ValueError("Колличество страниц не может быть < 0")
        Book.__init__(self, name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        if duration < 0:
            raise ValueError("Длительность не может быть < 0")
        Book.__init__(self, name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"


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
    pBook = PaperBook("name", "auth", 10)
    print(pBook)
    aBook = AudioBook("name", "auth", 10.)
    print(aBook)

    list_books = [
        PaperBook(name=book_dict["name"], author=book_dict["author"], pages=book_dict["pages"]) for book_dict in
        BOOKS_DATABASE
    ]
    print(list_books)
#                                     TEST END
