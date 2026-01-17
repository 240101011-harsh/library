class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("book id is not allowed")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }

    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("book not found")

        if self.books[book_id]["borrowed"]:
            raise ValueError("already borrowed")

        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("book not found")

        self.books[book_id]["borrowed"] = False
