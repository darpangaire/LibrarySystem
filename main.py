from library import LibraryManagementSystem

def main():
    system = LibraryManagementSystem()

    while True:
        print("\n📚 Library Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search by ID")
        print("4. Search by Title")
        print("5. Delete Book (Admin Only)")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            system.enter_book_list()
        elif choice == '2':
            system.book_List()
        elif choice == '3':
            book_id = input("Enter Book ID: ")
            system.search_id(book_id)
        elif choice == '4':
            title = input("Enter Book Title: ")
            system.search_title(title)
        elif choice == '5':
            system.delete()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
