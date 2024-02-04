BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book

class Book:
    """ Класс книга """

    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return "Книга \"" + str(self.name) + "\""

    def __repr__(self):
        rep = 'Book(id_=' + str(self.id) + ', name=\'' + str(self.name) + '\', pages=' + str(self.pages) + ')'
        return rep


# TODO написать класс Library
class Library:
    """ Класс библиотека """

    def __init__(self, books: list[Book] = None):
        self.books = books

    def get_next_book_id(self):
        """ Метод, возвращающий идентификатор для добавления новой книги в библиотеку """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """ Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса """
        if id_ < 1 or id_ > len(self.books) or len(self.books) == 0:
            raise ValueError("Книги с запрашиваемым id не существует")
        if not isinstance(id_, int):
            raise ValueError("id должен быть int")
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
