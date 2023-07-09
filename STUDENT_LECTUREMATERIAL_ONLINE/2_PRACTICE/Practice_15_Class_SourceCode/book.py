class Book:
    """Information about a book"""

    # 초기화 (overload : 다른 인자 전달 가능)
    def __init__(self, title="", authors=[], publisher="", isbn="0", price=10.0):
        """(Book, str, list of str, str, str, number) -> NoneType
        Create a new book entitled title, written by the people in authors,
        published by publisher, with ISBN isbn and costing price dollars.
        """
        self.title = title 
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn #0
        self.price = price #10.0

    # self 는 무조건 넣어야함 (python이 알아서 넣음)
    def __str__(self):
        """(Book) -> str
        Return a human-readable string representation of this book.
        """
        rep = " Title: {0}\n Authors: {1}\n Publisher: {2}\n ISBN: {3}\n Price: {4}".format(
            self.title, self.authors, self.publisher, self.ISBN, self.price)
        return rep

    # == 가 호출되면 class에 equal 함수를 호출 -> 여기서는 ISBN이 같으면 같은 Object로 인식 (override)
        # __ge__ .... 도 존재
    def __eq__(self, other):
        """ (Book, Book) -> bool
        Return True iff this book and other have the same ISBN.
        """
        return self.ISBN == other.ISBN
        

    def num_authors(self):
        """(Book) -> int

        Return the number of authors of this book.
        """
        return len(self.authors)


