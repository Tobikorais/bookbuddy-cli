from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Genre, Book, ReadingStatus

engine = create_engine('sqlite:///bookbuddy.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add genres
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy']
for name in genres:
    genre = Genre(name=name)
    session.add(genre)

session.commit()

# Add books
books = [
    {'title': '1984', 'author': 'George Orwell', 'genre_name': 'Fiction', 'status': ReadingStatus.completed},
    {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'genre_name': 'Non-Fiction', 'status': ReadingStatus.to_read},
]

for book in books:
    genre = session.query(Genre).filter_by(name=book['genre_name']).first()
    new_book = Book(title=book['title'], author=book['author'], genre=genre, status=book['status'])
    session.add(new_book)

session.commit()
session.close()
