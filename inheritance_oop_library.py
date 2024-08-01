from abc import abstractmethod


class LibraryItem:
    def __init__(self, title: str, author_or_director: str, year: int):
        self.title = title
        self.author_or_director = author_or_director
        self.year = year

    @abstractmethod
    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}"


class Book(LibraryItem):
    def __init__(self, number_of_pages: int):
        self.number_of_pages = number_of_pages

    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}, Number of Pages: {self.number_of_pages}"


class Magazine(LibraryItem):
    def __init__(self, issue_number: int):
        self.issue_number = issue_number

    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}, Issue Number: {self.issue_number}"


class DVD(LibraryItem):
    def __init__(self, duration: int):
        self.duration = duration

    def description(self):
        return f"Title: {self.title}, Author/Director: {self.author_or_director}, Year: {self.year}, Duration: {self.duration}"

