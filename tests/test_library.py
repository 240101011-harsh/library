import unittest
from src.library import Library


class TestLibrarySprint3(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.library.add_book(1, "Clean Code", "Robert C. Martin")

    def test_add_book_success(self):
        self.library.add_book(2, "Clean Code", "Robert C. Martin")
        self.assertIn(2, self.library.books)

    def test_duplicate_book_raises_error(self):
        self.library.add_book(2, "Clean Code", "Robert C. Martin")
        with self.assertRaises(ValueError):
            self.library.add_book(2, "Refactoring", "Martin Fowler")
 

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
    

    def test_report_not_empty(self):
        report=self.library.generate_report()
        self.assertTrue(report[0][0],1)
    def test_report_contains_book(self):
        report=self.library.generate_report()
        self.assertEqual(report[0][0],1)







if __name__ == "__main__":
    unittest.main()

