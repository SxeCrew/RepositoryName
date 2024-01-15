BOOKSDATA = [
    {
        "id": 1,
        "name": "Дом листьев",
        "pages": 750,
    },
    {
        "id": 2,
        "name": "Сад расходящихся тропок",
        "pages": 256,
    }
]

if __name__ == '__main__':
    class Book:
        def __init__(self, id_, name, pages):
            self.id = id_
            self.name = name
            self.pages = pages

        def __repr__(self):
            return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"
        def __str__(self):
            return f"Книга \"{self.name}\""

    list_books = \
        [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKSDATA]

    #проверка работы метода str
    for book in list_books:
        print(book)
    #проверка работы метода repr
    print(repr(list_books))