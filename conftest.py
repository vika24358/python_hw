from testing_oop_homework import Library, Book
import pytest


@pytest.fixture(scope='class')
def library1() -> Library:
    library = Library('The Best Library', [])
    return library


@pytest.fixture(scope='class')
def library2() -> Library:
    library = Library('Very Cool Library', [])
    return library


@pytest.fixture(scope='class')
def book1() -> Book:
    book = Book('Кобзар', "Тарас Шевченко", 333)
    return book


@pytest.fixture(scope='class')
def book2() -> Book:
    book = Book('Гаррі Поттер і філософський камень', "Джоан Роулінг", 432)
    return book


@pytest.fixture(scope='class')
def book3() -> Book:
    book = Book('Портрет Доріана Грея', "Оскар Вайльд", 228)
    return book
