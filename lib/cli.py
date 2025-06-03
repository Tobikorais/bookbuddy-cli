from helpers import (
    add_book, list_books, add_genre, list_genres, 
    update_book_status, delete_book, add_review,
    get_book_statistics, get_top_rated_books, get_book_details
)
from db.models import ReadingStatus

def view_books_menu():
    print("\n--- View Books ---")
    print("1. View All Books")
    print("2. View Book Details")
    print("3. Sort Books")
    print("4. Return to Main Menu")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        books = list_books()
        if books:
            print("\nYour Book Collection:")
            print("-" * 50)
            for book in books:
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Status: {book.status.value}")
                print(f"Genre: {book.genre.name}")
                if book.publication_year:
                    print(f"Year: {book.publication_year}")
                if book.isbn:
                    print(f"ISBN: {book.isbn}")
                print("-" * 50)
        else:
            print("No books found.")
    
    elif choice == '2':
        title = input("Enter book title: ")
        books = list_books()
        found_book = next((book for book in books if book.title.lower() == title.lower()), None)
        if found_book:
            details = get_book_details(found_book)
            print("\nBook Details:")
            print("-" * 50)
            print(f"Title: {details['title']}")
            print(f"Author: {details['author']}")
            print(f"Status: {details['status']}")
            print(f"Genre: {details['genre']}")
            if details['publication_year']:
                print(f"Publication Year: {details['publication_year']}")
            if details['isbn']:
                print(f"ISBN: {details['isbn']}")
            print(f"Average Rating: {details['average_rating']}")
            
            if details['reviews']:
                print("\nReviews:")
                for review in details['reviews']:
                    print(f"- Rating: {review['rating']}/5")
                    if review['comment']:
                        print(f"  Comment: {review['comment']}")
                    print(f"  Date: {review['date']}")
            print("-" * 50)
        else:
            print("Book not found.")
    
    elif choice == '3':
        print("\nSort by:")
        print("1. Title")
        print("2. Author")
        print("3. Status")
        print("4. Genre")
        sort_choice = input("Enter your choice: ")
        
        sort_options = {
            '1': 'title',
            '2': 'author',
            '3': 'status',
            '4': 'genre'
        }
        
        if sort_choice in sort_options:
            books = list_books(sort_by=sort_options[sort_choice])
            if books:
                print("\nSorted Books:")
                print("-" * 50)
                for book in books:
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"Status: {book.status.value}")
                    print(f"Genre: {book.genre.name}")
                    print("-" * 50)
            else:
                print("No books found.")
        else:
            print("Invalid choice.")
    
    elif choice == '4':
        return
    
    else:
        print("Invalid choice.")

def main_menu():
    while True:
        print("\n--- BookBuddy CLI ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Genre")
        print("4. View Genres")
        print("5. Update Book Status")
        print("6. Delete Book")
        print("7. Add Review")
        print("8. View Statistics")
        print("9. View Top Rated Books")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Book Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            status_input = input("Status (to_read/reading/completed): ")
            publication_year = input("Publication Year (optional): ")
            isbn = input("ISBN (optional): ")
            try:
                status = ReadingStatus[status_input]
                add_book(
                    title, 
                    author, 
                    genre, 
                    status,
                    int(publication_year) if publication_year else None,
                    isbn if isbn else None
                )
                print("Book added successfully.")
            except KeyError:
                print("Invalid status. Please enter one of: to_read, reading, completed.")
            except ValueError:
                print("Invalid publication year. Please enter a valid number.")
        elif choice == '2':
            view_books_menu()
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
            title = input("Enter the title of the book to update: ")
            status_input = input("New Status (to_read/reading/completed): ")
            try:
                status = ReadingStatus[status_input]
                update_book_status(title, status)
                print("Book status updated successfully.")
            except KeyError:
                print("Invalid status. Please enter one of: to_read, reading, completed.")
        elif choice == '6':
            title = input("Enter the title of the book to delete: ")
            delete_book(title)
            print("Book deleted successfully.")
        elif choice == '7':
            title = input("Enter the title of the book to review: ")
            try:
                rating = float(input("Rating (1-5): "))
                if 1 <= rating <= 5:
                    comment = input("Comment (optional): ")
                    add_review(title, rating, comment)
                    print("Review added successfully.")
                else:
                    print("Rating must be between 1 and 5.")
            except ValueError:
                print("Invalid rating. Please enter a number between 1 and 5.")
        elif choice == '8':
            stats = get_book_statistics()
            print("\nBook Statistics:")
            print(f"Total Books: {stats['total_books']}")
            print("\nBooks by Status:")
            for status, count in stats['books_by_status'].items():
                print(f"{status}: {count}")
            print("\nAverage Ratings by Genre:")
            for genre, rating in stats['average_ratings'].items():
                print(f"{genre}: {rating}")
            print("\nBooks per Genre:")
            for genre, count in stats['genre_counts'].items():
                print(f"{genre}: {count}")
        elif choice == '9':
            top_books = get_top_rated_books()
            if top_books:
                print("\nTop Rated Books:")
                for title, author, rating in top_books:
                    print(f"{title} by {author} - Rating: {rating}")
            else:
                print("No rated books found.")
        elif choice == '10':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
