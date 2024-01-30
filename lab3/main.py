class Book(object):
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        if pages < 0:
            raise ValueError("Колличество страниц не может быть < 0")
        elif not isinstance(pages, int):
            raise TypeError
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        if duration < 0:
            raise ValueError("Длительность не может быть < 0")
        elif not isinstance(duration, float):
            raise TypeError
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.get_name()!r}, author={self.get_author()!r}, duration={self.duration!r})"


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

    aBook = AudioBook("aName", "aAuthor", 10.31)
    print(aBook)
#                                     TEST END
