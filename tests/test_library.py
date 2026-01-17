import unittest
from src.library import Library


class TestLibrarySprint2(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book(1, "Clean Code", "Robert C. Martin")

    def test_borrow_available_book(self):
        self.library.borrow_book(1)
        self.assertTrue(self.library.books[1]["borrowed"])
        
        
    def test_borrow_book_unavailable(self):
        self.library.borrow_book(1)
        with self.assertRaises(ValueError):
            self.library.borrow_book(1)
            
            
    def test_return_book(self):
        self.library.borrow_book(1)
        self.library.return_book(1)
        self.assertFalse(self.library.books[1]["borrowed"])
    







if __name__ == "__main__":
    unittest.main()

