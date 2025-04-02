import json
import os

# File to store book data
BOOKS_FILE = "books.json"

# Load books from JSON file
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save books to JSON file
def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

# Display books in a table format
def list_books(books):
    if not books:
        print("\n📚 No books in the library yet.\n")
        return

    print("\n📚 Your Library:\n")
    print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'Genre':<15} {'Year':<5}")
    print("=" * 80)
    for idx, book in enumerate(books, start=1):
        print(f"{idx:<5} {book['title']:<30} {book['author']:<20} {book['genre']:<15} {book['year']:<5}")
    print()

# Add a new book
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter book genre: ").strip()
    year = input("Enter publication year: ").strip()

    books.append({"title": title, "author": author, "genre": genre, "year": year})
    save_books(books)
    print(f"\n✅ '{title}' has been added to your library!\n")

# Remove a book by ID
def remove_book(books):
    list_books(books)
    if not books:
        return

    try:
        book_id = int(input("Enter book ID to remove: ")) - 1
        if 0 <= book_id < len(books):
            removed_book = books.pop(book_id)
            save_books(books)
            print(f"\n❌ '{removed_book['title']}' has been removed.\n")
        else:
            print("\n⚠️ Invalid book ID!\n")
    except ValueError:
        print("\n⚠️ Please enter a valid number!\n")

# Search for books by title, author, or genre
def search_books(books):
    query = input("Enter search term (title/author/genre): ").strip().lower()
    results = [book for book in books if query in book["title"].lower() or query in book["author"].lower() or query in book["genre"].lower()]

    if results:
        list_books(results)
    else:
        print("\n🔍 No books found matching your search.\n")

# Main menu
def main():
    books = load_books()

    while True:
        print("\n📖 Personal Library Manager")
        print("1️⃣ List all books")
        print("2️⃣ Add a book")
        print("3️⃣ Remove a book")
        print("4️⃣ Search for a book")
        print("5️⃣ Exit")
        
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            list_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            remove_book(books)
        elif choice == "4":
            search_books(books)
        elif choice == "5":
            print("\n📚 Goodbye! Happy Reading! 👋\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
