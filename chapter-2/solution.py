"""
Create a Library class with following interface:

- constructor, which will create an instance of Library class. If no arguments are give, an empty collection of books
should be created. If list of books are given as a parameter to the method, each book from the list should be added
to the collection of books.

- an attribute number_of_books should return current number of books in the collection

- add_book(book) method should add a book to the collection if the book does not exist in the collection of books

- borrow_book(book) method should remove a book from the collection if the book is in the collection of books

- show_books() method should print to the console all books, which are in the collection of books
"""


class Library:
    def __init__(self, collection=None):
        self._book_collection = []

        if collection:
            for book in collection:
                self.add_book(book)

    @property
    def number_of_books(self):
        return len(self._book_collection)

    def add_book(self, book):
        if book not in self._book_collection:
            print(f'Book {book} added to collection')
            self._book_collection.append(book)

    def borrow_book(self, book):
        if book in self._book_collection:
            print(f'Book {book} removed from collection')
            self._book_collection.remove(book)

    def show_books(self):
        if self._book_collection:
            print('Book collection:')
            for book in self._book_collection:
                print(book)
        else:
            print('Book collection is empty')


# collection_1 = Library()
# collection_1.show_books()
# collection_1.add_book('C#')
# collection_1.add_book('Java')
# collection_1.show_books()

# print('----------------')

collection_2 = Library(['C#', 'Java', 'Python'])
# collection_2.show_books()
# collection_2.add_book('Ruby')
# collection_2.borrow_book('C#')
collection_2.borrow_book('PHP')
collection_2.add_book('Python')
collection_2.show_books()

print(f'Number of books in collection_2: {collection_2.number_of_books}')

