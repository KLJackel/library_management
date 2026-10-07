# Book class representing individual books in the library
class Book:
    def __init__(self, title: str, author: str, is_available: bool = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __repr__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"

# Library class managing the collection of books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str) -> None:
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"\n[Success] Added: {new_book}")

    # Search for books by title or author (case-insensitive)
    def search_books(self, query: str) -> list:
        match_condition = lambda book: (
            query.lower() in book.title.lower() or 
            query.lower() in book.author.lower()
        )
        return list(filter(match_condition, self.books))
    
    # Update the availability status of a book by title using annonymous lambda function
    def update_availability(self, title: str, status: bool) -> bool:
        set_status = lambda book: setattr(book, 'is_available', status)
        
        for book in self.books:
            if book.title.lower() == title.lower():
                set_status(book)
                status_text = "Available" if status else "Checked Out"
                print(f"\n[Success] Updated '{book.title}' status to '{status_text}'.")
                return True
                
        print(f"\n[Error] Book titled '{title}' was not found.")
        return False

    def display_all(self) -> None:
        print("\n" + "=" * 35)
        print("     CURRENT LIBRARY INVENTORY     ")
        print("=" * 35)
        if not self.books:
            print(" No books currently in the library.")
        else:
            # iterate through the books and display them with their index
            for idx, book in enumerate(self.books, 1):
                print(f" {idx}. {book}")
        print("=" * 35)


def run_cli():
    library = Library()

    # Pre-populating with sample data for easier testing
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")

    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. View All Books")
        print("2. Add a New Book")
        print("3. Search Books")
        print("4. Toggle Book Availability")
        print("5. Exit")

        #/n creates a new line for better readability in the CLI 
        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            library.display_all()

        elif choice == "2":
            print("\n--- Add New Book ---")
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            
            if title and author:
                library.add_book(title, author)
            else:
                print("\n[Error] Title and author cannot be empty!")

        elif choice == "3":
            print("\n--- Search Inventory ---")
            query = input("Enter title or author to search for: ").strip()
            if query:
                results = library.search_books(query)
                print(f"\n--- Search Results ({len(results)} found) ---")
                if results:
                    for book in results:
                        #f is a string litoral that allows for insertion of the string values of variables directly into the string using curly braces {}
                        print(f" - {book}")
                else:
                    print(" No matching books found.")
            else:
                print("\n[Error] Search query cannot be empty!")

        elif choice == "4":
            print("\n--- Update Availability ---")
            title = input("Enter exact book title: ").strip()
            print("Select new status:")
            print("1. Mark as Checked Out (Unavailable)")
            print("2. Mark as Returned (Available)")
            
            status_choice = input("Enter choice (1-2): ").strip()
            if status_choice == "1":
                library.update_availability(title, False)
            elif status_choice == "2":
                library.update_availability(title, True)
            else:
                print("\n[Error] Invalid status selection!")

        elif choice == "5":
            print("\nExiting Library System. Goodbye!")
            break

        else:
            print("\n[Error] Invalid choice! Please select a option between 1 and 5.")


if __name__ == "__main__":
    run_cli()