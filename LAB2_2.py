from typing import Any

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

        def __str__(self):
            return f"Книга \"{self.name}\""

        def __repr__(self):
            return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


    class Library:
        def get_index_by_book_id(self, id: Any) -> ValueError | int:
            for index, value in enumerate(self.books):
                if value.id == id:
                    return index
            return ValueError("Книги с таким номером не существует")

        def get_next_book_id(self) -> int:
            return len(self.books) + 1

        def __init__(self, books=None):
            if books is None:
                self.books = []
            else:
                self.books = books.copy()






    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKSDATA
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))