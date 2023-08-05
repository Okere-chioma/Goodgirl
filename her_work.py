import datetime

class Book:
    def __init__(self, title, author, genre, isbn, book_code):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.book_code = book_code
        self.is_borrowed = False
        self.borrower_id = None
        self.borrow_date = None
        self.return_date = None
        self.history = []

class Library:
    def __init__(self):
        self.books = []
        self.book_counter = 1

    def add_book(self, title, author, genre, isbn):
        book = Book(title, author, genre, isbn, self.book_counter)
        self.book_counter += 1
        book.history.append(f"Book added to library on {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        self.books.append(book)

    def add_nigerian_books(self):
        nigerian_books = [
            ("Things Fall Apart", "Chinua Achebe", "Fiction", "9780385474542"),
            ("Half of a Yellow Sun", "Chimamanda Ngozi Adichie", "Historical Fiction", "9781400044160"),
            ("Purple Hibiscus", "Chimamanda Ngozi Adichie", "Fiction", "9781616202415"),
            ("Americanah", "Chimamanda Ngozi Adichie", "Fiction", "9780307455925"),
            ("The Secret Lives of Baba Segi's Wives", "Lola Shoneyin", "Fiction", "9780061946370"),
            # Add more Nigerian books here...
        ]

        for title, author, genre, isbn in nigerian_books:
            self.add_book(title, author, genre, isbn)

    def view_books(self):
        print("All Books in the Library:")
        for book in self.books:
            print(f"Collection Number: {book.book_code}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, "
                  f"ISBN: {book.isbn}, Borrowed: {'Yes' if book.is_borrowed else 'No'}")

    def search_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print("Book(s) found:")
            for book in found_books:
                print(f"Collection Number: {book.book_code}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, "
                      f"ISBN: {book.isbn}, Borrowed: {'Yes' if book.is_borrowed else 'No'}")
        else:
            print("Book not found.")

    def borrow_book(self, book_code, borrower_id):
        for book in self.books:
            if book.book_code == book_code:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.borrower_id = borrower_id
                    book.borrow_date = datetime.date.today()
                    book.history.append(f"Book borrowed by {borrower_id} on {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
                    print(f"Book '{book.title}' has been borrowed by {borrower_id}.")
                    return True
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                    return False
        print("Book not found.")
        return False

    def return_book(self, book_code):
        for book in self.books:
            if book.book_code == book_code:
                if book.is_borrowed:
                    book.is_borrowed = False
                    book.borrower_id = None
                    book.return_date = datetime.date.today()
                    book.history.append(f"Book returned on {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
                    print(f"Book '{book.title}' has been returned.")
                    return True
                else:
                    print(f"Book '{book.title}' is not borrowed.")
                    return False
        print("Book not found.")
        return False

    def borrowed_books(self):
        borrowed_books_list = [book for book in self.books if book.is_borrowed]
        return borrowed_books_list

def main():
    library = Library()
    library.add_nigerian_books()

    while True:
        print("\nWelcome to the Library Management System")
        print("1. View Books")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Borrowed Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            library.view_books()

        elif choice == '2':
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == '3':
            book_code = int(input("Enter collection number to borrow: "))
            borrower_id = input("Enter your ID: ")
            library.borrow_book(book_code, borrower_id)

        elif choice == '4':
            book_code = int(input("Enter collection number to return: "))
            library.return_book(book_code)

        elif choice == '5':
            print("\nBorrowed Books:")
            borrowed_books = library.borrowed_books()
            for book in borrowed_books:
                print(f"Collection Number: {book.book_code}, Title: {book.title}, Author: {book.author}, "
                      f"Genre: {book.genre}, ISBN: {book.isbn}, Borrower ID: {book.borrower_id}, "
                      f"Borrow Date: {book.borrow_date}, Return Date: {book.return_date}")

        elif choice == '6':
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
1