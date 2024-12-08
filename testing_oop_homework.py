class Library:
    def __init__(self, name: str, book_list: list):
        self.name = name
        self.book_list = book_list

    def add_new_book(self, new_book: 'Book'):
        self.book_list.append(new_book)
        return self.book_list

    def delete_book(self, book_to_delete: 'Book'):
        if book_to_delete in self.book_list:
            self.book_list.remove(book_to_delete)
        else:
            raise KeyError('No such book found')

    def change_name(self, new_name):
        self.name = new_name


class Book:
    def __init__(self, name, author, amount_of_pages):
        self.name = name
        self.author = author
        self.amount_of_pages = amount_of_pages
