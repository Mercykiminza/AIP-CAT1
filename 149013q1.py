class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_borrowed(self):
        self.is_borrowed = True

    def mark_returned(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_borrowed()
            self.borrowed_books.append(book.title)
            return f"{book.title} successfully borrowed."
        else:
            return f"{book.title} is already borrowed."

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.mark_returned()
            self.borrowed_books.remove(book.title)
            return f"{book.title} returned successfully."
        else:
            return f"{book.title} not found in borrowed books."

    def list_borrowed_books(self):
        return f"Borrowed Books: {', '.join(self.borrowed_books)}"


book1 = Book("Python Programming", "Author A")
member1 = LibraryMember("Alice", "M123")
print(member1.borrow_book(book1))
print(member1.list_borrowed_books())
print(member1.return_book(book1))
print(member1.list_borrowed_books())
