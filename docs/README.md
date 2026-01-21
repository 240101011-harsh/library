
---

## 🚀 Agile Development (Sprint-wise)

### 🟢 Sprint 1: Book Registration  
**Sprint Goal:** Add and store book details.

**Features Implemented:**
- Add a book with Book ID, Title, and Author
- Prevent duplicate Book ID entries

**Unit Tests:**
- Successful book addition
- Error raised for duplicate Book ID

**Git Details:**
- Branch: `feature/sprint-1`
- Merge target: `main`
- Tag: `v0.1`

---

### 🟡 Sprint 2: Borrow and Return Book  
**Sprint Goal:** Manage borrowing status of books.

**Features Implemented:**
- Borrow a book
- Return a book
- Prevent borrowing of an already borrowed book

**Unit Tests:**
- Borrowing an available book
- Error when borrowing an unavailable book
- Correct status update after returning a book

**Git Details:**
- Branch: `feature/sprint-2`
- Merge target: `main`
- Tag: `v0.2`

---

### 🔵 Sprint 3: Library Report  
**Sprint Goal:** Generate a library status report.

**Features Implemented:**
- Generate report with:
  - Book ID
  - Title
  - Author
  - Status (Available / Borrowed)

**Unit Tests:**
- Report contains header
- Report contains at least one book entry

**Git Details:**
- Branch: `feature/sprint-3`
- Merge target: `main`
- Tag: `v0.3`

---

## 🧪 Running Unit Tests
To execute all unit tests, run the following command from the project root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
