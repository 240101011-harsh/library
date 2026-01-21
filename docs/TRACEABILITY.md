# TRACEABILITY MATRIX
Library Book Management System

This document maps user stories to implementation, unit tests,
sprints, and Git releases.

| User Story ID | Description                                  | Code / Function            | Unit Test                          | Sprint   | Git Tag |
|---------------|----------------------------------------------|----------------------------|------------------------------------|----------|---------|
| US-01         | Add new book                                 | add_book()                 | test_add_book_success              | Sprint-1 | v0.1    |
| US-02         | Prevent duplicate Book IDs                  | add_book() validation      | test_add_duplicate_book_error      | Sprint-1 | v0.1    |
| US-03         | Borrow available book                       | borrow_book()              | test_borrow_available_book         | Sprint-2 | v0.2    |
| US-04         | Block borrowing of borrowed book            | borrow_book() validation   | test_borrow_unavailable_book_error | Sprint-2 | v0.2    |
| US-05         | Return borrowed book                        | return_book()              | test_return_book                   | Sprint-2 | v0.2    |
| US-06         | Generate library report                     | generate_report()          | test_report_contains_header        | Sprint-3 | v0.3    |

