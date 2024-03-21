class Library:

    def __init__(self):
        self.books = []

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


l1 = Library()

l1.add_book("Book1", "Author1")
l1.add_book("Book2", "Author2")

l1.display_books()
l1.remove_book("Book1", "Author1")
l1.display_books()

