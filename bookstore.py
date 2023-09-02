def main():
    # Create a dictionary to store the books
    books = {}

    while True:
        print("\nBookshop Management System")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. Display all books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book's title: ")
            author = input("Enter the author's name: ")
            books[title] = author  # Add the book to the dictionary
            print(f"Book '{title}' by {author} added.")
        elif choice == '2':
            search_term = input("Enter the author's name or the book's title: ")
            if search_term in books:
                print(f"The book '{search_term}' is available by {books[search_term]}.")
            else:
                print(f"The book '{search_term}' is not available.")
        elif choice == '3':
            if books:
                print("List of Available Books:")
                for title, author in books.items():
                    print(f"Title: {title}, Author: {author}")
            else:
                print("No books available in the store.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
