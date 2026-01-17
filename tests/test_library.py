import unittest
from src.library import Library


class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        self.assertIn(1, self.library.books)

    def test_duplicate_book_raises_error(self):
        self.library.add_book(1, "Clean Code", "Robert C. Martin")
        with self.assertRaises(ValueError):
            self.library.add_book(1, "Refactoring", "Martin Fowler")


if __name__ == "__main__":
    unittest.main()
