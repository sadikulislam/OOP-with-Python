class Library:

    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, bookname, author):
        self.books.append({'title': bookname, 'author': author})
        print("Your book is added successfully.")

    def remove_book(self, bookname, author):
        self.books.remove({'title': bookname, 'author': author})
        print("Your book is removed successfully.")   

    def display_books(self):
        if len(self.books) == 0:
            print("There is no available books now.")
        else:
            print(f"The number of books available: {len(self.books)}\nAvialable books list: ")
            for book in self.books:
                print(book)

    def borrow_book(self, name, bookname):
        found = False
        for book in self.books:
            if book['title'] == bookname:
                found = True
                self.borrowed_books[name] = bookname
                self.books.remove(book)
                print("Book issued.")
                break
        if not found:
            print(f"{bookname} is not available right now.")
        
    def return_book(self, name):
        if name in self.borrowed_books:
            returned_book = self.borrowed_books.pop(name)
            self.books.append(returned_book)
            print("Thanks for returning.")
        else:
            print("No book borrowed under this name.")
   
    def display_borrowed_books(self):
        print("Borrowed books:")
        for name, book in self.borrowed_books.items():
            print(f"{name}: {book}")


l1 = Library()

l1.add_book("Book1", "Author1")
l1.add_book("Book2", "Author2")
l1.display_books()

l1.borrow_book("Karim", "Book1")
l1.display_books()
l1.display_borrowed_books()
l1.return_book("Karim")
l1.display_books()
l1.display_borrowed_books()

