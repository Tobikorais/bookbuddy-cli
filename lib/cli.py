from helpers import add_book, list_books, add_genre, list_genres
from models import ReadingStatus

def main_menu():
    while True:
        print("\n--- BookBuddy CLI ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Genre")
        print("4. View Genres")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            status_input = input("Status (to_read/reading/completed): ")
            try:
                status = ReadingStatus[status_input]
                add_book(title, author, genre, status)
                print("Book added successfully.")
            except KeyError:
                print("Invalid status. Please enter one of: to_read, reading, completed.")
        elif choice == '2':
            books = list_books()
            if books:
                for book in books:
                    print(f"{book.title} by {book.author} - {book.status.value} [{book.genre.name}]")
            else:
                print("No books found.")
        elif choice == '3':
            name = input("Genre Name: ")
            if name.strip():
                add_genre(name)
                print("Genre added successfully.")
            else:
                print("Genre name cannot be empty.")
        elif choice == '4':
            genres = list_genres()
            if genres:
                for genre in genres:
                    print(genre.name)
            else:
                print("No genres found.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
