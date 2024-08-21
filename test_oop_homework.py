import pytest


class TestLibrary:
    def test_new_library_book_list(self, library1):
        assert library1.book_list == []

    def test_add_book(self, library1, book1):
        library1.add_new_book(book1)
        assert len(library1.book_list) == 1

    def test_add_two_books(self, library1, book2, book3):
        library1.add_new_book(book2)
        library1.add_new_book(book3)
        assert len(library1.book_list) == 3

    def test_book_delete(self, library1, book2):
        library1.delete_book(book2)
        assert len(library1.book_list) == 2

    def test_delete_wrong_book(self, library2, book1):
        with pytest.raises(KeyError):
            library2.delete_book(book1)

    def test_change_name(self, library1):
        new_name = "The coolest library"
        library1.change_name(new_name)
        assert library1.name == new_name

class TestBook:
    def test_book_name(self, book1):
        expected_name = 'Кобзар'
        assert book1.name == expected_name

    def test_book_author(self, book2):
        expected_author = "Джоан Роулінг"
        assert book2.author == expected_author

    def test_amount_of_pages(self, book3):
        expected_amount_of_pages = 228
        assert book3.amount_of_pages == expected_amount_of_pages
