# books_library.py

# Database of books (you can expand this)
books_db = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951}
]

def search_books(query: str):
    """Search books by title, author, or year"""
    query = query.lower().strip()
    found = []

    for book in books_db:
        if (query == str(book["year"]).lower()
            or query in book["title"].lower()
            or query in book["author"].lower()):
            found.append(book)

    if found:
        print("\nBooks found:")
        for b in found:
            print(f"- {b['title']} ({b['year']}) by {b['author']}")
    else:
        print("Book not present in the library.")


if __name__ == "__main__":
    print("=== Welcome to the Book Library ===")
    while True:
        q = input("\nEnter book title/author/year (or 'exit' to quit): ")
        if q.lower() == "exit":
            break
        search_books(q)
